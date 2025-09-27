from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, enable_verbose_stdout_logging
from dotenv import load_dotenv
from rich import print
import os


set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY=os.environ.get("GEMINI_API_KEY")
enable_verbose_stdout_logging()

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
)


english_agent = Agent(
    name="English Linguistic",
    instructions="You are expert in English language",
    model=model
)

urdu_agent = Agent(
    name="Urdu Linguistic",
    instructions="You are expert in Urdu language",
    model=model
)

orchestrator_agent=Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        english_agent.as_tool(
            tool_name="translate_to_english",
            tool_description="Translate the user's message to English"
        ),
        urdu_agent.as_tool(
            tool_name="translate_to_urdu",
            tool_description="Translate the user's message to Urdu",
        )
    ],
     tool_use_behavior="stop_on_first_tool",
    model=model
)

result = Runner.run_sync(
    starting_agent=orchestrator_agent,
    input="tum kia kar rahy ho, translate it to english and my name is shah translate this into urdu"
)

print(result.final_output)

#🔹 1. Agent as Tool ka Model

#Jab aap agent ko ek tool ke taur pe expose karte ho (agent.as_tool()), to usko chalane ke liye bhi ek LLM model chahiye hota hai (jaise gpt-4o-mini, gpt-4.1, waghera).

#Agar aap explicitly model pass nahi karte (model=...), to wo SDK default logic use karega.

#🔹 2. OpenAI SDK ka Behavior

#OpenAI SDK me by default model inference hoti hai. Agar aapne Runner ya Agent banate waqt already ek default model set kiya hai, to agent.as_tool() bhi usi ko pick kar lega.

#Is liye OpenAI models ke sath aapko error nahi milta — kyunki wo fallback karke default model use kar leta hai.

#🔹 3. Gemini ya Dusre Providers ka Case

#Gemini ya koi dusra provider (Anthropic, Mistral, etc.) me ye fallback behavior hamesha available nahi hota.

#Agar aap agent.as_tool() banate waqt model pass nahi karte, to backend pe jab function decorator (@function_tool) call hota hai aur LLM inference ki zaroorat hoti hai, tab error throw karega — kyunki SDK ko samajh nahi ayega kaunsa model use karna hai.

#🔹 4. Error Handling

#Haan, @function_tool ke andar error wrapping hoti hai (tool crash se poora agent crash na ho).

#Lekin agar model hi missing hai, to wo runtime error dega (jaise "Model must be provided for tool execution" type).
