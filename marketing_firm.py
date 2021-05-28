from sweepstake import Sweepstake


class MarketingFirm:

    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes_name = input('What is the name of your sweepstake?')
        created_sweepstake = Sweepstake(sweepstakes_name)
        return created_sweepstake