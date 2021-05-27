import contestant
from contestant import Contestant
import sweepstake


def sweepstakes_management(self):
    user_input = int(input('Would you like the sweepstakes to be stored in a (1) Stack or (2) Queue?'))
    if user_input == 1:
        print('Stack management')  # test
    elif user_input == 2:
        print('Queue management')  # test
    else:
        sweepstakes_management()


def create_sweepstakes(self):
    sweepstakes_name = input('What is the name of your sweepstake?')
    return sweepstakes_name


def get_user_input(self):
    self.get_user_input_first_name()
    self.get_user_input_last_name()
    self.get_user_input_email_address()
# pass to Contestant attributes?


def get_user_input_first_name(self):
    first_name = input('First name: ')
    return first_name

def get_user_input_last_name(self):
    last_name = input('Last name: ')
    return last_name

def get_user_input_email_address(self):
    email_address = input('Email address: ')
    return email_address


def display_message(self, text):
    print(f'{text}')


# to be used in print_contestant_information method on Sweepstakes class
def display_user_information(self):
    print(f'Winner information: {contestant.first_name} {contestant.last_name} - {contestant.email_address}')