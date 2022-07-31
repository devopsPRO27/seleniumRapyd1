import json

import requests
import pytest

url = 'http://127.0.0.1:5000/users'

payload = {'id':5,'name':'hodi','address':'naura'}

#json_payload=json.load(payload)

response= requests.post(url,json = payload)

def test_get():
    flag = True
    get_response = requests.get(url)

    list_of_users =get_response.json()
    expected = list_of_users[-1]

    for k in expected.keys():
        if expected[k] != payload[k]:
            flag = False
    assert flag

