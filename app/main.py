from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()
my_posts = [{"title": "top","content": "check out","rating": 5,"id": 1},
{"title": "bottom","content": "check in","rating": 5,"id": 2},
]
class Post(BaseModel):#extends 
    title:str
    content:str
    published:bool = True
    rating:Optional[int] = None
    
@app.get("/")#to act like an api ---> magic method#get request to user-----> 
#we can use other http method instead of get
#http://127.0.0.1:8000  = http://127.0.0.1:8000/
#we can remove async too
async def root():
    return{"message":"welcome to my api"}
#fastapi python dict to json

#get all
@app.get("/posts")
def get_posts():
    return{"data":my_posts}

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
        
#if route is similar,this post must be top
@app.get("/post/next")
def get_next(): 
    return {"data":"next routh"}

#get one
@app.get("/posts/{id}")
def get_one_posts(id:int):
    rPost = find_post(id)
    #for မရှိတဲ့ id
    if not rPost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} was not found!')
    return{"data":rPost}

#create
@app.post("/createposts")
def create_posts(new_post:Post,status_code=status.HTTP_201_CREATED):
    dict_data = new_post.dict()
    dict_data['id'] = randrange(0,10000000)
    my_posts.append(dict_data)
    return {"data":my_posts}
#title str,content str,category,Book published

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == i:
            return i
#update
#get ll ya
@app.put("/posts/{id}")
def update_post(id:int,new_post:Post):#ပြင်စရာbody ပါပါ
    dic_post = new_post.dict()
    index = find_index_post(id)#id နဲ့တူတဲ့ index no ရမယ်
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} was not found!')
    dic_post['id'] = id
    my_posts[index] = dic_post
    return {"data":dic_post}

#delete
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id:{id} was not found!')
    my_posts.pop(index)
    return {"data":"Successfully Deleted!"}
