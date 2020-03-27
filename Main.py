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


# def assignDealer(parTableList, parEmployeeList):
#     for i in parTableList.replaceDealer():
#         return parTableList, parEmployeeList


def assignDealer(parTableList, parEmployeeList):
    emps_Leaving = []
    d = 0
    k = 0
    x = 0
    v = 0
    dlrN = 0

    filledTable = []
    for k in range(len(parTableList)):
        parTableList[k].gameType()
        parTableList[k].replaceDealer()

        pass

        # if parEmployeeList[x].alreadyDealing == True:
        #     x += 1
        #     pass
        # elif parTableList[k].isFull():
        #
        #     for dlrN in parTableList[k].dealerOut:
        #         if parEmployeeList[x].startTime in parTableList[k].dealerOut[v]:
        #             if parTableList[k].gameCode in parEmployeeList[x].gamesKnown:
        #                 parTableList[dlrN].dealerName[v] = parEmployeeList[x].name
        #                 parTableList[dlrN].dealerOut[v] = parEmployeeList[x].endTime
        #                 x += 1
        #                 dlrN += 1
        #                 emps_Leaving.append(parTableList[dlrN].dealerName[v])
        #                 print(emps_Leaving)
        #                 # parTableList[k].dealerOut[v].pop()
        #                 # parTableList[k].dealerName[v].pop()
        #                 # parTableList[k].dealerOut[v].append(parEmployeeList[x].name)
        #                 # parTableList[k].dealerOut[v].append(parEmployeeList[x].endTime)
        #             pass
        #         else:
        #             v = (v + 1)
        #             x += 1
        #             if v >= 3:
        #                 v = 0
        #                 pass
        #             if x >= 24:
        #                 x = 0
        #                 pass
        #             pass

        #
        #     elif parTableList[k].gameCode in parEmployeeList[x].gamesKnown:
        #
        #         # print(parTableList[k].gameCode, parEmployeeList[x].gamesKnown)
        #         # print(d)
        #         # print(parTableList[k].dealerName)
        #         # print(parEmployeeList[x].name)
        #         if parEmployeeList[x].name not in parTableList[k].currentDealer:
        #             d = parTableList[k].slotsUsed
        #             filledTable.append(str(parEmployeeList[x].name))
        #             d += 1
        #             # print(parTableList[k].dealerName)
        #             parTableList[k].slotsUsed = d
        #             parTableList[k].dealerOut.append(parEmployeeList[x].endTime)
        #             # print(d)
        #             parEmployeeList[x].alreadyDealing = True
        #         if d >= int(parTableList[k].slotsNeeded):
        #             d = 0
        #             parTableList[k].dealerName = filledTable
        #             filledTable = []
        #             pass
        #
        #
        #
        #         else:
        #             pass
        #     else:
        #         pass
        # else:
        #     k = 0
        #     pass

    return parTableList, parEmployeeList


#             # if parTableList[k].dealerName in parTableList[k - 1].dealerName:
#             #     if k != int(parTableList[-1].gameNum):
#             #         parTableList[k - 1].dealerName.remove(parTableList[k].dealerName)
#             # if parTableList[k].dealerOut == parTableList[k + 1].dealerOut:
#             #     if k != int(parTableList[-1].gameNum):
#             #         parTableList[k - 1].dealerOut.remove(parTableList[k].dealerOut)
#             # if k == int(parTableList[-1].gameNum):
#             #     break
#             # else:
#
#             # if int(parEmployeeList[x].startTime) == int(parTableList[i].dealerOut[i]):
#             #     for n in range(len(table_List[i].dealerName[d])):
#             #         if parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
#             #             parTableList[i].dealerName[d] = parEmployeeList[x].name
#             #             parTableList[i].dealerOut[d] = parEmployeeList[x].endTime
#             #             parEmployeeList[x] = Person.Person()
#             #             d += 1
#             #             print(parTableList[i].isFull(), parTableList[i])
#             #             if d >= int(parTableList[i].slotsNeeded):
#             #                 d = 0
#             #                 break
#             #         else:
#             #             pass
#     return parTableList, parEmployeeList
#
#
# # def assignDealer(parTableList, parEmployeeList):
# #     b = 0
# #     for i in range(len(parTableList)):
# #         for x in range(len(parEmployeeList)):
# #             silver = parEmployeeList[x]
# #             if parTableList[i].isFull():
# #                 pass
# #             elif int(len(parTableList[i].dealerName)) == int(parTableList[i].slotsNeeded):
# #                 break
# #             elif parTableList[i].gameCode in parEmployeeList[x].gamesKnown:
# #                      yellow = parTableList[i].dealerName
# #                      blue = parEmployeeList[x]
# #                      parTableList[i].dealerName = parEmployeeList[x].name
# #                      #parTableList[i].dealerOut[i] = parEmployeeList[x].endTime
# #                      parTableList[i].slotsUsed += 1
# #                      parEmployeeList[x] = Person.Person()
# #                      pass
# #                      #for n in range(len(parTableList[i].dealerName)):
# #                       #  print(parTableList[i].dealerName)
# #                        # b += 1
# #             pass
# #     return parTableList, parEmployeeList


def displayTable():
    # for i in range(len(table_List)):
    #     print(table_List[i])
    # for i in range(len(table_List)):
    #     print(table_List[i].slotsNeeded, table_List[i].slotsUsed)
    print("")
    print("")


def updateTable():
    global employee_List
    global table_List
    table_List, employee_List = assignDealer(table_List, employee_List)

    displayTable()


updateTable()
