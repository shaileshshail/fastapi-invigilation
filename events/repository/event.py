from fastapi import HTTPException,status
import ast,json,random,datetime
from sqlalchemy.orm import load_only
from dateutil import parser
import json
from fastapi.encoders import jsonable_encoder

from ..import models

def add_event(request,db):
    classrooms=ast.literal_eval(request.classrooms)  # convert string list to list
    staff_from_db=db.query(models.Staff).options(load_only(models.Staff.email,models.Staff.name)).all()
    staff_list=list(map(lambda x:[x.name,x.email],staff_from_db)) #all staff in list

    staff_list=random.sample(staff_list,len(classrooms))  #random staffs for each class
    staff_list=json.dumps(staff_list)

    new_event=models.Event(__tablename__ = "events",
                            id=random.randrange(0,1000), 
                            title=request.title,
                            session=request.session,
                            date=request.date,
                            classrooms=request.classrooms,
                            staffs=staff_list)


    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    
    return staff_list

def delete_event(id,db):
    db.query(models.Event).filter(models.Event.id==id).delete(False)
    db.commit()

    return 'deleted successfully'


def get_all_event(db):
    events=db.query(models.Event).all()
    
    json_compatible_item_data = jsonable_encoder(events)
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message
    return json_compatible_item_data

def get_one_event(id,db):
    events=db.query(models.Event).filter(models.Event.id==id).first()   #.first() is impo
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message
    return events

def update_event(id,request,db):
    events=db.query(models.Event).filter(models.Event.id==id)
    if not events.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message

    request=request.dict() #json to dict
    request['date']=parser.parse(request['date']) #string date to python datetime

    classrooms_count=len(ast.literal_eval(request['classrooms'])) # input classroom length

    if not len(events.first().classrooms)==classrooms_count:
        staff_from_db=db.query(models.Staff).options(load_only(models.Staff.email,models.Staff.name)).all()
        staff_list=list(map(lambda x:[x.name,x.email],staff_from_db)) #all staff in list

        staff_list=random.sample(staff_list,classrooms_count)  #random staffs for each class
        staff_list=json.dumps(staff_list)
        request['staffs']=staff_list 

    events.update(request)
    db.commit()

    return "updated"