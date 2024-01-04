import requests

endpoint = "https://"

get_response = requests.get(endpoint, params={"abc": 123},
                            json={"query": "Hello"})