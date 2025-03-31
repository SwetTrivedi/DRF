import requests
import json


# this is de-serialzation code

# URL="http://127.0.0.1:8000/stucreate/"

# data={'name':'Ram','roll':101,'city':'Kanpur'}
# json_data=json.dumps(data)
# r=requests.post(url=URL,data=json_data)
# data=r.json()
# print(data)



URL="http://127.0.0.1:8000/stuupdate/"
# URL="http://127.0.0.1:8000/stuupdate/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL , data=json_data)
    data=r.json()
    print(data)

# get_data(3)

def post_data():
    data={
        'name':'baj',
        'roll':106,
        'city':'Dellhi'
    }     
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
post_data()


def update_data():
    data={
        'id':4,
        'name':'Ravi',
        'city':'Kanpur nagar'
    }     
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={
        'id':2
    }     
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
# delete_data()