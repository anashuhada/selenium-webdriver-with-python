import pytest

# scope="function" - follows as by default
# scope="session" - only executed once
@pytest.fixture(autouse=True, scope="session")
def setup_and_teardown():
    print("Launch browser")
    print("Open application url in browser")
    yield # separate setup and teardown
    print("Logout from application")
    print("Close browser")