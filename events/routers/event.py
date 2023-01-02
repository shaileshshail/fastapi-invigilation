from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session

from .. import schemas,database

from ..repository import event

from .. import oauth2

router = APIRouter(
    tags=["Events"],
    prefix='/event',
    dependencies=[Depends(oauth2.get_current_user)] # route behind authentication 
)

get_db=database.get_db



@router.post('/add',status_code=status.HTTP_201_CREATED)
def addEvent(form:schemas.EventSchema,db: Session = Depends(get_db)):
    return event.add_event(form,db)  


@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleteEvent(id:int,db: Session = Depends(get_db)):
    return event.delete_event(id,db)


@router.get('/')
def getAllEvent(db: Session = Depends(get_db)):
    return event.get_all_event(db)


@router.get('/{id}')
def getOneEvent(id:int,db: Session = Depends(get_db)):
    return event.get_one_event(id,db)


@router.put('/update/{id}')
def updateEvent(id:int,form:schemas.EventSchema,db:Session = Depends(get_db)):
    return event.update_event(id,form,db)






