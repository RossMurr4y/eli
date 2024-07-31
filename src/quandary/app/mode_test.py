import pytest
from .mode import ModeInterface
from .response import ResponseInterface


class TestResponse(ResponseInterface):
    value = "This is a test response."


class TestMode(ModeInterface):
    question = "How many sides does a square have?"

    def __init__(self):
        pass

    def run(self) -> ResponseInterface:
        return TestResponse()


def test_one():
    assert issubclass(TestMode, ModeInterface)


def test_two():
    i = TestMode()
    assert isinstance(i, ModeInterface)


def test_three():
    """.run returns an Response Interface"""
    assert isinstance(TestMode().run(), ResponseInterface)
