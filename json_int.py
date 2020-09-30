import json


student= {'name':'andrew','class':4,'isbig':False,'employed':True}

# converting python to json
s_json= json.dumps(student,indent=4 ,sort_keys=True)
print(s_json)


# placing to json file
try:
    print('attempt....')
    with open ('students.json' ,'w') as file:
        json.dump(student,file)
    print('done')
    student= json.loads(s_json)
    print(student)
except:
    print('error!....')
    raise TypeError

# class 
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User('Andrew',20)

def encode(o):
    if isinstance(o,User):
        return {'name':o.name , 'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('not json serializable')

def decode(dct):
    if User.__name__ is dct:
        return User(name=dct['name'],age=dct['age'])
    return dct


j_user = json.dumps(user, default=encode)
print(j_user)

user_=json.loads(j_user,object_hook=decode)
print(user_)