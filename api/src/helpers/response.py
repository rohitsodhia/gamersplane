class Response:
    def __init__(self):
        self.reset()

    def reset(self):
        self._success = False
        self._data = {}
        self._errors = {}
        self._response_code = 200

    def set_success(self, success):
        self._success = success

    def add_data(self, values):
        self._data.update(values)

    def add_errors(self, values):
        self._errors.update(values)

    def set_response_code(self, response_code):
        self._response_code = response_code

    def build(self, **kwargs):
        if kwargs.get("success"):
            self.set_success(kwargs["success"])
        if kwargs.get("data"):
            self.add_data(kwargs["data"])
        if kwargs.get("errors"):
            self.add_errors(kwargs["errors"])
        if kwargs.get("response_code"):
            self.set_response_code(kwargs["response_code"])

        response = {"success": self._success}
        if self._data:
            response["data"] = self._data
        if self._errors:
            response["errors"] = self._errors

        return response, self._response_code

    def success(self, data):
        return self.build(data=data, success=True, response_code=200)

    def errors(self, errors, response_code=200):
        return self.build(errors=errors, success=False, response_code=response_code)

    def unauthorized(self, errors=None):
        if not errors:
            errors = {"unauthorized": True}
        return self.errors(errors=errors, response_code=401)


response = Response()
