# setup function will run every test function
# setup module will only run once

# def setup_function(function):
#     print("Launch browser")
#
# def teardown_function(function):
#     print("Close browser")

def setup_module(module):
    print("Launch browser")


def teardown_module(module):
    print("Close browser")


def test_one():
    print("Test one executed")


def test_two():
    print("Test two executed")


def test_three():
    print("Test three executed")


def test_four():
    print("Test four executed")


def test_five():
    print("Test five executed")


def test_six():
    print("Test six executed")

