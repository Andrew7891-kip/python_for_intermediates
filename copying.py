import copy

# shallow copy
# interferes the original
org = [[0,1,2,3],[5,6,7,8]]
cpy=copy.copy(org)

cpy[0][1]=9
print(cpy)
print(org)

# shallow func copy

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Student('Andrew',19)
p2 = copy.copy(p1)

p2.age=20

print(p1.age)
print(p2.age)

# deep copy
# not interfere the original 
orgy = [[0,1,2,3],[5,6,7,8]]
cpyi=copy.deepcopy(orgy)

cpyi[0][1]=9
print(cpyi)
print(orgy)

# deep copy func
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.employee=employee


p1=Student('Andrew',19)
p2 = copy.copy(p1)

p2.age=20

# shallow copy
company=Company(p1,p2)

# deep copy
company_clone=copy.deepcopy(company)

company_clone.boss.age=50
print(company_clone.boss.age)
print(company.boss.age)





