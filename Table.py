class Table():
    def __init__(self, gameCode = '', gameNum = 0, isOpen = False, slotsNeeded = 1, slotsUsed = 0, dealerName = '',
                 dealerOut = -1):
        self.gameCode = gameCode
        self.gameNum = gameNum
        self.isOpen = isOpen
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.dealerName = dealerName
        self.dealerOut = dealerOut

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.dealerName}"
