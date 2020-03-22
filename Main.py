import csv
import Person
import Table

employee_List = []
table_List = []

with open('schedule.csv', 'r') as Schedule:
    reader = csv.reader(Schedule)
    for row in reader:
        employee_List.append(Person.Person(row[0], row[1], row[2], row[3]))

with open('gameList.csv', 'r') as GameList:
    reader = csv.reader(GameList)
    for row in reader:
        table_List.append(Table.Table(row[0], row[1], row[2], row[3]))


def assignDealer(parEmployeeList, parTableList):
    b = 0
    for x in range(len(parEmployeeList)):
        for i in range(len(parTableList)):
            if not parTableList[i].isFull() and parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                parTableList[i].dealerName = parEmployeeList[x].name
                b = int(parTableList[i].slotsUsed) + 1
                parTableList[i].dealerOut = parEmployeeList[x].endTime
                parEmployeeList[x] = Person.Person()
            for n in range(len(table_List[i].dealerName)):
                if int(parEmployeeList[x].startTime) >= int(parTableList[i].dealerOut[n]):
                    if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                        parTableList[i].dealerName[n] = parEmployeeList[x].name
                        parTableList[i].dealerOut[n] = parEmployeeList[x].endTime
                        parEmployeeList[x] = Person.Person()
                        #parTableList[i].slotsUsed += 1
                        print(parTableList[i].isFull(), parTableList[i])
                        pass
                    else:
                        pass
                else:
                    break
    return parTableList, parEmployeeList


def displayTable():
    for i in range(len(table_List)):
        print(table_List[i])
        #print(table_List[i].slotsNeeded, table_List[i].dealerName)
        pass

def updateTable():
    global employee_List
    global table_List
    table_List, employee_List = assignDealer(employee_List, table_List)

    displayTable()

updateTable()