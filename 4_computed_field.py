from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: Optional[bool] = None
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

def update_employee_data(employee: Employee):

    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.allergies)
    print('BMI: ', employee.bmi)
    print('updated')

employee_info = {'name':'Anish', 'email':'abc@icici.com', 'age': '65', 'weight': 75.2, 'height': 1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

employee1 = Employee(**employee_info)

update_employee_data(employee1)