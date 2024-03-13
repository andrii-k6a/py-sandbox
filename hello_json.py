import json


def simple_json():
    person_json = '''{
        "name": "Henry",
        "dob": {
            "month": "June",
            "year": 1999
        },
        "hobbies": [
            "football",
            "science"
        ]
    }'''

    person = json.loads(person_json)
    print(type(person))  # it's a dictionary
    print(person)
    print('Name:', person["name"])
    print('Year of birth:', person["dob"]["year"])
    print('Hobbies:', person["hobbies"])
    print('Hobbies type :', type(person["hobbies"]))  # it's a list


def list_json():
    users_list_json = '''[
        {
            "id": "001",
            "nickname": "zero"
        },
        {
            "id": "010",
            "nickname": "cookie"
        },
        {
            "id": "100",
            "nickname": "foo"
        }
    ]'''
    users = json.loads(users_list_json)
    print(users)
    print(type(users))  # it's a list

    for user in users:
        print('*** USER ID:', user['id'], '***')
        print(user)
        print(type(user))

