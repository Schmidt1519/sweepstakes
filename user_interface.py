import contestant
from contestant import Contestant
from sweepstake import Sweepstake
import sweepstakes_queue_manager
import sweepstakes_stack_manager

def create_sweepstakes():
    sweepstakes_name = input('What is the name of your sweepstake?')
    created_sweepstake = Sweepstake(sweepstakes_name)
    sweepstakes_management(created_sweepstake)


def sweepstakes_management():
    user_input = int(input('Would you like the sweepstakes to be stored in a (1) Stack or (2) Queue?'))
    if user_input == 1:
        print('Stack management')  # test
        sweepstakes_stack_manager.SweepstakesStackManager.insert_sweepstakes()
    elif user_input == 2:
        sweepstakes_queue_manager.SweepstakesQueueManager.insert_sweepstakes()
        print('Queue management')  # test
    else:
        sweepstakes_management()


def get_user_input():
    first_name = input('First name: ')
    last_name = input('Last name: ')
    email_address = input('Email address: ')
# pass to Contestant attributes?


def display_message(text):
    print(f'{text}')


# to be used in print_contestant_information method on Sweepstakes class
def display_user_information(is_winner):
    print(f'Winner information: {is_winner[1].first_name} {is_winner[1].last_name} - {is_winner[1].email_address}')