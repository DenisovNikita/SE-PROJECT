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
    path = 'list_files'
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


def test_upload(filename):
    path = 'upload'
    body = {'filename': filename, 'data': data}
    r = requests.post(url + path, json=body)
    check_status_code(r)


def test_download(filename):
    path = 'download'
    params = {'filename': filename}
    r = requests.get(url + path, params=params)
    check_status_code(r)
    return r.json()


def test_upload_and_download():
    filename = 'test_fastapi'
    test_upload(filename)
    res = test_download(filename)
    assert res == 'data', f'expected data = {data}, but have {res}'
