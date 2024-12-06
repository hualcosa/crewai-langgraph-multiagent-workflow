import json
from ..crews.email_crew import EmailCrew
from ..agents.agent_definitions import Agents
from ..tasks.task_definitions import Tasks
from ..config import langchain_llm


class Nodes:
    def entry_node(self, state):
        input = state["query"]
        agent = langchain_llm.invoke(f"""
        User input
        ---
        {input}
        ---
        You have given one user input and you have to perform actions on it based on given instructions

        Categorize the user input in below categories
        email_query: If user want to generate a reply to given email
        weather_query: If user want any weather info about given location
        other: If it is any other query

        After categorizing your final RESPONSE must be in json format with these properties:
        category: category of user input
        email: If category is 'email_query' then extract the email body from user input with proper line breaks and add it here else keep it blank
        query: If category is 'weather_query' or 'other' then add the user's query here else keep it blank
        """)
        response = json.loads(agent.content)
        return {
            "email": response["email"],
            "query": response["query"],
            "category": response["category"],
        }

    def writer_node(self, state):
        email = state["email"]
        emailCrew = EmailCrew(email)
        crewResult = emailCrew.run()
        messages = state["messages"]
        messages.append(crewResult)
        return {"messages": messages}

    def weather_node(self, state):
        query = state["query"]
        weatherAgent = Agents.weatherAgent()
        weatherTask = Tasks.weatherTask(agent=weatherAgent, query=query)
        result = weatherTask.execute()
        messages = state["messages"]
        messages.append(result)
        return {"messages": messages}

    def reply_node(self, state):
        query = state["query"]
        agent = langchain_llm.invoke(f"""
            {query}
        """)
        messages = state["messages"]
        messages.append(agent.content)
        return {"messages": messages}

    # ... other node methods ...
