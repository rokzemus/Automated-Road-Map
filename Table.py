import Person
import Main


class Table():
    def __init__(self, gameCode='', gameNum=0, slotsNeeded=0, slotsUsed=0, currentDealer=[], nextDealer=[], isOpen=False, stringLoc=[]):

        self.gameCode = gameCode
        self.gameNum = gameNum
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.currentDealer = currentDealer
        self.nextDealer = nextDealer
        self.isOpen = isOpen
        self.stringLoc = stringLoc

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.currentDealer}"

    def isFull(self):
        return self.slotsNeeded == self.slotsUsed

    def gameType(self):
        gameTypes = {'CR': 4, 'BJ': 1}
        self.slotsNeeded = gameTypes[self.gameCode]
        self.currentDealer = [Person.Person()] * self.slotsNeeded

    def fillSlot(self):
        for i in self.currentDealer:
            self.slotsUsed = i
            pass

    def replaceDealer(self):
        for x in range(len(self.currentDealer)):
            for i in range(len(Main.employee_List)):
                if not Main.employee_List[i].alreadyDealing:
                    if Main.employee_List[i].startTime >= self.currentDealer[x].endTime:
                        self.currentDealer[x] = Main.employee_List[i]
                        Main.employee_List[i].alreadyDealing = True
                        x += 1
                        if x >= self.slotsNeeded:
                            x = 0
                            pass
                        pass

                    else:
                        break


    def nextRota(self, x):
        self.stringLoc += x
