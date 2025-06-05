from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Employee(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city': 'Kolkata', 'state': 'West Bengal', 'pin': '700045'}
address1 = Address(**address_dict)

employee_dict = {'name': 'Anish', 'gender': 'male', 'age': 22, 'address': address1}
employee1 = Employee(**employee_dict)

print(employee1)