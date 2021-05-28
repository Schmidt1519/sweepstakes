from stack import Stack


class SweepstakesStackManager:

    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):  # takes in sweepstakes object and passes it in the stack
        self.stack.push(sweepstakes)

    def get_sweepstakes(self):  # should return a sweepstakes object
        return self.stack.pop()