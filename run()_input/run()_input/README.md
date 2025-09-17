OpenAI Agents SDK – run() Input Guide (Complete)
Introduction

Ye guide explain karta hai ki run() function me input kaise dena hai, kya valid hai, kya galat ho sakta hai, aur kab errors aayenge

1️⃣ Input Types
A) String Input

Agar aap single message bhejna chahte ho, string type ka input valid hai.

SDK automatically is string ko convert kar deta hai TResponseInputItem me with role="user".

result1 = run(
    starting_agent=my_agent,
    input="Hello, summarize this article."
)


✅ Explanation:

String → single TResponseInputItem

role = "user"

content = string value

B) List Input

Multi-turn conversation ke liye list of dictionaries dena hota hai.

Har dictionary ke 2 mandatory keys: role aur content.

conversation_input = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help?"},
    {"role": "system", "content": "Only respond in short sentences."}
]

result2 = run(
    starting_agent=my_agent,
    input=conversation_input,
    max_turns=5
)


✅ Explanation:

Har item sequentially process hota hai

Roles (user/assistant/system) aur content preserve hoti hai

Multi-turn conversation ke liye list zaruri hai

2️⃣ Mandatory Dict Structure
Correct Example
input_data = [
    {"role": "user", "content": "Hello, can you summarize this?"},
    {"role": "assistant", "content": "Sure! Here's the summary..."},
    {"role": "system", "content": "Only respond in short sentences."}
]

Incorrect Examples
# Missing role → Error
bad_input1 = [{"content": "Hello"}]

# Missing content → Error
bad_input2 = [{"role": "user"}]


# Content not string → Error
bad_input4 = [{"role": "user", "content": 123}]

3️⃣ Common Errors & When They Occur
Error	Cause
TypeError	Input mix (string + list) or invalid type in content
ValidationError	Missing role or content key in dict
GuardrailTripwireTriggered	Guardrail rules violated on input/output
MaxTurnsExceeded	max_turns limit exceeded
4️⃣ Tips for Correct Input

role values allowed: "user", "assistant", "system"

content hamesha string honi chahiye

Multi-turn conversation → list of items

Single message → string sufficient

Previous conversation → use conversation_id + list

5️⃣ Practical Examples
Example 1 – Single string input
result = run(
    starting_agent=my_agent,
    input="What is AI?"
)


Auto converts to single TResponseInputItem

Role = "user"

Example 2 – List input
messages = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi! How can I help?"}
]

result = run(
    starting_agent=my_agent,
    input=messages,
    max_turns=3
)


Multiple items processed sequentially

Roles preserved → agent knows context

Example 3 – Invalid input causing error
bad_messages = [
    {"role": "user"}  # content missing
]

run(starting_agent=my_agent, input=bad_messages)
# → ValidationError thrown

6️⃣ Key Takeaways

String input → single message, simple case

List input → multi-turn, roles preserved

Mandatory keys → role + content

Errors → occur if keys missing, content invalid, type mix

Conversation history → use conversation_id + list

💡 Pro Tip:

Always check role + content for each dictionary. Agar correct nahi → run() fail ho jayega.

