from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from Model import Post


my_posts = [{"title": "content of posts 1", "content": "content of post 1", "id": "1"}, 
{"title": "content of post 2", "content": "content of post 2", "id": "2"}]

app = FastAPI()



@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post_ID(id: int):
    for post in my_posts:
        if post["id"] == id:
            return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_blog(request: Post):
    new_post = request.model_dump()
    new_post = request.dict()
    my_posts.append(new_post)
    return {"data": new_post}
    
@app.delete("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_post(request: Post):
    
    new_posts = [post for post in my_posts if post["id"] != id]