from app.models.states.state import State, InputState
from langgraph.graph import StateGraph, START, END
from app.nodes.lower_case import lower_case
from app.nodes.generate_response import generate_response

workflow = StateGraph(
    state_schema=State,
    input=InputState
)

#add node
workflow.add_node("lower_case",lower_case)
workflow.add_node("generate_response",generate_response)

#connect edge
workflow.add_edge(START,"lower_case")
workflow.add_edge("lower_case","generate_response")
workflow.add_edge("generate_response",END)

#compile graph
graph = workflow.compile()

#export graph
with open("./graph.png","wb") as file:
    file.write(graph.get_graph().draw_mermaid_png())
