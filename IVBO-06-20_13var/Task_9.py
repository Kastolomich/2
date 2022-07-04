class StateMachine:
    state = 'A'

    def tag(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'F':
            self.state = 'G'
            return 10
        elif self.state == 'C':
            self.state = 'H'
            return 5
        else:
            raise(KeyError)

    def dash(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'E':
            self.state = 'B'
            return 9
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 6
        else:
            raise(KeyError)

    def sit(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'G'
            return 4
        elif self.state == 'G':
            self.state = 'H'
            return 11
        else:
            raise(KeyError)


def main():
    return StateMachine()
