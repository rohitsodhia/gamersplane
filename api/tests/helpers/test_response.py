from faker import Faker

from helpers.response import Response

faker = Faker()


class TestResponse:
    def test_build_success(self):
        response = Response()

        success = True
        data = {faker.random_letter(): faker.random_digit()}
        errors = {faker.random_letter(): faker.random_digit()}
        response_code = 400

        response_body, returned_response_code = response.build(
            success=success, data=data, errors=errors, response_code=response_code
        )
        assert returned_response_code == response_code
        assert response_body["success"] == success
        assert response_body["data"] == data
        assert response_body["errors"] == errors

    def test_success(self):
        response = Response()

        data = {faker.random_letter(): faker.random_digit()}

        response_body, returned_response_code = response.success(data)
        assert returned_response_code == 200
        assert response_body["success"] == True
        assert response_body["data"] == data
        assert "errors" not in response_body

    def test_errors(self):
        response = Response()

        errors = {faker.random_letter(): faker.random_digit()}

        response_body, returned_response_code = response.errors(errors)
        assert returned_response_code == 200
        assert response_body["success"] == False
        assert response_body["errors"] == errors
        assert "data" not in response_body

        response_body, returned_response_code = response.errors(errors, 400)
        assert returned_response_code == 400
