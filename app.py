from fastapi import FastAPI
from agent import Agent38
app = FastAPI(title="Code-Quality-Guardian")
agent = Agent38()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
