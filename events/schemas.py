from pydantic import BaseModel

class EventSchema(BaseModel):
    title:str 
    date:str = "2005-06-12"
    session:str = "FN"
    classrooms: str = "[ ]"

class UserSchema(BaseModel):
    email:str
    privilege:str



class TokenSchema(BaseModel):
    federatedId: str
    providerId: str
    email: str
    emailVerified: bool
    firstName: str
    fullName: str
    lastName: str
    photoUrl: str
    localId: str
    displayName: str
    idToken: str
    context: str
    oauthAccessToken: str
    oauthExpireIn: int
    refreshToken: str
    expiresIn: str
    oauthIdToken: str
    rawUserInfo: str
    kind: str