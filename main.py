from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return "hii"


@app.get('/events/{event_id}')
def event(event_id:str):
    return {'event_no':event_id}