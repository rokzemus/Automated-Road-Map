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
    emps_Leaving = []
    d = 0
    k = 0
    x = 0
    v = 0

    for k in range(len(parTableList)):
        parTableList[k].gameType()
        parTableList[k].replaceDealer()

        pass

    return parTableList, parEmployeeList


def displayTable():
    print("")
    print("")


def updateTable():
    global employee_List
    global table_List
    table_List, employee_List = assignDealer(table_List, employee_List)

    displayTable()


updateTable()
