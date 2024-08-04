# crud_query.py

from fastapi import FastAPI, HTTPException

app = FastAPI()

# User database
USER_DB = {}

# Fail response 
NAME_NOT_FOUND = HTTPException(status_code=400, 
                               detail="Name not found.")

# Create
@app.post("/users")
def create_user(name: str, nickname: str):
    USER_DB[name] = nickname
    return {"status": "success"}

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


