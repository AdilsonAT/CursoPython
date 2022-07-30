# Any pytest file should start with test_ or end _test
# pytest methods names should with test
#  run -> edit configurations -> Phyton tests
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution
# -s logs in output
# -v stands for more info metadata
# you can run specific file with py.test <filename>
# -m you can mark (tag) tests and then run with -m
# you can skip test with @pytest.mark.skip
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize fixtures
#   and make it avaliable to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class in initiate and at the end
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test -v  # mais informações
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test -v -s   # mostra prints do pgm
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test test_demo2.py -v -s # executar um arquivo do pacote
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test -k CreditCard -v -s # executar os testes que tenham no nome CreditCard
# PS C:\Users\004696631\PycharmProjects\cursoPython\pytestDemo> py.test -m smoke -v -s  # executar os marcados

import pytest

def test_firstProgram(setup):
    print("Hello")

# def test_firstProgram():
#     print("Good Morning")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)