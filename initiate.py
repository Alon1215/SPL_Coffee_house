import REPOSITORY
from DAOs import _CoffeeStands,_Activities,_Employees,_Products,_Suppliers
from DTOs import *
from REPOSITORY import repo

file = open('config.txt', 'r')
f = file.readlines()
parseList = []

for line in f:
    if line[-1]=='\n':
        line = line[:-1]

    l = line.split(', ')
    parseList.append(l)

print(parseList)

for line in parseList:
    if(line[0]=='C'):
        _CoffeeStands.insert(CoffeeStand())



    elif line[0] == 'S':

    elif line[0] == 'E':
        #_Employees.insert(Employee(line[1],line[2],line[3],line[3]))
        _Employees.insert(Employee(*line[1:]))
    elif line[0] == 'F':
























