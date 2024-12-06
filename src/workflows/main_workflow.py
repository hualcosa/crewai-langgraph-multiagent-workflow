from langgraph.graph import Graph, END, StateGraph
from ..models.state import AgentState
from ..nodes.workflow_nodes import Nodes


def where_to_go(state):
    cat = state["category"]
    print("Category: ", cat)
    if cat == "email_query":
        return "email"
    elif cat == "weather_query":
        return "weather"
    else:
        return "reply"


def create_workflow():
    workflow = StateGraph(AgentState)
    node = Nodes()

    # Add nodes with updated method names
    workflow.add_node("entryNode", node.entry_node)
    workflow.add_node("weatherNode", node.weather_node)
    workflow.add_node("responder", node.reply_node)
    workflow.add_node("emailNode", node.writer_node)

    # Add edges
    workflow.add_conditional_edges(
        "entryNode",
        where_to_go,
        {"email": "emailNode", "weather": "weatherNode", "reply": "responder"},
    )
    workflow.add_edge("weatherNode", END)
    workflow.add_edge("responder", END)
    workflow.add_edge("emailNode", END)

    workflow.set_entry_point("entryNode")
    return workflow.compile()


app = create_workflow()
