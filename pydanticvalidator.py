from pydantic import BaseModel, validator

class Computer(BaseModel):
    brand: str
    storage_type: str
    ratings: list[int]

    @validator("storage_type")
    #@classmethod  # Optional, but your linter may like it.
    def check_storage_type(cls, value):
        if value not in ("SSD", "HDD"):
            raise ValueError("Storage type can only be SSD or HDD.")
        return value
    

c1 = Computer(brand="soorya",storage_type="soorya",ratings=[1,2])    

"""
output:
(myenv) PS C:\FASTAPI_NONDB> python .\pydanticvalidator.py 
Traceback (most recent call last):
  File "C:\FASTAPI_NONDB\pydanticvalidator.py", line 16, in <module>     
    c1 = Computer(brand="soorya",storage_type="soorya",ratings=[1,2])    
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__ 
pydantic.error_wrappers.ValidationError: 1 validation error for Computer 
storage_type
  Storage type can only be SSD or HDD. (type=value_error)
(myenv) PS C:\FASTAPI_NONDB> 
"""