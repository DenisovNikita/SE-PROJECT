from fastapi import FastAPI
from os import listdir
from os.path import isfile, join


app = FastAPI()
folder_with_files = '../../user_files/'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/list_files/")
async def list_files():
    return [f for f in listdir(folder_with_files) if isfile(join(folder_with_files, f))]
