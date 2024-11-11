import json
from fastapi import FastAPI, HTTPException

# Membaca data dari file JSON
with open("response.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

@app.get('/post/{item_id}')
async def read_post(item_id: int):
    for post in data:
        if post['id'] == item_id:
            return post
    raise HTTPException(
        status_code=404, detail=f'Post with ID {item_id} not found'
    )
