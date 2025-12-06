from fastapi import FastAPI, Request
from datetime import datetime
from sse_starlette.sse import EventSourceResponse
from langgraph_swarm import create_swarm
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
import json
from agent import compiled_agent
import random

app = FastAPI(title="GDG API", version="0.1.0")


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "gdg-api"
    }

@app.get("/stream")
async def stream_swarm(query: str, request: Request):
    """
    Stream the response from the swarm agent using SSE.
    """    
    async def event_generator():
        config = {"configurable": {"thread_id": str(random.randint(0, 1000))}}
        inputs = {"messages": [{"role": "user", "content": query}]}
        async for event in compiled_agent.astream_events(
            inputs,
            config,
            version="v2",
        ):
            if event["event"] == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if chunk.content:
                    yield {"data": json.dumps({"content": chunk.content})}

    return EventSourceResponse(event_generator())
