from crewai import Agent
from .tools import Tools
from ..config import bedrock_llm


class Agents:
    @staticmethod
    def classifierAgent():
        return Agent(
            role="Email Classifier",
            goal="You will be given an email and you have to classify the given email in one of these 2 categories: 1) Important 2) Casual ",
            backstory="An email classifier who is expert in classifying every type of email and have classified so many emails so far",
            verbose=True,
            allow_delegation=False,
            llm=bedrock_llm,
        )

    @staticmethod
    def emailWriterAgent():
        return Agent(
            role="Email writing expert",
            goal="You are email writing assistant for Shivam. You will be given an email and a category of that email and your job is to write a reply for that email. If email category is 'Important' then write the reply in professional way and If email category is 'Casual' then write in a casual way",
            backstory="An email writer with an expertise in email writing for more than 10 years",
            verbose=True,
            allow_delegation=False,
            llm=bedrock_llm,
        )

    @staticmethod
    def weatherAgent():
        return Agent(
            role="Weather Expert",
            goal="You will be given a location name and you have to find the weather information about that location using the tools provided to you",
            backstory="An weather expert who is expert in providing weather information about any location",
            tools=[Tools.weather_tool],
            verbose=True,
            allow_delegation=False,
            llm=bedrock_llm,
        )
