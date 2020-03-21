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
        table_List.append(Table.Table(row[0], row[1]))


def assignDealer(parTableList, parEmployeeList):
    for i in range(len(parTableList)):
        for x in range(len(parEmployeeList)):
            if int(parEmployeeList[x].startTime) >= int(parTableList[i].dealerOut):
                if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
                    parTableList[i].dealerName = parEmployeeList[x].name
                    parTableList[i].dealerOut = parEmployeeList[x].endTime
                    parEmployeeList[x] = Person.Person()
                    break
                else:
                    pass
    return parEmployeeList, parTableList


def displayTable():
    for i in range(len(table_List)):
        print(table_List[i])
    print("")
    print("")


employee_List, table_List = assignDealer(table_List, employee_List)

displayTable()

employee_List, table_List = assignDealer(table_List, employee_List)

displayTable()

employee_List, table_List = assignDealer(table_List, employee_List)

displayTable()
