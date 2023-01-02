from fastapi import APIRouter,Depends,status,HTTPException
from httplib2 import GoogleLoginAuthentication
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm,OAuth2AuthorizationCodeBearer
from .. import schemas,database,models

from .. import hashing,JWTtoken


from firebase_admin import auth


router = APIRouter(
    tags=["Authentication"],
)

get_db=database.get_db

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    print(user)
    if not user: #check username
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials") 

    elif not hashing.Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")  # chnage password to credential 

    access_token = JWTtoken.create_access_token(data={"email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/lg',status_code=status.HTTP_202_ACCEPTED)
def loginGoogle(request:schemas.TokenSchema,db:Session=Depends(get_db)):
    try:
        print(request.idToken)
        decoded_token = auth.verify_id_token(request.idToken)
        uid = decoded_token
        print('hrer',uid)
    except :
        print('id verification error')
        return 'expired'

    user=db.query(models.User).filter(models.User.email==request.email).first()

    if not user: #check username
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials") 
    print( request.email)
    access_token = JWTtoken.create_access_token(data={"email": user.email})
    return access_token


