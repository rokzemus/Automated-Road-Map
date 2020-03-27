''' Class Person: an individual to be scheduled on the road map. @name: the Persons name. @startTime: the time the
    individual is scheduled to work. @outTime: the time the individual is meant to leave work. @gamesKnow: a list of
    table games that the individual is capable of dealing.
'''


class Person:
    def __init__(self, name='Default', startTime=0000, endTime=0000, gamesKnown=None, alreadyDealing=False):
        if gamesKnown is None:
            gamesKnown = []
        self.name = name
        self.startTime = int(startTime)
        self.endTime = int(endTime)
        self.gamesKnown = gamesKnown
        self.alreadyDealing = alreadyDealing

    def __str__(self):
        return f"{self.name} {self.startTime} {self.endTime} {self.alreadyDealing}"

