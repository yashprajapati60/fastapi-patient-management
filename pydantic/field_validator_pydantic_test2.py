from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

#Pydantic Model Initiate
class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    # linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    
    def email_validator(cls, value):
        valid_domain = ['hdfc.com', 'icici.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError('Not a Valid Domain.')
        
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
        
    @field_validator('age', mode = 'after') #default mode value is AFTER
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age should be in between 0 to 100')
            

#Pydantic Model Ends

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data Inserted')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data Updated')
    
patient_info = {'name': 'yashkumar', 'email': 'xp1@icici.com', 'age': '30', 'weight': 64.59, 'married': True,'allergies': ['sugar', 'dust'], 'contact_details': {'mono': '9988554444'}}

patient1 = Patient(**patient_info) #validation #type correction

update_patient_data(patient1)
