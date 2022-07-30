import pytest


@pytest.fixture(scope="class")    # executado apenas na classe, no inicio e fim
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Doctor", "Who", "tardis.org"]

@pytest.fixture(params=[("chrome","Doctor","Who"),("Firefox","Rose"),("IE","Dona")])
def crossBrowser(request):
    return request.param