import user_interface
from contestant import Contestant
from sweepstake import Sweepstake
from marketing_firm_creator import MarketingFirmCreator

# Create contestants
contestant_1 = Contestant('Leighton', 'Schmidt', 'leighton@gmail.com', 100)
contestant_2 = Contestant('Bob', 'Jefferson', 'bob@gmail.com', 200)
contestant_3 = Contestant('Jessica', 'King', 'jessica@gmail.com', 300)

contestant_4 = Contestant('James', 'Smith', 'james@gmail.com', 400)
contestant_5 = Contestant('Lauren', 'Jensen', 'lauren@gmail.com', 500)
contestant_6 = Contestant('Dylan', 'Bryant', 'dylan@gmail.com', 600)

contestant_7 = Contestant('Jordan', 'Holtz', 'jordan@gmail.com', 700)
contestant_8 = Contestant('Carson', 'Joseph', 'carson@gmail.com', 800)
contestant_9 = Contestant('Bennett', 'Jacob', 'bennett@gmail.com', 900)

# Create sweepstakes objects
sweepstake_1 = Sweepstake('Chiefs tickets')
sweepstake_2 = Sweepstake('Bitcoin Giveaway')
sweepstake_3 = Sweepstake('The Lumineers tickets')

# Register contestants
sweepstake_1.register_contestant(contestant_1)
sweepstake_1.register_contestant(contestant_2)
sweepstake_1.register_contestant(contestant_3)

sweepstake_2.register_contestant(contestant_4)
sweepstake_2.register_contestant(contestant_5)
sweepstake_2.register_contestant(contestant_6)

sweepstake_3.register_contestant(contestant_7)
sweepstake_3.register_contestant(contestant_8)
sweepstake_3.register_contestant(contestant_9)

sweepstake_1.register_new_contestant()
sweepstake_2.register_new_contestant()
sweepstake_3.register_new_contestant()

# Insert sweepstakes into a manager object - dependency injection used to add new marketing firm to begin creating a new sweepstakes and choosing stack/queue management.
marketing_firm_1 = MarketingFirmCreator.choose_manager_type("Top Sales LLC")
marketing_firm_2 = MarketingFirmCreator.choose_manager_type("Sales R Us")
marketing_firm_3 = MarketingFirmCreator.choose_manager_type("Premiere Marketing LLC")

# Pick winner
winner_1 = sweepstake_1.pick_winner()
winner_2 = sweepstake_2.pick_winner()
winner_3 = sweepstake_3.pick_winner()

# Print Contestant Info
display_info_winner_1 = sweepstake_1.print_contestant_info(winner_1)
display_info_winner_2 = sweepstake_1.print_contestant_info(winner_2)
display_info_winner_3 = sweepstake_1.print_contestant_info(winner_3)