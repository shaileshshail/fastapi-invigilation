from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2AuthorizationCodeBearer
from . import JWTtoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
oauth2_scheme1 = OAuth2AuthorizationCodeBearer(tokenUrl="lg",authorizationUrl='lg')#recap from fastapi bitumes video


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print('inside  oauth get_current_user------------------------------------------')
    return JWTtoken.verify_token(token,credentials_exception)
    