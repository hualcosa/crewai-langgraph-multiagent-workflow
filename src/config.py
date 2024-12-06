from crewai import LLM
from langchain_aws import ChatBedrockConverse
from langchain_community.utilities import OpenWeatherMapAPIWrapper

bedrock_llm = LLM(
    model="bedrock/anthropic.claude-3-sonnet-20240229-v1:0", temperature=0
)

langchain_llm = ChatBedrockConverse(
    model="anthropic.claude-3-sonnet-20240229-v1:0",
    temperature=0,
    region_name="us-west-2",
)

weather = OpenWeatherMapAPIWrapper()
