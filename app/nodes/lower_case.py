from app.models.states.state import State

def lower_case(state: State) -> State:
    lowered_name = state['my_name'].lower()
    return {'my_name' : lowered_name}
