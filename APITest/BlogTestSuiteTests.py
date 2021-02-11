import unittest
import ddt as ddt

from HelperClass.APIUrl import URL
from HelperClass.RESTClient import RESTClient
from SchemaFiles.Schemas import Schema
from HelperClass.APIEndpoints import Endpoint


@ddt.ddt
class APITestCases(unittest.TestCase):
    def test_CategoryList(self):
        response = RESTClient.GetRequest(URL.BaseURL, Endpoint.BlogCategory)
        # Status Code verification
        self.assertEqual(200, response.status_code)
        # Content-Type verification
        self.assertEqual('application/json', response.headers['content-type'])

        RESTClient.ValidateJson(response.json(), Schema.ListCategorySchemas)

    @ddt.data(('Engineering'), ('Cookery'), ('Science'))
    def test_AddCategory(self, category):
        response = RESTClient.PostRequest(URL.BaseURL, Endpoint.BlogCategory, {"name": ""+category+""})
        # Status Code verification
        self.assertEqual(201, response.status_code)
        # Content-Type verification
        self.assertEqual('application/json', response.headers['content-type'])

    @ddt.data(('4', 204), ('5', 204), ('6', 204), ('20', 404))
    @ddt.unpack
    def test_DeleteCategory(self, category_id, status_code):
        response = RESTClient.DeleteRequest(URL.BaseURL, Endpoint.BlogCategory, category_id)
        # Status Code verification
        self.assertEqual(status_code, response.status_code)
        # Content-Type verification
        self.assertEqual('application/json', response.headers['content-type'])

    @ddt.data(('1', 200), ('20', 404))
    @ddt.unpack
    def test_BlogList(self, category_id, status_code):
        response = RESTClient.GetRequest(URL.BaseURL, Endpoint.BlogCategory + category_id)
        # Status Code verification
        self.assertEqual(status_code, response.status_code)
        # Content-Type verification
        self.assertEqual('application/json', response.headers['content-type'])


if __name__ == '__main__':
    unittest.main()
