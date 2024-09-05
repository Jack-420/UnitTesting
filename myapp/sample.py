import json

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

def valid_age(age):
    if age<0:
        raise ValueError("Age cannot be less than 0")
    
def save_dict(_dict, filepath):
    json.dump(_dict,open(filepath,'w'))
    print("saved")
    
class Student:
    
    def __init__(self,name,age,credit):
        self.name=name
        self.age=age
        self.credit=credit
        
    def get_age(self):
        return self.age 
    
    def get_credit(self):
        return self.credit
    
    def set_credit(self,value):
        self.credit=value