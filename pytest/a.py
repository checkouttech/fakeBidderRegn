import requests

response = requests.get(
        "http://192.168.150.110:10001/hello/kapil"
    )

print response.status_code 
#print response.json()["status"] 
print response.text
#print response.json()
#print response.encoding 
print response 
