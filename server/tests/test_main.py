from server.src.main import sum
import requests


def test_main():
    assert sum(2, 2) == 4, "kek"


url = 'http://localhost/api/'
data = 'data'


def check_status_code(r):
    assert r.status_code == 200, f'expected 200, but status_code = {r.status_code}'


def test_list_files():
    path = 'list_files'
    r = requests.get(url + path)
    check_status_code(r)
    assert r.json() == '[]', f'expected empty list, but have {r.json()}'


def test_upload():
    path = 'upload'
    body = {'filename': data}
    r = requests.post(url + path, json=body)
    check_status_code(r)


def test_download():
    path = 'download'
    params = {'filename': 'filename'}
    r = requests.get(url + path, params=params)
    check_status_code(r)
    assert r.json() == 'data', f'expected data = {data}, but have {r.json()}'
