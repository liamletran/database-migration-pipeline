from app import test_hello, more_1


def more_test_hello():
    assert test_hello() == "Hello, World!"


def test_more():
    assert more_1() == 1
