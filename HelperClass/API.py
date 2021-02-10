import requests

from jsonschema import validate, SchemaError


class RESTClient:
    @staticmethod
    def GetRequest(url, endpoint):
        response = requests.get(url + endpoint)
        return response

    @staticmethod
    def PostRequest(url, endpoint, payload):
        response = requests.post(url + endpoint, json=payload)
        return response

    @staticmethod
    def DeleteRequest(url, endpoint, categoryid):
        response = requests.delete(url + endpoint + categoryid)
        return response

    @staticmethod
    def ValidateJson(data, schema):
        try:
            validate(data, schema)
        except SchemaError as e:
            print("Schema error detected")

        return


