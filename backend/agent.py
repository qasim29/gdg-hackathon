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

orchestrator = create_agent(
    "google_genai:gemini-2.5-flash-lite",
    tools=[
        add,
        create_handoff_tool(
            agent_name="Content Creation",
            description="Transfer to Content Creation",
        ),
    ],
    system_prompt="You are the Orchestrator. Your main purpose is to use the Pipedream MCP servers to fetch data. After gathering the data, transfer all the content to the Content Creation agent.",
    name="Orchestrator",
)

content_creation = create_agent(
    "google_genai:gemini-2.5-flash-lite",
    tools=[
        create_handoff_tool(
            agent_name="Orchestrator",
            description="Transfer to Orchestrator, who can help with math",
        ),
    ],
    system_prompt="You are the Content Creation Agent, you speak like a pirate.",
    name="Content Creation",
)

checkpointer = InMemorySaver()
workflow = create_swarm(
    [orchestrator, content_creation],
    default_active_agent="Orchestrator"
)
compiled_agent = workflow.compile(checkpointer=checkpointer)
