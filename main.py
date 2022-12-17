from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()
class Post(BaseModel):#extends 
    title:str
    content:str
    
@app.get("/")#to act like an api ---> magic method#get request to user-----> 
#we can use other http method instead of get
#http://127.0.0.1:8000  = http://127.0.0.1:8000/
#we can remove async too
async def root():
    return{"message":"welcome to my api"}
#fastapi python dict to json

@app.get("/posts")
def get_posts():
    return{"message":"This is your posts"}

@app.post("/createposts")
def create_posts(payload:dict=Body(...)):
    print(payload)
    return {"new_post":f"title:{payload['title']} content:{payload['content']}"}
#title str,content str,category,Book published
