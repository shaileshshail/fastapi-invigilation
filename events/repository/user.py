from fastapi import HTTPException,status
from ..import models,hashing
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


def get_users(db:Session):
    users=db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"no user available with email ") #to return custom status code and error message
    print(jsonable_encoder(users))
    return users

def add_user(request,db:Session):
    hashedPassword=hashing.Hash.bcrypt('123')
    name='hehe'
    print(request)
    new_user=models.User(email=request.email,name=name,password=hashedPassword,privilege=request.privilege)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(email,db):
    db.query(models.User).filter(models.User.email==email).delete(False)
    db.commit()

    return 'deleted successfully'