import pytest

from server.src.main import sum
import requests


def test_main():
    assert sum(2, 2) == 4, "kek"


url = 'http://localhost:8000/'
data = 'data'


def check_status_code(r):
    assert r.status_code == 200, f'expected 200, but status_code = {r.status_code}'


def test_list_files():
    path = 'list_files'
    r = requests.get(url + path)
    check_status_code(r)
    assert r.json() == ['test1', 'test2'], f'expected empty list, but have {r.json()}'


@pytest.fixture
def filename():
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
