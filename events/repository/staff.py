from fastapi import Response,status
from ..import models
from fastapi.encoders import jsonable_encoder
import json
json.dump
def get_all_staff(date,db):
    staff_list=db.query(models.PresentStaff).filter(models.PresentStaff.date==date).first()
    print(type(staff_list))
    print("iniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    if not staff_list:
        return 'null' #to return custom status code and error message
    return staff_list