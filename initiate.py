import repository
from DAOs import _CoffeeStands,_Activities,_Employees,_Products,_Suppliers
from DTOs import *
from repository import repo


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
        cf = CoffeeStand(*line[1:])
        _CoffeeStands.insert(cf)
    elif line[0] == 'S':
        _Suppliers.insert(Supplier(*line[1:]))
    elif line[0] == 'E':
        #_Employees.insert(Employee(line[1],line[2],line[3],line[3]))
        _Employees.insert(Employee(*line[1:])) #TODO:check if this works
    elif line[0] == 'P':
        _Products.insert(Product(*line[1:]))
























