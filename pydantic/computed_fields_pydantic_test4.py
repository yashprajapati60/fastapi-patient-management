from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field

from typing import List, Dict, Optional, Annotated

#Pydantic Model Initiate
class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round((self.weight) / (self.height**2),2)    
        return bmi
    # @model_validator(mode='after')
    # def validate_emergency_contact(cls, model):
    #     if model.age > 60 and 'emergency' not in model.contact_details:
    #         raise ValueError('Patient Older than 60 must have an Emergency contact')
    #     return model
    
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    # print(patient.linkedin_url)
    print(patient.weight)
    print(patient.height)
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
    print(patient.height)
    print('BMI', patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('data Updated')
    
patient_info = {'name': 'yashkumar', 'email': 'xp1@icici.com', 'age': 23, 'weight': 64.59, 'height': 1.82, 'married': True,'allergies': ['sugar', 'dust'], 'contact_details': {'emergency': '9988554444'}}

patient1 = Patient(**patient_info) #validation #type correction

update_patient_data(patient1)
