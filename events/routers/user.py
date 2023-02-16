from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database
from sqlalchemy.orm import Session

from ..repository import user
from .. import oauth2

router=APIRouter(
    tags=['Users'],
    prefix='/user',
    #dependencies=[Depends(oauth2.get_current_user)] # route behind authentication 

)

get_db=database.get_db

@router.get('/all')
def getUser(db:Session = Depends(get_db)):
    return user.get_users(db)
    
    
@router.post('/add')
def addUser(request:schemas.UserSchema,db:Session = Depends(get_db)):
    return user.add_user(request,db)

@router.delete('/delete/{email}')
def deleteUser(email:str,db:Session = Depends(get_db)):
    return user.delete_user(email,db)