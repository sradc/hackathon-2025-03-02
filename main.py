from dataclasses import dataclass

import browser_use
from langchain_openai import ChatOpenAI


@dataclass
class Field:
    name: str
    type: str
    description: str
    nullable: bool = True


HIGH_LEVEL_SEARCH = """Find the """

REQUIRED_FILEDS = [
    Field(name="is_available", type="boolean", description="Whether the property is still available"),
    Field(name="available_date", type="date", description="The date the property became available"),
    Field(name="cost_pcm", type="number", description="The cost per month of the property"),
    Field(name="proximity_of_tube_bus", type="number", description="The proximity of the property to the nearest tube or bus station"),
    Field(name="let_type", type="string", description="The type of let the property is"),
    Field(name="deposit", type="number", description="The deposit of the property"),
    Field(name="furnish_type", type="string", description="The type of furnishing the property has"),
    Field(name="min_tenancy", type="number", description="The minimum tenancy of the property"),
    Field(name="council_tax", type="number", description="The council tax of the property"),
    Field(name="location", type="string", description="The location of the property"),
    Field(name="property_type", type="string", description="The type of property"),
    Field(name="bedrooms", type="number", description="The number of bedrooms in the property"),
    Field(name="bathrooms", type="number", description="The number of bathrooms in the property"),
    Field(name="size", type="number", description="The size of the property"),
    # Field(name="lease_type", type="string", description="The type of lease the property is on"),
    Field(name="utility_providers", type="string", description="The utility providers of the property"),
    Field(name="utility_price_estimates", type="string", description="The estimated cost of the utilities of the property"),
    Field(name="parking", type="boolean", description="Whether the property has parking"),
    Field(name="pets", type="boolean", description="Whether the property allows pets"),
]


async def search_agent(query):
    agent = browser_use.Agent(
        task=SEARCH_TASK.format(query=query),
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run(query)
