class State:
    def __init__(self, name: str, transitions: list[tuple]):
        self.name = name
        self.transitions = transitions
        for i in range(len(self.transitions)):
            if transitions[i][1] == 'self':
                transitions[i] = (transitions[i][0], self)

    def next_state(self, input_character: str):
        return next((transition[1] for transition in self.transitions
                     if input_character in transition[0]),
                    None)
