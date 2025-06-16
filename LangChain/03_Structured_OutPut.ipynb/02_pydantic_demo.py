from pydantic import BaseModel,Field,EmailStr
from typing import  Optional

class Student(BaseModel):
    age:Optional[int]
    email:EmailStr

    # cgpa i want in specific range 
    cgpa:float=Field(gt=0,le=10,default=5,
                     description="A decimal value representing the cgpa of student"
                     )
    Gender:str=Field(...,description="It represent the Gender",examples=['male','female'])


newstd= Student(age=10,email='mahaleankit12@gmail.com',cgpa=8,Gender='male')
print(newstd)

res = newstd.model_dump_json()
print(res)

