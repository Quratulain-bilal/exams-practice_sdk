
⚙️ OpenAI Agents SDK – Configuration (Roman Urdu with Defaults)


---

🔑 1. API Keys (By Default)

Jab ap SDK import karte ho, woh automatically check karta hai:

Environment variable OPENAI_API_KEY


Agar yeh set hai → wahi key use hoti hai.

Agar ap set_default_openai_key("sk-...") use karo → key manually set ho jati hai.


👉 Default behavior: OPENAI_API_KEY environment variable use hota hai.


---

🤝 2. Clients (By Default)

SDK automatically apna ek AsyncOpenAI client bana leta hai.

Us client ke andar woh API key environment variable wali dalta hai.

ap chaho to custom client bana ke set_default_openai_client() ke through de sakte ho.


👉 Default behavior: built-in AsyncOpenAI client with your environment key.


---

🛠 3. API Type (By Default)

Docs aur code dono ke mutabiq:

Default API = Responses API

Agar ap change karna chaho to set_default_openai_api("chat_completions") kar do.


👉 Default behavior: "responses" API use hota hai.


---

📊 4. Tracing (By Default)

Tracing by default enabled hota hai.

Woh wahi API key use karega jo tumne environment mein ya set_default_openai_key() se di hai.

Agar ap chaho to:

set_tracing_export_api_key("sk-...") se alag key do

Ya set_tracing_disabled(True) se tracing band kar do



👉 Default behavior: Tracing = ON, same key use hoti hai.


---

🐞 5. Logging (By Default)

SDK ke paas do loggers hote hain (openai.agents, openai.agents.tracing).

By default sirf warnings aur errors stdout pe jate hain.

Agar ap detailed logs chaho to enable_verbose_stdout_logging() use karo.


👉 Default behavior: Sirf warnings/errors dikhte hain.


---

✅ Summary (Defaults)

Feature	Default Behavior	Change karne ka tareeqa

API Key	OPENAI_API_KEY env variable se uthata hai	set_default_openai_key("sk-...")
Client	Built-in AsyncOpenAI client banata hai	set_default_openai_client(custom_client)
API Type	"responses" API use hota hai	set_default_openai_api("chat_completions")
Tracing	Enabled (same key use karta hai)	set_tracing_export_api_key() ya set_tracing_disabled(True)
Logging	Sirf warnings/errors stdout par	enable_verbose_stdout_logging() ya custom logging setup
