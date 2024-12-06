from typing import TypedDict


class AgentState(TypedDict):
    messages: list[str]
    email: str
    query: str
    category: str
