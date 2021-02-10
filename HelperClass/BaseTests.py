

class BasicTests:
    def VerifyBaseTests(self, expected, response):
        self.assertEqual(expected, response.status_code)

        self.assertEqual(expected, response.headers["content-type"])

