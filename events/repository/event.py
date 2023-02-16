from fastapi import HTTPException,Response,status
import ast,json,random,datetime
from sqlalchemy.orm import load_only
from dateutil import parser
import json,math
from fastapi.encoders import jsonable_encoder

from ..import models

def add_event(request,db):
    def check_duplicate():
        event_list=db.query(models.Event).all()
        event_list=list(map(lambda x:[x.date,x.session],event_list))
        print(event_list,'\n',request.date,request.session)
        for (date,session) in event_list:
            print(date==request.date and session==request.session)
            if date==request.date and session==request.session:
                print('same')
                return 'same'
        return 'different'
        print(event_list)
    check=check_duplicate()
    if check=='same':
        return 'same event exist'
    
    classrooms=ast.literal_eval(request.classrooms)  # convert string list to list
    staff_from_db=db.query(models.Staff).options(load_only(models.Staff.email,models.Staff.name)).all()
    all_staff_list=list(map(lambda x:[x.name,x.email],staff_from_db)) #all staff in list

    staff_list=random.sample(all_staff_list,len(classrooms))  #random staffs for each class
    print('staff_list',staff_list)
    staff_list_json=json.dumps(staff_list)
    print(classrooms)
    backup_list=getBackupstaff(staff_list=staff_list,all_staff_list=all_staff_list)

    backup_list=json.dumps(backup_list)
    new_event=models.Event(__tablename__ = "events",
                            id=random.randrange(0,1000), 
                            title=request.title,
                            session=request.session,
                            date=request.date,
                            classrooms=request.classrooms,
                            staffs=staff_list_json,
                            backup=backup_list)


    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    
    return 'added successfully'

def delete_event(id,db):
    db.query(models.Event).filter(models.Event.id==id).delete(False)
    db.commit()

    return 'deleted successfully'


def get_all_event(db):
    events=db.query(models.Event).all()
    
    json_compatible_item_data = jsonable_encoder(events)
    if not events:
        return Response(content="No Events Found",status_code=status.HTTP_200_OK) #to return custom status code and error message
    return json_compatible_item_data

def get_one_event(id,db):
    events=db.query(models.Event).filter(models.Event.id==id).first()   #.first() is impo
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message
    return events

def getBackupstaff(staff_list,all_staff_list):
    backup_list=[]
    backup_count=math.ceil(len(staff_list)*7/100)
    for i in all_staff_list:
        val=random.sample(all_staff_list,1)[0]
        print(val)
        if val not in staff_list and val not in backup_list :
            print('inside')
            backup_list.append(val)
        if len(backup_list)>= 5:      #backup count value
            break
    return backup_list 

def update_event(id,request,db):
    events=db.query(models.Event).filter(models.Event.id==id)
    print("dataaaa",events[0].__dict__)

    if not events.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message

    request=request.dict() #json to dict
    request['date']=parser.parse(request['date']) #string date to python datetime

    classrooms_count=len(ast.literal_eval(request['classrooms'])) # input classroom length

    if len(events.first().classrooms)!=classrooms_count and events[0].__dict__['classrooms']!=request['classrooms']:#and request['classrooms']!=events['classrooms']
        staff_from_db=db.query(models.Staff).options(load_only(models.Staff.email,models.Staff.name)).all()
        all_staff_list=list(map(lambda x:[x.name,x.email],staff_from_db)) #all staff in list

        staff_list=random.sample(all_staff_list,classrooms_count)  #random staffs for each class
        staff_list_json=json.dumps(staff_list)
        request['staffs']=staff_list_json
    
        backup_list=backup_list=getBackupstaff(staff_list=staff_list,all_staff_list=all_staff_list)

                
        backup_list=json.dumps(backup_list)
        request['backup']=backup_list

    events.update(request)
    db.commit()

    return "updated"

def get_all_classrooms(db):
    classrooms=db.query(models.Classrooms).all()
    unique=[]
    ret=[]
    for classroom in classrooms:
        k={}
        if classroom.block not in unique:
            unique.append(classroom.block)
        k['room_no']=classroom.room_no
        k['floor']=classroom.floor
        k['block']=classroom.block
        ret.append(k)
    print(unique)
    
    json_compatible_item_data = jsonable_encoder(ret)
    print(jsonable_encoder)
    print(type(jsonable_encoder))
    if not classrooms:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not available with id {id}") #to return custom status code and error message
    return json_compatible_item_data,unique
