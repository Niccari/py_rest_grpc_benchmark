from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from random_generator import generate_id
from random_generator import generate_string


app = FastAPI()


@app.get("/")
def fetch_empty():
    return {}


@app.get("/contents")
def fetch_content(count: int):
    return {
        "data": [{
            "id": generate_id(),
            "hoge": generate_string(),
        } for i in range(count)]
    }


@app.post("/texts")
def post_text(file: UploadFile = File(...)):
    return {}


@app.post("/images")
def post_image(file: UploadFile = File(...)):
    return {}
