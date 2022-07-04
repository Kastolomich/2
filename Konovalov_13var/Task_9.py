class StateMachine:
    state = 'A'

    def herd(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'F'
            return 3
        elif self.state == 'H':
            self.state = 'E'
            return 11
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise(KeyError)

    def put(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise(KeyError)

    def align(self):
        if self.state == 'G':
            self.state = 'A'
            return 10
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise(KeyError)

    def push(self):
        if self.state == 'C':
            self.state = 'A'
            return 5
        else:
            raise(KeyError)


def main():
    return StateMachine()
