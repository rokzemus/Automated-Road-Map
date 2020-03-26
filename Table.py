import Person
import Main


class Table():
    def __init__(self, gameCode='', gameNum=0, slotsNeeded=0, slotsUsed=0, currentDealer=[],
                 dealerOut=[], nextDealer=[], isOpen=False):

        self.gameCode = gameCode
        self.gameNum = gameNum
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.currentDealer = currentDealer
        self.dealerOut = dealerOut
        self.nextDealer = nextDealer
        self.isOpen = isOpen

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.currentDealer}"

    def isFull(self):
        return self.slotsNeeded == self.slotsUsed

    def gameType(self):
        gameTypes = {'CR': 4, 'BJ': 1}
        self.slotsNeeded = gameTypes[self.gameCode]

    def fillSlot(self):
        for i in self.currentDealer:
            self.slotsUsed = i
            pass

    def replaceDealer(self):
        for x in self.currentDealer:
            for i in Main.employee_List:
                if not i.alreadyDealing:
                    if i.startTime == x.dealerOut:
                        x = i
                        i.alreadyDealing = True
                        x.alreadyDealing = False
                        pass
                pass
