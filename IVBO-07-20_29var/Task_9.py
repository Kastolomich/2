class StateMachine:
    state = 'A'

    def crush(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'H'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'C'
            return 10
        else:
            raise(KeyError)

    def order(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'D'
            return 5
        elif self.state == 'F':
            self.state = 'A'
            return 9
        elif self.state == 'G':
            self.state = 'H'
            return 11
        else:
            raise(KeyError)

    def sit(self):
        if self.state == 'A':
            self.state = 'H'
            return 2
        elif self.state == 'E':
            self.state = 'F'
            return 7
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise(KeyError)


def main():
    return StateMachine()
