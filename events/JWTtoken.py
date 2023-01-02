import json
from fastapi import Depends
from jose import JWTError,jwt
from datetime import datetime,timedelta
import firebase_admin
from sqlalchemy.orm import Session

from events import database
from . import schemas,models
get_db=database.get_db

options = {
    'serviceAccountId': 'firebase-adminsdk-kcyck@invigilation-e3fe5.iam.gserviceaccount.com',
}
from firebase_admin import credentials
key1="invigilation-9cc29-firebase-adminsdk-z5jv1-ce45484260.json"
cred = credentials.Certificate(key1)
firebase_admin.initialize_app(credential=cred)

data=open(key1)
data=json.load(data)
SECRET_KEY=data['private_key']

ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=5)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
