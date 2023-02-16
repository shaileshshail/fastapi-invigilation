from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import models
from .database import engine,SessionLocal,get_db

from fastapi.middleware.cors import CORSMiddleware

from .routers import user,event,authentication,staff

from .repository.biometric import bio_data

import schedule,time

app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(staff.router)
origins = [
    "http://localhost:4200",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from .repository import biometric

