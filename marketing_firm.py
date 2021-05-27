import user_interface
import marketing_firm_creator


class MarketingFirm:

    def __init__(self, manager):
        self.manager = manager


    def create_sweepstakes(self):
        marketing_firm_creator.choose_manager_type()