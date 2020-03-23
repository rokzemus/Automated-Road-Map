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
    #for row in reader:
    for row in reader:
        table_List.append((row[0], int(row[1], row[2], row[3])))


def assignDealer(parTableList, parEmployeeList):
    # non full table
    for tbl in range(len(parTableList)):
        if int(parTableList[tbl].slotsUsed) == int(parTableList[tbl].slotsNeeded):
            parTableList[tbl].isFull = True
            pass
        for x in range(len(parEmployeeList)):
            if parEmployeeList[x].alreadyDealing == False:
                for n in range(int(len(parTableList[tbl].dealerName))):
                    parTableList[tbl].slotsUsed = n
                    print(n)
                    pass
                    if parTableList[tbl].gameCode in parEmployeeList[x].gamesKnown:
                        parTableList[tbl].dealerName.append(parEmployeeList[x].name)
                        parEmployeeList[x].alreadyDealing = True
                        print(table_List)

                        pass
                pass
            pass

            # for x in range(len(parEmployeeList)):
            #     for i in range(len(parTableList)):
            #         if not parTableList[i].isFull() and parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
            #             parTableList[i].dealerName.append(parEmployeeList[x].name)
            #             parTableList[i].dealerOut.append(parEmployeeList[x].endTime)
            #             parEmployeeList[x] = Person.Person()
            #             b = int(parTableList[i].slotsUsed)
            #             b += 1
            #             print(b)
            #             if b >= 4:
            #                 b = 0
            #                 break
            #             pass
            #
            #         for n in range(len(table_List[i].dealerName)):
            #             if int(parEmployeeList[x].startTime) >= int(parTableList[i].dealerOut[n]):
            #                 if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
            #                     parTableList[i].dealerName[n].append(parEmployeeList[x].name)
            #                     parTableList[i].dealerOut[n].append(parEmployeeList[x].endTime)
            #                     parEmployeeList[x] = Person.Person()
            #                     #parTableList[i].slotsUsed += 1
            #                     print(parTableList[i].isFull(), parTableList[i])
            #                     if b >= 4:
            #                         b = 0
            #                         break
            #                     pass
            #                 else:
            #                     pass
            #             else:
            #                 break
    return parTableList, parEmployeeList


def displayTable():
    for i in range(len(table_List)):
        print(table_List[i])
        print(table_List[i].slotsNeeded)
        pass


def updateTable():
    global table_List
    global employee_List
    table_List, employee_List = assignDealer(table_List, employee_List)

    displayTable()


updateTable()
