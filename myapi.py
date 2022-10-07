from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

class Item(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: float
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


@app.get("/")
def read_root():
    return {"Calcula possibilidade do paciente ter diabetes"}


@app.post("/calc/")
async def calc_pacient(item: Item):
    with open('./content/model.pkl', 'rb') as f:
        data = pickle.load(f)
        df = pd.DataFrame(columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"])

        df = df.append({"Pregnancies" : item.Pregnancies, "Glucose" :item.Glucose, "BloodPressure" :item.BloodPressure, "SkinThickness" :item.SkinThickness, 
            "Insulin" :item.Insulin, "BMI" :item.BMI, "DiabetesPedigreeFunction" :item.DiabetesPedigreeFunction, "Age" :item.Age}, ignore_index=True)
        x = data.predict(df)      
    return {"Resultado_Diabetes" : bool(x)}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

