import Person


class Table():
    def __init__(self, gameCode='', gameNum=0, slotsNeeded=0, slotsUsed=0, currentDealer=None, nextDealer=[],
                 isOpen=False, stringLoc=[]):
        self.gameCode = gameCode
        self.gameNum = int(gameNum)
        self.slotsNeeded = slotsNeeded
        self.slotsUsed = slotsUsed
        self.currentDealer = currentDealer
        self.nextDealer = nextDealer
        self.isOpen = isOpen
        self.stringLoc = stringLoc

    def __str__(self):
        return f"{self.gameCode} {self.gameNum} {self.currentDealer}"

    def displayDealers(self):
        for i in range(len(self.currentDealer)):
            print(self.gameCode, self.gameNum, self.currentDealer[i].name, self.currentDealer[i].endTime)

    def isFull(self):
        return self.slotsNeeded == self.slotsUsed

    def gameType(self):
        gameTypes = {'CR': 4, 'BJ': 1}
        self.slotsNeeded = gameTypes[self.gameCode]
        if self.currentDealer == None:
            self.currentDealer = [Person.Person()] * self.slotsNeeded

    def replaceDealer(self):
        import Main
        for x in range(len(self.currentDealer)):
            for i in range(len(Main.employee_List)):
                if not Main.employee_List[i].alreadyDealing:
                    if Main.employee_List[i].startTime >= self.currentDealer[x].endTime:
                        self.currentDealer[x] = Main.employee_List[i]
                        Main.employee_List[i].alreadyDealing = True
                        self.slotsUsed += 1

                        x += 1
                        if x >= self.slotsNeeded:
                            x = 0
                            break
                        break

                    else:
                        pass
                else:
                    pass
        self.displayDealers()

    def nextRota(self, x):
        self.stringLoc += x
