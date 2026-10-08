                                ###POST METHOD###
# from email.policy import default
from fastapi import FastAPI, Path, HTTPException, Query
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, List, Dict, Optional, Literal

import pydantic
app = FastAPI()

#pydanticModel
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the Patient', examples=['P001'])]
    name: Annotated[str, Field(..., max_length=30, description='Name of the Patient', examples=['yashkumar'])]
    city: Annotated[str, Field(..., description='City of the Patient', examples=['New York'])]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the Patient', examples=[35])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the Patient', examples=['male'])]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in meters', examples=[1.75])]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in KGs', examples=[70.0])]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'OverWeight'
        else: 
            return 'Obese'
        
class PatientUpdate(BaseModel):
    
    #ID as path parameter
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male','female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
    
    
    
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
        
            ###GET METHOD INITIATE:--->>>>
            
@app.get("/")
def hello():
    return{'message': 'Hello, World'}

@app.get("/about")
def about():
    return{'message': 'You are the next billionaire, keep going!'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='ID of the Patient', examples=['P001'])):
    data = load_data() #load all patients data
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail= 'patient not found')    

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description = 'sort on the basis of height, weight, bmi') , order: str = Query('asc', description = 'sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail="invalid field, select from {valid_fields}")
    if order not in ['asc','desc']:
        raise HTTPException(status_code= 400, detail="invalid order, select from asc or desc")
         
    #HTTPException coe:400=bad request
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)
    return sorted_data
    
                #POST METHOD INITIATE:--->>>>
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()  #load existing data
        
    if patient.id in data: #Check  if the patient already exists - > raise error
        raise HTTPException(status_code=400, detail = 'patient already exists')
        
    data[patient.id] = patient.model_dump(exclude = ['id']) #Add new patient to DB
        
        #Save in json file
    save_data(data)
        
    return JSONResponse(status_code=201, content = {'message': "Patient succesfully created"})
 
@app.put("/edit/{patient_id}")

def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data() #Load Data 1st
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not exist.')
    
    existing_patient_info = data[patient_id]  #Extract existing Patient's data
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True) #make dict of Patient_update
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
        
    # existing_patient_info -> pydantic object -> updated bmi + verdict
    # -> pydantic pbjevt -> dict
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    existing_patient_info = patient_pydantic_obj.model_dump(exclude={'id'})
    data[patient_id] = existing_patient_info #Add to dict
    #save data
    save_data(data)
    return JSONResponse(status_code=200, content={'message': 'patient updated!'})
    
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data() #Load Data 1st
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found.')
    
    del data[patient_id]
    
    save_data(data)
    return JSONResponse(status_code=200, content={'message': 'patient deleted!'})
    
    
    
    
    #stop at 26:06 (video)
        
        
        
        
