

def display_message(contestant, text):
    print(f'{contestant[1].first_name} {contestant[1].last_name}: {text}')

# to be used in print_contestant_information method on Sweepstakes class to display all winners information
def display_user_information(is_winner):
    print(f'Winner information: {is_winner[1].first_name} {is_winner[1].last_name} - {is_winner[1].email_address}')

def notify_contestants(contestant):
    print(f'You win the sweepstake {contestant[1].first_name} {contestant[1].last_name}!\n')


