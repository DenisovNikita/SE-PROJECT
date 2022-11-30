from typing import Any

import pytest
from requests import Response

from server.src.main import sum
import requests


def test_main() -> None:
    """Test for checking pytest workability.

    Returns:
        None.

    """
    assert sum(2, 2) == 4, "kek"


url: str = 'http://localhost:8000/'
data: str = 'data'


def check_status_code(r: Response) -> None:
    """Test for checking status code of network response.

    Args:
        r (Response): Network response.

    Returns:
        None.

    """
    assert r.status_code == 200, f'expected 200, but status_code = {r.status_code}'


def test_list_files() -> None:
    """Test for endpoint `list_files`.

    Returns:
        None.

    """
    path: str = 'list_files'
    r: Response = requests.get(url + path)
    check_status_code(r)
    assert r.json() == ['test1', 'test2'], f'expected empty list, but have {r.json()}'


@pytest.fixture
def filename() -> str:
    """Experiment with fixtures.

    Returns:
        str: Generated filename.

    """
    return 'kek'


def test_upload(filename: str) -> None:
    """Test for endpoint `upload`.

    Args:
        filename (str): Name of file which user want to upload.

    Returns:
        None.

    """
    path: str = 'upload'
    body: dict = {'filename': filename, 'data': data}
    r: Response = requests.post(url + path, json=body)
    check_status_code(r)


def test_download(filename: str) -> Any:
    """Test for endpoint `download`.

    Args:
        filename (str): Name of file which user want to download.

    Returns:
        Any: A json of network response.

    """
    path: str = 'download'
    params: dict = {'filename': filename}
    r: Response = requests.get(url + path, params=params)
    check_status_code(r)
    return r.json()


def test_upload_and_download() -> None:
    """Complex test for download same file as was uploaded before.

    Returns:
        None.

    """
    filename: str = 'test_fastapi'
    test_upload(filename)
    res: Any = test_download(filename)
    assert res == 'data', f'expected data = {data}, but have {res}'
