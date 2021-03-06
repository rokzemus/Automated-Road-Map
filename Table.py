class Table():
    def __init__(self, gameCode = '', gameNum = 0, slotsNeeded = 4, slotsUsed = 0, dealerName = [],
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
        if int(self.slotsNeeded) == int(self.slotsUsed):
            return True
        else:
            return False


    def fillSlot(self):
        for i in self.dealerName:
            if len(self.dealerName[i]) >= self.slotsNeeded:
                pass
        return 'Full'
