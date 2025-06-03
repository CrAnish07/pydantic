from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Employee(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Anish', 'Ankush'])]
    age: int = Field(gt=20, lt=60)
    email: EmailStr
    linkedin_url: AnyUrl
    salary: int
    skills: Annotated[List[str], Field(default=None, max_length=5)]
    experiences: Optional[List[str]] = None
    contact_details: Dict[str, str]

def update_employee_data(employee: Employee):
    print(employee.id)
    print(employee.name)
    print(employee.age)
    print(employee.email)
    print(employee.linkedin_url)
    print(employee.salary)
    print(employee.skills)
    print(employee.experiences)
    print(employee.contact_details)
    print("Updated")

employee1_info = {'id': '111', 'name': 'Anish', 'email': 'abc@gmail.com', 'linkedin_url': 'http://linkedin.com/1337x', 'age': 22, 'salary': 40000, 'married': True, 'skills': ['C++', 'Rust', 'System Design', 'Docker', 'Kubernetes'], 'contact_details': {'phone': '12996591'}}

Employee1 = Employee(**employee1_info)

update_employee_data(Employee1)