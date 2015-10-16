import pytest 


@pytest.fixture()
def startup(request):
    print "\ninside startup "
    def fin():
       print ("\nfinishing startup")
    request.addfinalizer(fin) 
    return None


@pytest.mark.usefixtures("startup") 
def test_1():
    print ("\n\t inside test1")

def test_2(startup):
    print ("\n\t inside test2")

def test_3(startup):
    print ("\n\t inside test3")


@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.mark.xfail(("6*9", 42)),
    ("3+4", 7),
])


@pytest.mark.usefixtures("startup") 
def test_eval(input,expected):
    assert eval(input) == expected





