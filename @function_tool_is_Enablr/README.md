🛠️ Understanding @function_tool and is_enabled 

📌 1. What is @function_tool?

Normally ek Python function apna kaam karta hai.

Lekin agar hum us function ko agent ke liye tool banana chahte hain → to hum @function_tool decorator lagate hain.


Example:

@function_tool()
def greet():
    return "Hello, User!"

👉 Ab greet() ek agent tool ban gaya jo call ho sakta hai.


---

📌 2. What is is_enabled?

is_enabled ek option hai jo decide karta hai ki tool available hoga ya nahi.

Teen tareeqe hote hain:



---

✅ Case A: Always Enabled

@function_tool(is_enabled=True)
def greet():
    return "Hello, User!"

Tool hamesha sabke liye available.



---

❌ Case B: Always Disabled

@function_tool(is_enabled=False)
def greet():
    return "Hello, User!"

Tool kabhi use nahi ho sakta.



---

🎯 Case C: Conditional (Dynamic)

def only_admin(run_context, tool):
    return run_context.get("user_name") == "Ali"

@function_tool(is_enabled=only_admin)
def add_member():
    return "Member added to group"

Ab tool sirf Ali ke liye enabled hai.

SDK jab tool ko check karega → wo run_context aur tool automatically pass karega.

Agar function True return kare → tool enable. Agar False → disable.



---

📌 3. Why Parameters in is_enabled Function?

Jab is_enabled ek function hai → usko 2 arguments lena hi padenge:

1. run_context → Current user/session info (e.g. user_name)


2. tool → Kaunsa tool call ho raha hai



Example:

def is_Admin(run_context, tool):
    # Sirf Ali ka naam match ho to enable
    return run_context.get("user_name") == "Ali"

⚠️ Agar ye parameters nahi doge → Python error aayega:

TypeError: is_Admin() missing 2 required positional arguments

👉 Isliye aksar log default =None dete hain taake manual call karne par bhi error na aaye:

def is_Admin(run_context=None, tool=None):
    ...


---

📌 4. Summary Table

Case	is_enabled value	Parameters required?	Tool availability

Fixed Enabled	True	❌ No	Always available
Fixed Disabled	False	❌ No	Never available
Conditional	Function	✅ Yes (run_context, tool)	Depends on logic

