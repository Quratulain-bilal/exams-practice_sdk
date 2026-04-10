📘 AgentOutputSchema Guide 


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


methods

1) is_plain_text()

Kya karta hai

Bataata hai ke output plain text (simple string) expect ho raha hai ya nahi.


Return value

True agar output_type is None ya output_type is str.

False warna.


Jab use hota hai

Jab code ko decide karna ho ke json_schema() call karein ya nahi.

Agar is_plain_text() True ho to json_schema() nahi banaya jayega (aur agar call karoge to UserError aaega).


Example (code)

s1 = AgentOutputSchema(str)
print(s1.is_plain_text())  # True

s2 = AgentOutputSchema(int)
print(s2.is_plain_text())  # False

Common pitfall / error

Agar is_plain_text() True hai lekin tum json_schema() call karte ho → UserError.
Fix: agar text chahiye to json_schema() na call karo; seedha validate_json('"hello"') call karo.



---

2) name()

Kya karta hai

output_type ka readable naam return karta hai (simple string).

Generic types ko bhi accha format me dikhata hai, jaise list[int], dict[str, int].


Return value

e.g. "int", "str", "list[int]", "dict[str,int]", "Person" (agar BaseModel ya class ho).


Example (code)

print(AgentOutputSchema(int).name())            # "int"
print(AgentOutputSchema(list[int]).name())     # "list[int]"
print(AgentOutputSchema(dict[str,int]).name()) # "dict[str,int]"

Usefulness

Logging/debugging ke liye best — jab error messages me type dikhana ho.



---

3) json_schema()

Kya karta hai

Agar output plain text nahi (i.e. is_plain_text() False) to JSON Schema object return karta hai jo AI ko/validate ko batata hai expected structure kya hai.


Return value

Python dict jo JSON Schema represent karta hai (_output_schema).


Important rule / error

Agar is_plain_text() True (i.e. output_type str ya None), to json_schema() UserError raise karega: "Output type is plain text, so no JSON schema is available".


Example (code)

s = AgentOutputSchema(dict[str,int])  
schema = s.json_schema()
# schema ek dict hogi, e.g. {"type":"object", "additionalProperties": {"type":"integer"}}

Kaha faida

Jab tum model ko structured output dena chahte ho, to json_schema() ko prompt me ya validation me use kar ke model se expected structure seedha enforce kar sakte ho.


Common pitfall / fix

Agar tum AgentOutputSchema(str) banaya aur json_schema() call kiya → UserError. Fix: agar sirf text chahiye to is_plain_text() check karo; json_schema() sirf object/array types ke liye use karo.



---

4) is_strict_json_schema()

Kya karta hai

Batata hai ke constructor me strict_json_schema True set hua tha ya nahi.


Return value

True ya False (default True in provided code).


Effect (kya hota hai agar True)

Constructor ensure_strict_json_schema(self._output_schema) call karta hai — agar schema strict rules pe fit nahi hota to UserError throw hota at init time (pehle hi).

Strict mode ka matlab: schema zyada constrained aur predictable hota hai (less ambiguity), lekin kuch Python types strict schema me convert nahi hote aur error aayega.


Example

s = AgentOutputSchema(int)
print(s.is_strict_json_schema())  # True by default

Fixes agar strict fail kare

AgentOutputSchema(MyType, strict_json_schema=False) pass karo.

Ya apna type BaseModel (Pydantic) bana lo jisse strict schema easily banta hai.



---

5) validate_json(json_str: str) -> Any

Ye sabse important method hai — step by step samjho.

Kya karta hai (story)

1. Pehle input json_str ko parse karta hai (JSON text → Python object). Ye parsing _json.validate_json ke through hoti hai using the TypeAdapter (pydantic).


2. Fir TypeAdapter se validation karta hai: parsed value expected type ke mutabiq hai ya nahi.


3. Agar self._is_wrapped True hai:

Pehle check karega: validated object dict hai ya nahi.

Agar dict nahi → ModelBehaviorError (expected dict but got something else).

Agar dict hai to check karega ke key _WRAPPER_DICT_KEY (jo "response") dict ke andar maujood hai ya nahi.

Agar "response" missing ho → ModelBehaviorError (Could not find key "response").

Agar sab theek ho → return karega validated["response"] (i.e. wrapped value).



4. Agar self._is_wrapped False → validated object directly return karega.



Return value

