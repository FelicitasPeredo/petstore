import requests
import json
from jsonschema import validate
from jsonschema.exceptions import *

with open("C:\\Users\\Felicitas Peredo\\Documents\\petstore\\schema.json") as json_file:
    schema = json.load(json_file)

def test_post_pet():
    url = "https://petstore.swagger.io/v2/pet?"
    payload = json.dumps({
    "id": 2,
    "category": {
        "id": 1,
        "name": "small dog"
    },
    "name": "raul",
    "photoUrls": [
        "https://thumbs.dreamstime.com/b/fall-beagle-dog-pet-outdoors-35091247.jpg"
    ],
    "tags": [
        {
        "id": 2,
        "name": "bruno"
        }
    ],
    "status": "sold"
    })
    headers = {
    'api_key': '55887744555874',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # check the schema of the response
    if response.status_code == 200:
        response_data = response.json()
        try:
            validate(instance=response_data, schema=schema)
        except ValidationError as e:
            print("The instance is invalid. Reason: ", e)
        except SchemaError as e:
            print("The schema is invalid. Reason: ", e)

    # check the status code of the response
    assert response.status_code == 200, f"STATUS CODE: {response.status_code}"

def test_get_pet():
    url = "https://petstore.swagger.io/v2/pet/2"
    payload={}
    headers = {
    'api_key': '55887744555874',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # check the schema of the response
    if response.status_code == 200:
        response_data = response.json()
        try:
            validate(instance=response_data, schema=schema)
        except ValidationError as e:
            print("The instance is invalid. Reason: ", e)
        except SchemaError as e:
            print("The schema is invalid. Reason: ", e)


    # check the status code of the response
    assert response.status_code == 200, f"STATUS CODE: {response.status_code}"

def test_put_pet():
    url = "https://petstore.swagger.io/v2/pet"
    payload = json.dumps({
    "id": 1,
    "category": {
        "id": 1,
        "name": "small dog"
    },
    "name": "bruno",
    "photoUrls": [
        "https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg"
    ],
    "tags": [
        {
        "id": 1,
        "name": "bruno"
        }
    ],
    "status": "pending"
    })
    headers = {
    'api_key': '55887744555874',
    'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    # check the schema of the response
    if response.status_code == 200:
        response_data = response.json()
        try:
            validate(instance=response_data, schema=schema)
        except ValidationError as e:
            print("The instance is invalid. Reason: ", e)
        except SchemaError as e:
            print("The schema is invalid. Reason: ", e)

    # check the status code of the response
    assert response.status_code == 200, f"STATUS CODE: {response.status_code}"