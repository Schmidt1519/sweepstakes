import user_interface


class Contestant:

    def __init__(self, first_name, last_name, email_address, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.registration_number = registration_number


    def notify(self, is_winner):  # is_winner coming from Sweepstakes def pick_winner
        user_interface.notify_contestants(is_winner)