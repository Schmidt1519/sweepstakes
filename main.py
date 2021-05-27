import user_interface
from marketing_firm import MarketingFirm
from contestant import Contestant
from sweepstake import Sweepstake

# marketing_firm = MarketingFirm()
# marketing_firm_creator = MarketingFirmCreator()
# user_interface.sweepstakes_management()

# Create contestants
contestant_1 = Contestant('Leighton', 'Schmidt', 'leighton@gmail.com', 1)
contestant_2 = Contestant('Bob', 'Jefferson', 'bob@gmail.com', 2)
contestant_3 = Contestant('Jessica', 'King', 'jessica@gmail.com', 3)

contestant_4 = Contestant('James', 'Smith', 'james@gmail.com', 4)
contestant_5 = Contestant('Lauren', 'Jensen', 'lauren@gmail.com', 5)
contestant_6 = Contestant('Dylan', 'Bryant', 'dylan@gmail.com', 6)

contestant_7 = Contestant('Jordan', 'Holtz', 'jordan@gmail.com', 7)
contestant_8 = Contestant('Carson', 'Joseph', 'carson@gmail.com', 8)
contestant_9 = Contestant('Bennett', 'Jacob', 'bennett@gmail.com', 9)

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

# Insert sweepstakes into a manager object
insert_sweepstakes_1 = MarketingFirm(sweepstake_1)
insert_sweepstakes_2 = MarketingFirm(sweepstake_2)
insert_sweepstakes_3 = MarketingFirm(sweepstake_3)

# Pick winner
winner_1 = sweepstake_1.pick_winner()
winner_2 = sweepstake_2.pick_winner()
winner_3 = sweepstake_3.pick_winner()

# Print Contestant Info
# sweepstake_1.print_contestant_info(winner_1)