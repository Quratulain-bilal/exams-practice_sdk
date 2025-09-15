📘 AgentOutputSchema Guide (Step by Step)


---

1. Python Basics: Data Representation

Python me data 2 main tarah se hota hai:

Primitive types: int, str, bool, float

Structured types: dict, list, class


Example:

x = 5           # int
name = "Ali"    # str
items = [1,2,3] # list
person = {"age": 20, "city": "Lahore"}  # dict

👉 Dict me key-value hota hai, list me sirf values hoti hain (keys nahi hoti).


---

2. Pydantic (BaseModel) ka role

Pydantic ek library hai jo Python classes ko data validation aur parsing ke liye use hoti hai.

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

Agar sahi data do:


p = Person(name="Ali", age=20)
print(p.dict())  # {'name': 'Ali', 'age': 20}

Agar galat do:


p = Person(name="Ali", age="not_number")
# ❌ ValidationError throw hoga

👉 BaseModel me keys hamesha hoti hain, is liye yeh “wrap” nahi hota.


---

3. Dataclass vs BaseModel

Dataclass: Simple Python ka feature hai jo class ko “data holder” banata hai.

Pydantic BaseModel: Yeh validation aur type checking karta hai.


from dataclasses import dataclass

@dataclass
class PersonData:
    name: str
    age: int

Difference:

Dataclass → sirf data rakhta hai, validation nahi.

BaseModel → data + validation.


SDK ke context me:

Agar aap dataclass use karo, to SDK usko wrap karega under response (kyunki direct JSON schema nahi banta).

Agar BaseModel use karo, to wrap nahi hoga (kyunki already structured hai).



---

4. OpenAI SDK ka Scene

SDK me jab aap Agent banate ho, to usko batana padta hai ke output kis type ka hoga.
Iske liye use hota hai:

Simple Python type → int, str, bool

Complex Pydantic class → BaseModel

Ya AgentOutputSchema



---

5. Wrap hone ka Rule

Primitive types (int, str, bool, list[int]) → Wrap hote hain into {"response": ...} kyunki inki key nahi hoti.


Example:

output_type = int
# Model 5 return karega → SDK banayega {"response": 5}

Dict/BaseModel → Wrap nahi hota, kyunki inme already keys hoti hain.


Example:

class User(BaseModel):
    name: str
    age: int

output_type = User
# Model {"name":"Ali","age":20} return karega → no wrap

Dataclass → Wrap hota hai, kyunki SDK isko JSON schema me convert karne ke liye “response” ka ek layer dalta hai.



---

6. AgentOutputSchema: Kyu use karte hain?

Agar aapko zyaada control chahiye ke SDK output ko kaise parse kare, tab AgentOutputSchema use karte ho.
Yeh ek helper hai jo:

Validation lagata hai

Wrap/un-wrap handle karta hai

Nested data support karta hai


