from app.models.states.state import State
from langchain_openai import ChatOpenAI

def generate_response(state : State) -> State:
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0
    )
    input_prompt = state['input_prompt']
    my_name = state['my_name']

    prompt = f'My name is {my_name}. This is my query: {input_prompt}'
    response = llm.invoke(prompt)

    return{'output' : response.content}
