class Table():
    def __init__(self, gameCode = '', gameNum = 0, slotsUsed = 0, slotsNeeded = 1, isFull = False, dealerName = [],
                 dealerOut = [], isOpen = False):
        self.gameCode = gameCode
        self.gameNum = gameNum
        self.slotsUsed = slotsUsed
        self.slotsNeeded = slotsNeeded
        self.isFull = isFull
        self.dealerName = dealerName
        self.dealerOut = dealerOut
        self.isOpen = isOpen

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.dealerName}"

    # def isFull(self):
    #     if int(self.slotsUsed) == int(self.slotsNeeded):
    #         return True
    #     else:
    #         return False