from crewai import Crew
from ..agents.agent_definitions import Agents
from ..tasks.task_definitions import Tasks


class EmailCrew:
    def __init__(self, email):
        self.email = email

    def run(self):
        classifierAgent = Agents.classifierAgent()
        writerAgent = Agents.emailWriterAgent()

        classifierTask = Tasks.classificationTask(
            agent=classifierAgent, email=self.email
        )
        writerTask = Tasks.writerTask(agent=writerAgent, email=self.email)

        crew = Crew(
            agents=[classifierAgent, writerAgent],
            tasks=[classifierTask, writerTask],
            verbose=True,
        )
        return crew.kickoff()
