import pytest 
import yaml 
#
## content of test_example.py
#def pytest_generate_tests(metafunc):
#    #metafunc.parametrize("number", ["1","2","3","5","10"])
#    for fixture in metafunc.fixturenames:
#        metafunc.parametrize(fixture , range(10))
#
#def test_func(number):
#    assert number < 8
#
#def pytest_generate_tests(metafunc):
#    for fixture in metafunc.fixturenames:
#        if 'number1' in metafunc.fixturenames:
#            metafunc.parametrize('number1' , [1,3,5]) 
#        if 'number2' in metafunc.fixturenames:
#            metafunc.parametrize('number2' , [2,4,6]) 
#
##
def pytest_generate_tests(metafunc):
    dataMap = yaml.load('data.yaml')
    print yaml.dump(dataMap) 
    #metafunc.parametrize((fixture) , [1,3,5,2,4,6]) 


def test_func(number1):
    print str(number1) +"\t-\t"+ str(number2)
    assert number1 < number2

def test_func2(number2):
    print str(number1) +"\t-\t"+ str(number2)
    assert number1 < number2





#
#        my $testcase_description_file  = YAML::LoadFile("$jenkins_workspace_dir/info/$testtype/$testcase");
#
#        print "\n YAML file : $jenkins_workspace_dir/info/$testtype/$testcase \n";
#
#        my $testcase_status_from_doc = $testcase_description_file->{status};
#        my $testcase_name_from_doc = $testcase_description_file->{name};
#        my $testcase_desc_from_doc = $testcase_description_file->{description};
#
#
##test.mark.parametrize(("input", "expected"), [
#    ("3+5", 8),
#    ("2+4", 6),
#    ("6*9", 42),
#])
#


#@pytest.mark.parametrize("numb", range(10))
#def test_f(numb):
#    assert numb < 9
##
#

#    if "number" in metafunc.fixturenames:

#fixturenames
#    if "number" in metafunc.funcargnames:
#
#def pytest_generate_tests(metafunc):
#    argnames = ["str"]
#    argvalues = [["\n\tHello"], ["\n\tWorld"]]
#    print "\n\tEntered pytest_generate_tests"
#    metafunc.parametrize("str", ["Hello","World"] )
#
#print "\nat the start"
#
#def test_sample(str):
#    print str
#



#     metafunc.parametrize("str", ["Hello","World"] )
