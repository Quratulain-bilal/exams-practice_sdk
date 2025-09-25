

---

## 🔹 Background

`@function_tool` ka matlab hai aap ek Python function ko **Agent ke tool** ke taur pe expose kar rahe ho.
Problem yeh hoti hai ki kabhi kabhi **tool fail ho sakta hai** (jaise API down, galat input, ya aapke code mein bug).

Agar tool fail ho, to LLM ko kaise batana hai?
Isi liye `failure_error_function` option diya gaya hai.

---

## 🔹 3 Behaviors

1. **Default (kuch pass na karo)**
   Agar aap `@function_tool` simple use karte ho, aur tool crash hota hai, to ek **default error message** generate hota hai jo LLM ko diya jata hai (something like: `"An error occurred while running the tool."`).

2. **Custom error function pass karo**
   Agar aap khud ek function pass kar dete ho `failure_error_function=my_custom_error_function`, to aap control karte ho ki LLM ko kya reply mile.
   Example:

   ```python
   def my_custom_error_function(context: RunContextWrapper[Any], error: Exception) -> str:
       print(f"Error aaya: {error}")
       return "Internal server error. Try again later."
   ```

   Ab agar tool crash hota hai → yeh function chalega → aur LLM ko woh message milega jo aap return karte ho.

3. **Explicitly None pass karo**
   Agar aap `failure_error_function=None` kar dete ho, to **SDK error ko LLM ko hide nahi karega**.
   Instead, error **raise** ho jaayega aapke Python code me.

   * Agar model ne galat JSON bheja → `ModelBehaviorError`
   * Agar aapke code me bug tha → `UserError`

   Matlab: responsibility aapki hogi error catch karke handle karne ki.

---

## 🔹 Example 

```python
from agents import function_tool, RunContextWrapper
from typing import Any

# custom error function
def my_custom_error_function(context: RunContextWrapper[Any], error: Exception) -> str:
    print(f"A tool call failed: {error}")
    return "Sorry, something went wrong. Please try again later."

# tool banaya
@function_tool(failure_error_function=my_custom_error_function)
def get_user_profile(user_id: str) -> str:
    if user_id == "user_123":
        return "User profile for user_123 retrieved."
    else:
        # intentionally crash
        raise ValueError(f"No profile found for {user_id}")
```

### Case 1: Input = `"user_123"`

→ Output: `"User profile for user_123 retrieved."`

### Case 2: Input = `"user_999"`

→ Exception aayegi, lekin SDK LLM ko reply karega:
`"Sorry, something went wrong. Please try again later."`

---

## 🔹 Agar manually FunctionTool object banate ho

Us case me `on_invoke_tool` function likhna parta hai, aur usme error handling aapko khud karni padti hai.
Yani `try/except` laga kar error handle karna parta hai.

---

👉 Simple words me:

* `failure_error_function` ek **fallback system** hai jo decide karta hai tool crash hone pe **LLM ko kya message bhejna hai**.
* Agar aap kuch nahi karte → default message.
* Agar aap custom dete ho → aapka friendly message.
* Agar `None` dete ho → error upar raise hoga, LLM tak nahi jaayega.


# ❓ Question

Suppose tumne ek **triage agent** banaya hai jo 4 different agents ko tools ke taur pe use karta hai:

* `math_agent` (maths solve karta hai)
* `search_agent` (web search karta hai)
* `translate_agent` (translation karta hai)
* `summary_agent` (text summarization karta hai)

Agar user ek request bhejta hai aur LLM decide karta hai ke `translate_agent` ko call karna hai,
**lekin `translate_agent` tool crash ho jata hai** (jaise invalid arguments ya API error), aur LLM ke instruction me alternative likha ho:

> "If translate fails, fallback to summary\_agent."

👉 Tum batayo: SDK is case ko kaise handle karega? Kya wo automatically alternative tool run karega ya tumhe khud logic likhna hoga?

---

# Answer

1. **Tool crash handling mechanism**

   * Har tool (chahe wo normal function ho ya agent-as-tool) ek `on_invoke_tool` ke through run hota hai.
   * Agar tool fail karta hai → SDK default me `default_tool_error_function` call karta hai jo LLM ko ek structured error message bhej deta hai.
   * Matlab LLM ko ye information milti hai:

     ```json
     { "error": "Tool call failed: translate_agent" }
     ```





