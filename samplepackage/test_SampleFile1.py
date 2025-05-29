import pytest


@pytest.mark.smoke
def test_sample_one():
    a = 5
    b = 10
    assert a == b, "a is not equal to b"


@pytest.mark.xfail
def test_sample_two():
    a = 7
    b = 3
    assert a > b


@pytest.mark.xfail
def test_sample_three():
    a = "Ana"
    b = "Shuhada"
    assert a.__eq__(b)


@pytest.mark.regression
def test_sample_four():
    print("Inside test sample four")
