from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):

    name: str
    email: EmailStr
    age: int
    salary: int
    linkedin_url: AnyUrl
    skills: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_salary_base_skills(cls, model):
        if model.salary > 50000 and 'System Design' not in model.skills:
            raise ValueError('Employee should know about System Design')
        return model

def update_employee_data(employee: Employee):

    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.skills)
    print('updated')

employee_info = {'name':'nitish', 'email':'abc@hdfc.com', 'age': '65', 'salary': 60000, 'linkedin_url':'http://linkedin.com/1322', 'skills': ['C++', 'Rust', 'System Design', 'Docker', 'Kubernetes'], 'contact_details':{'phone':'2353462'}}

employee1 = Employee(**employee_info)

update_employee_data(employee1)