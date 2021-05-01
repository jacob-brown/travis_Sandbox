import pytest
import helloWorld


def test_helloWorld():
    assert helloWorld.helloWorld() == "hello world"