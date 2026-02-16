from fastapi import FastAPI

app=FastAPI()

users=[
        {
            "name":"nitin",
            "age":21
        }
        ,{
            "name":"Alex",
            "age":22
        }
    ]

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def post_users(user):
    users.append(user)
    return 

@app.put("/users/{id}")
def put_user():
    pass

@app.delete("/users/{name}")
def delete_user(name):
    tempusers=list()
    for user in users:
        if user["name"]!=name:
            tempusers.append(user)