from fastapi import HTTPException,status
from ..import models,hashing
from sqlalchemy.orm import Session


def get_user(email,db:Session):
    user=db.query(models.User).filter(models.User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user available with email {email}") #to return custom status code and error message
    return user

def add_user(request,db:Session):
    hashedPassword=hashing.Hash.bcrypt(request.password)

    new_user=models.User(email=request.email,name=request.name,password=hashedPassword)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user