from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length = 30, title='name of patient', description='name of patient should be less than 30 characters', examples=['yashkumar', 'bigBoss'])]
    email: EmailStr
    age:int = Field(gt=0, lt=120)
    linkedin_url: AnyUrl
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='True if u r married else False', examples=['True', 'False'])]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Optional[Dict[str, str]] = None

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data Inserted')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data Updated')
    
patient_info = {'name': 'yashkumar', 'email': 'xp@gmail.com', 'age': 30, 'linkedin_url': 'https://www.linkedin.com/feed/', 'weight': 64.59,'allergies': ['sugar', 'dust', 'oil']}
patient1 = Patient(**patient_info)

update_patient_data(patient1)
