from .database import Base
from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.sql import func
import datetime
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer,primary_key=True,index=True)
    title =Column(String)
    date =Column(String)
    session = Column(String)
    classrooms = Column(String)
    staffs = Column(String)
    backup = Column(String)

class Staff(Base):
    __tablename__ = "staff"

    biometric_id= Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    dept= Column(String)

class User(Base):
    __tablename__ = "User"

    email = Column(String,primary_key=True)
    name = Column(String)
    password= Column(String)
    privilege= Column(String)
    
class Classrooms(Base):
    __tablename__ = "classrooms"

    room_no = Column(String,primary_key=True)
    floor = Column(String)
    block = Column(String)

class PresentStaff(Base):
    __tablename__ = "presentstaff"

    id = Column(Integer,primary_key=True,autoincrement=True)
    date = Column()
    data = Column(String)
