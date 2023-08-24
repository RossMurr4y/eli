import pytest

from .response import ResponseInterface

class TestResponse(ResponseInterface):
    value = "This is a mock response return type"

def test_one():
    assert issubclass(TestResponse, ResponseInterface)

def test_two():
    i = TestResponse()
    assert isinstance(i, ResponseInterface)