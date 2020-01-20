
from DAOs import _CoffeeStands,_Activities,_Employees,_Products,_Suppliers
from DTOs import *
from repository import repo
import os
dbExist = os.path.isfile('moncafe.db')
if dbExist:
    os.remove('moncafe.db')
repo.create_tables()
file = open('config.txt','r')
f = file.readlines()
parseList = []

for line in f:
    if line[-1]=='\n':
        line = line[:-1]
    parseList.append(line.split(', '))

# print(parseList)
for line in parseList:
    if  line[0]=='C':
        print(*line[1:])
        repo.CoffeeStands.insert(CoffeeStand(*line[1:]))
    elif line[0] == 'S':
        repo.Suppliers.insert(Supplier(*line[1:]))
    elif line[0] == 'E':
        repo.Employees.insert(Employee(*line[1:])) #TODO:check if this works
    elif line[0] == 'P':
        repo.Products.insert(Product(*line[1:]))
























