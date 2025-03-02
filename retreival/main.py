import browser_use
from langchain_openai import ChatOpenAI


async def search_agent(query):
    agent = browser_use.Agent(
        task=query,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run(query)
