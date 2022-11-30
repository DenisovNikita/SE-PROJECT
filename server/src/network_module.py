from fastapi import FastAPI
from entities import File
from os import listdir
from os.path import isfile, join
from typing import List, Optional
import logging

app = FastAPI()
folder_with_files: str = '../../user_files/'


@app.get("/")
async def root() -> dict:
    """Endpoint for empty path.

    Returns:
        dict: A json with greetings.

    """
    return {"message": "Hello World"}


@app.get("/list_files/")
async def list_files() -> List[str]:
    """Endpoint for listing files which are enabled to download from server to user.

    Returns:
        List[str]: Filenames of appropriate files.

    """
    return [f for f in listdir(folder_with_files) if isfile(join(folder_with_files, f))]


@app.post("/upload")
async def upload(body: File) -> bool:
    """Endpoint for upload file from user to server.

    Args:
        body (File): File with filename and data which user want to upload to server.

    Returns:
        bool: Is file have been successfully uploaded.

    """
    try:
        with open(join(folder_with_files, body.filename), 'w') as f:
            f.write(body.data)
        return True
    except:
        logging.error(f'File with name "{body.filename}" cannot be uploaded.')
    return False


@app.get("/download")
async def download(filename: str) -> Optional[str]:
    """Endpoint for download file to user from server.

    Args:
        filename (str): Name of file which user want to download.

    Returns:
        Optional[str]: Data of file with name `filename` if it exists or None else.

    """
    try:
        with open(join(folder_with_files, filename), 'r') as f:
            return f.read()
    except:
        logging.error(f'File with name "{filename}" does not exist.')
