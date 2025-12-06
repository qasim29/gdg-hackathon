from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool, create_swarm
from dotenv import load_dotenv
load_dotenv()


# Ensure API key is set (User should provide this in env)
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def add(a: int, b: int) -> int:
    '''Add two numbers'''
    return a + b

alice = create_agent(
    "google_genai:gemini-2.5-flash-lite",
    tools=[
        add,
        create_handoff_tool(
            agent_name="Bob",
            description="Transfer to Bob",
        ),
    ],
    system_prompt="You are Alice, an addition expert.",
    name="Alice",
)

bob = create_agent(
    "google_genai:gemini-2.5-flash-lite",
    tools=[
        create_handoff_tool(
            agent_name="Alice",
            description="Transfer to Alice, she can help with math",
        ),
    ],
    system_prompt="You are Bob, you speak like a pirate.",
    name="Bob",
)

checkpointer = InMemorySaver()
workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice"
)
compiled_agent = workflow.compile(checkpointer=checkpointer)
