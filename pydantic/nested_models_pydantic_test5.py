from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pin: str
    
class Patient(BaseModel):
    name: str
    gender: str
    age: int = 35
    address: Address
    
address_dict = {'city': 'Amdavad', 'state': 'Gujarat', 'pin': '380001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'yashkumar', 'gender': 'male', 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) #include and exclude/exclude-unset
print(temp)
print(type(temp))
