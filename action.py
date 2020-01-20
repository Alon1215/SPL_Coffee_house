import repository
from DAOs import _CoffeeStands,_Activities,_Employees,_Products,_Suppliers
from DTOs import *
from repository import repo

file = open('action.txt', 'r')
f = file.readlines()
activityList = []

for line in f:
    if line[-1]=='\n':
        line = line[:-1]
    activityList.append(line.split(', '))

#print(activityList)

for activity in activityList:
    currQuantity = repo.Products.get_quantity(activity[0])
    activityQuantity = int(activity[1])
    newQuantity = currQuantity + activityQuantity
    if activityQuantity>0:
        repo.Products.update_quantity(activity[0], newQuantity)
        repo.Activities.insert(Activity(*activity))

    elif activityQuantity < 0 and newQuantity >= 0:
            repo.Products.update_quantity(activity[0], newQuantity)
            repo.Activities.insert(Activity(*activity))




