from pydantic import BaseModel

class Medical(BaseModel):
    age: int
    bmi: float
    children: int
    sex_female: int
    sex_male: int
    smoker_no: int
    smoker_yes: int
    region_northeast: int
    region_northwest: int
    region_southeast: int
    region_southwest: int
