import random
import contestant
import user_interface


class Sweepstake:

    def __init__(self, name):
        self.contestants = {}
        self.name = name


    def register_contestant(self, contestant):  # takes in contestant object
        self.contestants[contestant.registration_number] = contestant


    def pick_winner(self):   # randomly select one contestant object
        entry_list = list(self.contestants.items())
        is_winner = random.choice(entry_list)
        print(is_winner)   # test. remove
        return is_winner


    def print_contestant_info(self, contestant):  # call a method on user_interface called “display_user_information”
        user_interface.display_user_information(contestant)