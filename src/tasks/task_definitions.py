from textwrap import dedent
from crewai import Task


class Tasks:
    @staticmethod
    def classificationTask(agent, email):
        return Task(
            description=dedent(f"""
            You have given an email and you have to classify this email
            {email}
            """),
            agent=agent,
            expected_output="Email category as a string",
        )

    @staticmethod
    def writerTask(agent, email):
        return Task(
            description=dedent(f"""
	      Create an email response to the given email based on the category provided by 'Email Classifier' Agent
	      {email}
	      """),
            agent=agent,
            expected_output="A very concise response to the email based on the category provided by 'Email Classifier' Agent",
        )

    @staticmethod
    def weatherTask(agent, query):
        return Task(
            description=dedent(f"""
            Get the location from the user query and find the weather information about that location

            Here is the user query:
            {query}
            """),
            agent=agent,
            expected_output="A weather information asked by user",
        )
