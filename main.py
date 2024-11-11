import json
from fastapi import FastAPI

# Membaca data dari file JSON
with open("response.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

# Endpoint untuk mendapatkan seluruh data
@app.get("/posts")
async def get_all_posts():
    return data
