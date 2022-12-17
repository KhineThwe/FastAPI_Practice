from fastapi import FastAPI
app = FastAPI()

@app.get("/")#to act like an api ---> magic method#get request to user-----> 
#we can use other http method instead of get
#http://127.0.0.1:8000  = http://127.0.0.1:8000/
#we can remove async too
async def root():
    return{"message":"welcome to my api"}
#fastapi python dict to json