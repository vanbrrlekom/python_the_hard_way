class Game(object):
    def __init__(self):
        self.room = "room"
        self.Inventory = []

    def get_outcomes(self, input):
        outcomes = {
            "Unlock library": "turn_lock",
            "Add mean tweets": "add_mean_tweets"
        }

        outcome_method_name = outcomes.get(input)
        if outcome_method_name:
            outcome_method = getattr(self, outcome_method_name)
            return outcome_method()

    def turn_lock(self):
        return self.room.turn_lock()

    def add_mean_tweets(self):
        self.Inventory.append(mean_tweets)
        return "Mean tweets added to inventory."

game = Game()
outcome = game.get_outcomes("Unlock library")
print(outcome)
print(game.Inventory)

outcome = game.get_outcomes("Add mean tweets")
print(outcome)
print(game.Inventory)