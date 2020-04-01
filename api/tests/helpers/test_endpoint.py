from helpers.endpoint import require_values


class TestEndpointHelpers:
    def test_require_values(self):
        data_obj = {"a": 1, "b": 2, "c": 3}
        required_fields = ["a", "d"]
        missing_fields = require_values(data_obj, required_fields)
        assert missing_fields == ["d"]
        missing_fields = require_values(data_obj, ["a"])
        assert missing_fields == []
