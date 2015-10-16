import pytest 

#
#def pytest_generate_tests(metafunc):
#    params = [("input", "output")]
#    metafunc.parametrize(("test_case", "result"), params)
#


def pytest_generate_tests(metafunc):
    argnames = ["str"]
    argvalues = [["\n\tHello"], ["\n\tWorld"]]
    print "\n\tEntered pytest_generate_tests"
    metafunc.parametrize("str", ["Hello","World"] )

print "\nat the start"

def test_sample(str):
    print str




