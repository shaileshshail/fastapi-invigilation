from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database
from sqlalchemy.orm import Session

from ..repository import user
from .. import oauth2

router=APIRouter(
    tags=['Users'],
    prefix='/user',
    dependencies=[Depends(oauth2.get_current_user)] # route behind authentication 

)

get_db=database.get_db

@router.get('/{email}/',response_model=schemas.UserResponseSchema)
def getUser(email:str,db:Session = Depends(get_db)):
    return user.get_user(email,db)
    
    
@router.post('/')
def addUser(request:schemas.UserSchema,db:Session = Depends(get_db)):
    return user.add_user(request,db)

    