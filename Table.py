import Person
import Main

class Table():
    def __init__(self, gameCode = '', gameNum = 0, slotsNeeded = 1, slotsUsed = 0, dealerName = [],
                 dealerOut = [], isOpen = False):
        self.gameCode = gameCode
        self.gameNum = gameNum
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.dealerName = dealerName
        self.dealerOut = dealerOut
        self.isOpen = isOpen

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.dealerName}"

    def isFull(self):
        if self.slotsNeeded == self.slotsUsed:
            return True
#        else:
#            return False

    def gameType(self):
        gameTypes = {"CR": 4, "BJ": 1}
        self.slotsNeeded = gameTypes[self.gameCode]


    def fillSlot(self):
        self.isOpen = True

