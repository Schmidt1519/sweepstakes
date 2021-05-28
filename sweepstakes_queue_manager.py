from data_queue import Queue


class SweepstakesQueueManager:

    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):  # takes in sweepstakes object and passes it in the queue
        self.queue.enqueue(sweepstakes)

    def get_sweepstakes(self):  # should return a sweepstakes object
        return self.queue.dequeue()
