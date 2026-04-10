

🧠 OpenAI Agents SDK

1.

By default, when you import the OpenAI Agents SDK, which source is first checked for the API key?
A) set_default_openai_key()
B) OPENAI_API_KEY environment variable
C) AsyncOpenAI(api_key="...") custom client
D) Responses API internal fallback

Answer: 


---

2.

If you never set an API key manually, which client does the SDK automatically create?
A) SyncOpenAI with default key
B) AsyncOpenAI using environment key
C) AsyncOpenAI using no key
D) A mock client for debugging

Answer: 


---

3.

What is the default API type used by the SDK if you don’t call set_default_openai_api()?
A) chat_completions
B) responses
C) whichever is first imported
D) none, until explicitly set

Answer: 


---

4.

Calling set_default_openai_api("chat_completions") has which effect?
A) Forces SDK to reject Responses API requests
B) Switches default from Responses API to Chat Completions API
C) Enables dual API usage
D) Automatically disables tracing

Answer: 


---

5.

Which statement about tracing is TRUE by default?
A) Tracing is disabled unless explicitly enabled
B) Tracing is enabled and uses the default API key
C) Tracing is enabled but needs a separate tracing key always
D) Tracing only logs if verbose mode is on

Answer: 


---

6.

If you want tracing to use a different API key than your LLM requests, which function should you use?
A) set_default_openai_key()
B) set_tracing_export_api_key()
C) set_default_openai_client()
D) set_tracing_disabled()

Answer: 


---

7.

What happens if you call set_default_openai_key("sk-123", use_for_tracing=False)?
A) Key is ignored completely
B) Key is set only for requests, not tracing
C) Key is used for tracing only
D) SDK crashes due to missing tracing key

Answer: 


---

8.

Which logger names exist in the SDK by default?
A) openai.sdk and openai.sdk.tracing
B) openai.agents and openai.agents.tracing
C) openai.core and openai.trace
D) openai.api and openai.logs

Answer: 


---

9.

What is the default logging level if no custom logger is configured?
A) DEBUG for all logs
B) INFO for all logs
C) Only WARNING and ERROR visible
D) No logs are shown

Answer: 


---

10.

Which environment variable disables logging of LLM inputs and outputs?
A) OPENAI_DONT_LOG
B) OPENAI_AGENTS_DONT_LOG_MODEL_DATA
C) OPENAI_AGENTS_DISABLE_LOGS
D) OPENAI_MODEL_LOGGING_OFF

Answer: 


---

11.

Which environment variable disables logging of tool inputs and outputs?
A) OPENAI_AGENTS_DONT_LOG_TOOL_DATA
B) OPENAI_DISABLE_TOOL_LOGS
C) OPENAI_AGENTS_NO_TOOL_LOGGING
D) OPENAI_LOGS_OFF

Answer: 


---

12.

If you want all logs including DEBUG to show up, what should you do?
A) logger.setLevel(logging.INFO)
B) logger.setLevel(logging.DEBUG)
C) enable_verbose_stdout_logging() only
D) Export OPENAI_ENABLE_ALL_LOGS=1

Answer: 


---

13.

What happens if you never set a tracing key but tracing is enabled?
A) SDK throws an error
B) SDK reuses the default OpenAI API key for tracing
C) Tracing silently fails
D) SDK switches to mock tracing

Answer: 


---

14.

Which function completely disables tracing in the SDK?
A) disable_tracing()
B) set_tracing_disabled(True)
C) turn_off_tracing()
D) set_tracing_export_api_key(None)

Answer: 


---

15.

What is the effect of calling set_default_openai_client(custom_client, use_for_tracing=True)?
A) Only requests use custom client; tracing still uses old key
B) Requests and tracing both use the custom client’s API key
C) Requests fail since custom client overrides environment
D) Tracing is disabled automatically

Answer: B


---

16.

Which API type (responses vs chat_completions) is recommended for beginners according to docs?
A) responses
B) chat_completions
C) both equally
D) neither, must be explicitly configured

Answer: 


---

17.

If you forget to call set_default_openai_key() and don’t have OPENAI_API_KEY set, what happens?
A) SDK automatically fetches a free trial key
B) SDK errors because no key is found
C) SDK uses a fallback test key
D) SDK silently disables API calls

Answer: 


---

18.

Which function allows you to see more logs directly in stdout without configuring Python’s logging module?
A) enable_verbose_stdout_logging()
B) enable_stdout_debugging()
C) show_all_logs()
D) set_logging_verbose(True)

Answer: 


19.

Why is it dangerous to keep use_for_tracing=True when setting your default key?
A) Tracing may consume extra tokens and cost
B) Sensitive data may appear in tracing logs
C) It disables Responses API
D) It makes SDK slower

Answer:

20.

Which of the following is the most correct description of default SDK behavior (if no functions are called)?
A) Uses Responses API, AsyncOpenAI client with OPENAI_API_KEY, tracing ON with same key, warnings/errors logs only
B) Uses Chat Completions API, requires manual key set, tracing OFF, no logs
C) Uses Responses API, requires manual client, tracing OFF, all logs enabled
D) No defaults, everything must be configured

.

