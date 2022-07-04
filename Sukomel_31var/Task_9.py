class StateMachine:
    state = 'A'

    def file(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'D':
            self.state = 'A'
            return 5
        elif self.state == 'G':
            self.state = 'D'
            return 8
        elif self.state == 'C':
            self.state = 'D'
            return 2
        else:
            raise(KeyError)

    def mass(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            return 3
        elif self.state == 'G':
            self.state = 'A'
            return 9
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'D':
            self.state = 'E'
            return 4
        else:
            raise(KeyError)


def main():
    return StateMachine()
