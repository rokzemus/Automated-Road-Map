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
        table_List.append(Table.Table(row[0], row[1], row[2]))


def assignDealer(parTableList, parEmployeeList):
    for x in range(len(parEmployeeList)):
        for i in range(len(parTableList)):
            if parTableList[i].isFull() == False:
                if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                    parTableList[i].dealerName.append(parEmployeeList[x].name)
                    parTableList[i].dealerOut.append(parEmployeeList[x].endTime)
                    parTableList[i].slotsUsed += 1
                    parEmployeeList[x] = Person.Person()
                    pass
                else:
                    break

            elif int(parEmployeeList[x].startTime) >= int(parTableList[i].dealerOut[i]):
                for n in range(len(table_List[i].dealerName)):
                    if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                        parTableList[i].dealerName[n] = parEmployeeList[x].name
                        parTableList[i].dealerOut[n] = parEmployeeList[x].endTime
                        parEmployeeList[x] = Person.Person()
                        #parTableList[i].slotsUsed += 1
                        print(parTableList[i].isFull(), parTableList[i])
                        break
                    else:
                        pass
    return parTableList, parEmployeeList


def displayTable():
    for i in range(len(table_List)):
        print(table_List[i])
    for i in range(len(table_List)):
        print(table_List[i].slotsNeeded, table_List[i].slotsUsed)
    print("")
    print("")




def updateTable():
    global employee_List
    global table_List

    table_List, employee_List = assignDealer(table_List, employee_List)

    displayTable()

updateTable()
updateTable()
updateTable()
updateTable()
updateTable()

