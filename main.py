import browser_use
from langchain_openai import ChatOpenAI

SEARCH_TASK = """"""

REQUIRED_FILEDS = [
    ""
]


async def search_agent(query):
    agent = browser_use.Agent(
        task=SEARCH_TASK.format(query=query),
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run(query)
