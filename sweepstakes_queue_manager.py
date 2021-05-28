import data_queue
from data_queue import Queue
from sweepstake import Sweepstake


class SweepstakesQueueManager:

    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):  # takes in sweepstakes object and passes it in
        data_queue.Queue.enqueue(sweepstakes)

    def get_sweepstakes(self):  # should return a sweepstakes object
        # remove sweepstakes from queue
        # return that sweepstakes
        pass