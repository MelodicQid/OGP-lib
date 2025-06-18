class Observer:
    def __init__(self, input_data):
        self.input = input_data
        self.level = self._determine_level()
        self.state = self._collapse()

    def _determine_level(self):
        if isinstance(self.input, Observer):
            return self.input.level + 1
        return 1

    def _collapse(self):
        if isinstance(self.input, Observer):
            return hash((self.input.state, self.level)) % 9973
        return hash(self.input) % 9973

    def __repr__(self):
        return f"O{self.level}(...) -> state:{self.state}"
