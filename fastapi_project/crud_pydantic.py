# crud_pydantic.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class CreateIn(BaseModel):
    name: str
    nickname: str
    
class CreateOut(BaseModel):
    status: str
    id: int
    

app = FastAPI()

USER_DB = {} 

# Fail response 
NAME_NOT_FOUND = HTTPException(status_code=400, 
                               detail="Name not found.")

    
# Create
@app.post("/users", response_model=CreateOut)
def create_user(user: CreateIn):
    USER_DB[user.name] = user.nickname
    user_dict = user.dict()
    user_dict["status"] = "success"
    user_dict["id"] = len(USER_DB)
    return user_dict

# Read
@app.get("/users/")
def read_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    return {"nickname": USER_DB[name]}

# Update : name, nickname
@app.put("/users/")
def update_user(name: str, nickname: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    USER_DB[name] = nickname
    return {"status": "success"}


# Delete : name
@app.delete("/users/")
def delete_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    del USER_DB[name]
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

