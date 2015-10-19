import pytest




def divide(a,b): 
    return a/b

def test_divide(): 
    assert divide (2,2) == 1
    #pytest.mark.xfail (divide (4,2) == 3) 
    with pytest.raises(ZeroDivisionError):
        divide(2,1)

#    try:
#        divide(2,0)
#        assert False
#    except ZeroDivisionError:
#        assert True 
    #assertRaises ( ZeroDivisionError, "divide(2,0)")
    #raises(ZeroDivisionError, "divide(2,0)") 


