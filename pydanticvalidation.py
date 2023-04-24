from pydantic import BaseModel

class Computer(BaseModel):
    brand: str
    storage_type: str
    ratings: list[int]

# The input is valid for the model.
computer = Computer(brand="Apple", storage_type="SSD", ratings=["5", "3", "4"])
# The below input is invalid for the model
print(computer.dict())
computer1 = Computer(brand='Apple', storage_type="SSD", ratings=['Good', 'Bad'])
print(computer1.dict())

"""
output:
Traceback (most recent call last):
  File "C:\FASTAPI_NONDB\pydanticvali.py", line 11, in <module>
    computer1 = Computer(brand='Apple', storage_type="SSD", ratings=['Good', 'Bad'])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 2 validation errors for Computer
ratings -> 0
  value is not a valid integer (type=type_error.integer)
ratings -> 1
  value is not a valid integer (type=type_error.integer)
(myenv) PS C:\FASTAPI_NONDB> 
"""

"""
input : computer = Computer(brand="Apple", storage_type="SSD", ratings=["5", "3d", "4"])
output:
 File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Computer
ratings -> 0
  value is not a valid integer (type=type_error.integer)
(myenv) PS C:\FASTAPI_NONDB> python .\pydanticvalidation.py
Traceback (most recent call last):
  File "C:\FASTAPI_NONDB\pydanticvalidation.py", line 9, in <module>
    computer = Computer(brand="Apple", storage_type="SSD", ratings=["5", "3d", "4"])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pydantic\main.py", line 341, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Computer
ratings -> 1
  value is not a valid integer (type=type_error.integer)
"""