import pytest


@pytest.mark.parametrize("username, password", [("Ana", "12345"), ("Johnny", "54321"), ("David", "32154")])
def test_sample_file_two(username, password):
    # print("Inside sample file two")
    print(username + "-" + password)
