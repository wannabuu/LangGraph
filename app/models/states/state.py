from typing_extensions import TypedDict

#state fore all graph
class State(TypedDict):
    input_prompt: str
    my_name: str
    output: str

#state only input
class InputState(TypedDict):
    input_prompt: str
    my_name: str  