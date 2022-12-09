from state import State


class PasswordStateMachine:
    def __init__(self, start_state: State, end_state: State):
        self.start_state = start_state
        self.end_state = end_state
        self.current_state = self.start_state

    def test(self, password):
        for character in password:
            self.current_state = self.current_state.next_state(character)
            if self.current_state is None:
                raise ValueError(f"Символ '{character}' не входит в алфавит")

        return self.current_state == self.end_state
