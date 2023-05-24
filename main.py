from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"key": "Hello"}

@app.get('/{pk}')
def get_item(pk:int):
    return {"key": pk}