Validated Python value (type depends on output_type): e.g., int, list, dict, BaseModel object, etc.


Exceptions (kab kya raise hota)

ModelBehaviorError:

When _is_wrapped=True but parsed value is not a dict.

When _is_wrapped=True but "response" key missing.

When TypeAdapter validation fails (value type mismatch).


UserError:

Mostly from constructor or when calling json_schema() for plain text. (Not usually from validate_json unless constructor earlier failed.)



Detailed Examples (practical — copy/paste style)

Example A — int (wrapped)

schema = AgentOutputSchema(int)   # _is_wrapped = True
# Correct usage:
schema.validate_json('{"response": 5}')   # returns 5

# Wrong usage:
schema.validate_json('5')
# -> ModelBehaviorError: Expected a dict, got <class 'int'> for JSON: 5
# Fix: either pass wrapped JSON, or set strict_json_schema=False and handle parsing differently.

Example B — str (plain text)

schema = AgentOutputSchema(str)  # _is_wrapped = False
schema.validate_json('"hello"')  # returns "hello"

# Wrong:
schema.validate_json('{"response":"hello"}')
# -> TypeAdapter may reject (expected str but got dict) -> ModelBehaviorError
# Fix: send plain string if output_type is str.

Example C — list[int] (per code: wrapped)

schema = AgentOutputSchema(list[int])  # _is_wrapped = True (list top-level)
schema.validate_json('{"response":[1,2,3]}')  # returns [1,2,3]

# If AI returns plain array: [1,2,3]
schema.validate_json('[1,2,3]')
# -> ModelBehaviorError: Expected a dict, got <class 'list'> for JSON: [1,2,3]
# Fix: ask AI to return {"response": [1,2,3]} or change output_type to dict/list handling.

Example D — dict[str,int] (no wrap)

schema = AgentOutputSchema(dict[str,int])  # _is_wrapped = False
schema.validate_json('{"a":1,"b":2}')  # returns {"a":1,"b":2}

# Wrong:
schema.validate_json('{"response":{"a":1}}')
# -> TypeAdapter might reject (expected dict[str,int] but got dict with key 'response')
# Fix: AI should produce top-level dict keys that match schema.

Example E — BaseModel

class Person(BaseModel):
    name: str
    age: int

schema = AgentOutputSchema(Person)  # _is_wrapped = False

schema.validate_json('{"name":"Ali","age":20}')
# returns validated dict or pydantic object depending on adapter; safe

schema.validate_json('{"name":"Ali"}')
# -> ModelBehaviorError or UserError depending on strictness (missing required field)

Parse vs Validate (seedha)

Parse: JSON string ko Python object me convert karna ('{"a":1}' -> {"a":1}).

Validate: Jo parsed object aya use check karna ke kya woh expected type/shape follow karta hai.


validate_json() dono karta hai: parse + validate.


---

Extra: Real-life "If / Then" (bohot clear)

If tumne AgentOutputSchema(int) use kia then AI must return {"response": 5}; agar AI ne 5 diya → ModelBehaviorError.

If tumne AgentOutputSchema(str) use kia then AI must return "text" not {"response":"text"}.

If tumne AgentOutputSchema(dict[str,int]) use kia then AI must return {"k":1} not {"response":{"k":1}}.

If tumne AgentOutputSchema(list[BaseModel]) use kia → code will wrap because top-level is list → expect {"response":[{...},{...}]}.



---

Fixes / Recommendations (taareeqe jo aam tor pe use karo)

1. Complex structured outputs → use pydantic.BaseModel. (No wrap, strict friendly.)


2. If model returns primitives or arrays and SDK expects wrapper → instruct model to return {"response": ...} exactly. (In prompt give schema or examples.)


3. If constructor throws UserError about strict schema → either convert your type to BaseModel or use strict_json_schema=False.


4. Always test with schema.validate_json(sample_json_string) to see exactly kya expected hai aur kya error aata hai.




---

Final quick cheat-sheet (1-line per method)

is_plain_text() → True agar output type str/None. Use: decide whether to call json_schema().

name() → readable name of type (logging).

json_schema() → returns JSON Schema (raises UserError if plain text).

is_strict_json_schema() → tells if strict mode on (default True).

validate_json(json_str) → parse + validate; if _is_wrapped True expect {"response": ...}, else expect direct structure; raises ModelBehaviorError on mismatch.





