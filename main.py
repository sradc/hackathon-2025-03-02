from dataclasses import dataclass
from datetime import date

import browser_use
import pydantic
from langchain_openai import ChatOpenAI



@dataclass
class Field:
    name: str
    type: str
    description: str
    nullable: bool = True


FIND_PROPERTIES_TASK = """Return the links to the specific properties (i.e. pages of individual properties) that match the following criteria: {query}"""
EXTRACT_PROPERTY_DETAILS_TASK = """Extract the specified fields from the property at this link: {link}

{required_fields}
"""


class Property(pydantic.BaseModel):
    pass


class Schema(pydantic.BaseModel):
    is_available: bool | None = pydantic.Field(default=None, description="Whether the property is still available")
    available_date: date | None = pydantic.Field(default=None, description="The date from which the property will be available")
    cost_pcm: float | None = pydantic.Field(default=None, description="The cost per calendar month of the property")
    proximity_of_tube_bus: float | None = pydantic.Field(default=None, description="The proximity of the property to the nearest tube or bus station in minutes")
    let_type: str | None = pydantic.Field(default=None, description="The type of let the property is")
    deposit: float | None = pydantic.Field(default=None, description="The amount of deposit of the property")
    furnish_type: bool | None = pydantic.Field(default=None, description="Whether the property is furnished")
    min_tenancy: int | None = pydantic.Field(default=None, description="The minimum tenancy duration of the property")
    council_tax: float | None = pydantic.Field(default=None, description="The council tax of the property")
    location: str | None = pydantic.Field(default=None, description="The location of the property")
    property_type: str | None = pydantic.Field(default=None, description="The type of property")
    bedrooms: int | None = pydantic.Field(default=None, description="The number of bedrooms in the property")
    bathrooms: int | None = pydantic.Field(default=None, description="The number of bathrooms in the property")
    size: int | None = pydantic.Field(default=None, description="The size of the property in square feets")
    utility_prices_estimate: int | None = pydantic.Field(default=None, description="The estimated cost of the utilities of the property")
    parking: bool | None = pydantic.Field(default=None, description="Whether the property has parking")
    pets: bool | None = pydantic.Field(default=None, description="Whether the property allows pets")


async def find_properties_agent(query):
    agent = browser_use.Agent(
        task=FIND_PROPERTIES_TASK.format(query=query),
        llm=ChatOpenAI(model="gpt-4o"),
    )
    return await agent.run()


async def extract_property_details_agent(link):
    agent = browser_use.Agent(
        task=EXTRACT_PROPERTY_DETAILS_TASK.format(
            link=link,
            required_fields=Schema.model_json_schema(),
        ),
        llm=ChatOpenAI(model="gpt-4o"),
    )
    return await agent.run()
