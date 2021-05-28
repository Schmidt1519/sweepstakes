import random
from contestant import Contestant
import user_interface


class Sweepstake:

    def __init__(self, name):
        self.contestants = {}
        self.name = name

    def register_contestant(self, contestant):  # takes in contestant object
        self.contestants[contestant.registration_number] = contestant

    def register_new_contestant(self):
        print('Register New Contestant:')
        first_name = input('First name: ')
        last_name = input('Last name: ')
        email_address = input('Email address: ')
        registration_number = random.randint(1000, 10000)
        self.contestants[registration_number] = Contestant(first_name, last_name, email_address, registration_number)

    def pick_winner(self):   # randomly select one contestant object
        entry_list = list(self.contestants.items())
        is_winner = random.choice(entry_list)
        contestant = list(is_winner)
        contestant[1].notify(contestant)

        self.unregister(contestant[0])
        self.contestant_notification(f'{contestant[1].first_name} {contestant[1].last_name} has won the sweepstake. Please try again by registering in our future sweepstakes!\n')

        return is_winner

    def print_contestant_info(self, contestant):  # call a method on user_interface called “display_user_information”
        user_interface.display_user_information(contestant)

    def unregister(self, contestant):
        self.contestants.pop(contestant)

    def contestant_notification(self, text):
        for contestant in self.contestants.items():
            contestants = list(contestant)
            user_interface.display_message(contestants, text)