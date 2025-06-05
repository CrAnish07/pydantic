from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):
    name: str
    email: EmailStr
    age: int
    linkedin_url: Optional[AnyUrl] = None
    skills: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 20 < value < 60:
            return value
        else:
            return ValueError('Age should be between 20 and 60')

def update_employee_data(employee: Employee):

    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.skills)
    print('updated')

employee_info = {'name':'anish', 'email':'abc@hdfc.com', 'age': '30', 'linkedin_url':'http://linkedin.com/1322','contact_details':{'phone':'2353462'}}

employee1 = Employee(**employee_info)

update_employee_data(employee1)