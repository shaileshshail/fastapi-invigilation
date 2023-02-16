from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session

from .. import schemas,database

from ..repository import staff
from fastapi.responses import FileResponse

from .. import oauth2

router = APIRouter(
    tags=["Staff"],
    prefix='/staff',
    #dependencies=[Depends(oauth2.get_current_user)] # route behind authentication 
)

get_db=database.get_db

@router.get('/{date}')
def getAllEvent(date:str,db: Session = Depends(get_db)):
    print(date)
    return staff.get_all_staff(date,db)

