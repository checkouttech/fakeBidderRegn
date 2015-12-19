import pytest
import requests

def test_get_request():
    response = requests.get(
        "http://192.168.150.110:10001/hello/kapil"
    )
    assert response.status_code == 200
    assert response.text == "<b>Hello kapil!</b>"



def test_post_request():
    response = requests.post(
        "http://192.168.150.110:10001/fakebidder/",

        data={"accept_language":"en-us,en;q=0.5","auction_id":"e59cf7f965e5634770bec77b8e234e8447da8992","country":"ca","domain_name":"www.bender-testing.com","ip_address":"137.122.14.11","page_url":"","secure":0,"network_user_id":"bid=3.02^robot_tracking=8498431437585754.94","xff":"209.232.44.21","region":"on","user_id":"9c051f73a0b28f3130fcedf6372f75c90f3a89cc","publisher_id":99999,"site_id":42,"designated_site_url":"www.bender-testing.com","user_agent":"python-requests/2.2.1 CPython/2.7.5 Linux/2.6.18-308.13.1.el5","denied_ad_types":[14001,14004,14006,14007,14008,14009,14010,14011,14012,14013,14020,14021,14022,14002,14003,14005,14014,14015,14016,14017,14018,14019],"render_status":"js","site_size_session_count":1,"user_tz":-400,"page_position":"unknown","expandable":0,"supported_tech":[],"private":0,"preferred_seats":["r1"],"pmp":{"deals":[{"id":"TA-99999-r1","floor":0.20000000298023224,"seats":["r1"],"type":2}]},"device":{"os":"25043","dclass":40,"carrier":"Other"},"ad_size_id":1,"ad_width_px":468,"ad_height_px":60,"alt_ads":[],"instl":0}, 

        headers={'Content-Type':'application/json' , 
                 'cookie': 'returnBidAmount=5.2345' }
    )
    print response
    assert response.status_code == 200
    #assert response.text == "foo" 
    #assert response.json()["price"] == 5.5 

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass


@pytest.fixture()
def before():
    print('\nbefore each test')

    def fin():
        print('\n[teardown] cheese_db finalizer, disconnect from db')
    #self.addfinalizer(fin)
    # how to add finalizer 
    return None

@pytest.mark.parametrize(("input", "expected"), [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])




@pytest.mark.usefixtures("before") 
def test_eval(input, expected):
    assert eval(input) == expected

# to add a finalizer 
def fin():
    print ("teardown smtp")
    smtp.close()
    request.addfinalizer(fin)

#print response.status_code
#print response.json()["status"]
#print response.text


# http://192.168.150.110:10001/hello/kapil

# content of test_sample.py
#def func(x):
#    return x + 1

#def test_answer():
#    assert func(3) == 5

# 
#    skipif - skip a test function if a certain condition is met
#    xfail - produce an “expected failure” outcome if a certain condition is met
#    parametrize to perform multiple calls to the same test function.


# curl -v --header 'Content-Type:application/json' -X POST --data '{"accept_language":"en-us,en;q=0.5","auction_id":"e59cf7f965e5634770bec77b8e234e8447da8992","country":"ca","domain_name":"www.bender-testing.com","ip_address":"137.122.14.11","page_url":"","secure":0,"network_user_id":"bid=3.02^robot_tracking=8498431437585754.94","xff":"209.232.44.21","region":"on","user_id":"9c051f73a0b28f3130fcedf6372f75c90f3a89cc","publisher_id":99999,"site_id":42,"designated_site_url":"www.bender-testing.com","user_agent":"python-requests/2.2.1 CPython/2.7.5 Linux/2.6.18-308.13.1.el5","denied_ad_types":[14001,14004,14006,14007,14008,14009,14010,14011,14012,14013,14020,14021,14022,14002,14003,14005,14014,14015,14016,14017,14018,14019],"render_status":"js","site_size_session_count":1,"user_tz":-400,"page_position":"unknown","expandable":0,"supported_tech":[],"private":0,"preferred_seats":["r1"],"pmp":{"deals":[{"id":"TA-99999-r1","floor":0.20000000298023224,"seats":["r1"],"type":2}]},"device":{"os":"25043","dclass":40,"carrier":"Other"},"ad_size_id":1,"ad_width_px":468,"ad_height_px":60,"alt_ads":[],"instl":0}' http://192.168.150.110:10001/fakebidder/  --cookie "returnBidAmount=5.2345"
