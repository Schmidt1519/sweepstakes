from marketing_firm import MarketingFirm
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager


class MarketingFirmCreator:
    def __init__(self, name):
        self.name = name

    def choose_manager_type(self):  # MarketingFirm
        user_input = int(input('Would you like the sweepstakes to be stored in a (1) Stack or (2) Queue?'))
        if user_input == 1:
            # print('Stack management')  # test
            stack_manager = SweepstakesStackManager()
            marketing_firm = MarketingFirm(stack_manager)
            sweepstake = marketing_firm.create_sweepstakes()
            stack_manager.insert_sweepstakes(sweepstake)

        elif user_input == 2:
            # print('Queue management')  # test
            queue_manager = SweepstakesQueueManager()
            marketing_firm = MarketingFirm(queue_manager)
            sweepstake = marketing_firm.create_sweepstakes()
            queue_manager.insert_sweepstakes(sweepstake)
        else:
            self.choose_manager_type()