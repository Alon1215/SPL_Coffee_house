import REPOSITORY
from DAOs import _CoffeeStands,_Activities,_Employees,_Products,_Suppliers
from DTOs import *
from REPOSITORY import repo

file = open('action.txt', 'r')
f = file.readlines()
actionList = []

for line in f:
    if line[-1]=='\n':
        line = line[:-1]
    actionList.append(line.split(', '))

print(actionList)

for activity in actionList:
    currQuantity = 5
    activityQuantity = int(activity[1])
    newQuantity = currQuantity + activityQuantity
    if(activityQuantity>0):
        _Products.update(activity[0], newQuantity)
        _Activities.insert(Activity(*activity))

    elif(activityQuantity < 0):
        if newQuantity >= 0:
            _Products.update(activity[0], newQuantity)
            _Activities.insert(Activity(*activity))




