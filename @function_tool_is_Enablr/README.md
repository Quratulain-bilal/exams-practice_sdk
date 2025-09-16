1️⃣ Function aur Decorator ka relation

Normal Python me:

def my_func():
    return "hello"

Ab agar isko agent ka tool banana hai → hum @function_tool decorator lagate hain:

@function_tool()
def my_func():
    return "hello"

Matlab: decorator ke bina ye sirf Python function hai, decorator ke saath ye agent ke liye ek tool ban jata hai.


---

2️⃣ is_enabled ka role

Ab tool ban gaya, lekin hamesha har user ke liye enable ho ya kabhi kabhi ho → yeh decide karne ke liye is_enabled option hota hai.

Case A: Hamesha enabled

@function_tool(is_enabled=True)
def my_func():
    return "hello"

Tool sabke liye hamesha available hai.

is_enabled=True ek fixed value hai → function ki zarurat nahi.


Case B: Hamesha disabled

@function_tool(is_enabled=False)
def my_func():
    return "hello"

Tool kabhi enable nahi hoga.


Case C: Sirf special condition me enable

Yahan hum function dete hain:

def only_admin(run_context, tool):
    return run_context.get("user_name") == "Ali"

@function_tool(is_enabled=only_admin)
def my_func():
    return "hello"

Ab is_enabled ek function hai jo decide karega.

SDK jab tool run karega, us waqt run_context aur tool pass karega.

Agar function True return kare → tool enable. Agar False → tool disable
