from fastapi import FastAPI
from entities import File
from os import listdir
from os.path import isfile, join
from typing import List


app = FastAPI()
folder_with_files: str = '../../user_files/'


@app.get("/")
async def root() -> dict:
    """

    Returns:
        json with greetings

    """
    return {"message": "Hello World"}


@app.get("/list_files/")
async def list_files() -> List[str]:
    """

    Returns:
        list of files which are enabled to download from server to user

    """
    return [f for f in listdir(folder_with_files) if isfile(join(folder_with_files, f))]


@app.post("/upload")
async def upload(body: File) -> None:
    """

    Args:
        body (): File which user want to upload to server

    Returns:
        None

    """
    with open(join(folder_with_files, body.filename), 'w') as f:
        f.write(body.data)


@app.get("/download")
async def download(filename: str) -> str:
    """

    Args:
        filename (): name of file which user want to download

    Returns:
        data of file with name `filename`

    """
    with open(join(folder_with_files, filename), 'r') as f:
        return f.read()
