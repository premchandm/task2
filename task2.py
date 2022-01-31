import requests
import json

def get_value(object,k):
    for key, value in object.items():
        if type(value) is dict:
            get_value(value,k)
            if key == k:
                print (value)
        else:
            if key == k:
                print (value)


r = requests.get("http://169.254.169.254/latest/meta-data/")
r = r.json()
print(json.dumps(r,indent=2))
key = input("Enter Key: ")
get_value(r,key)

#For testing the request can be replaced with ("http://headers.jsontest.com")
