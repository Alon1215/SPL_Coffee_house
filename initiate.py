from DTOs import *
from repository import repo
import sys

def main():

    repo.create_tables()
    file = open(sys.argv[1], 'r')
    f = file.readlines()
    parse_list = []

    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        parse_list.append(line.split(', '))

    #print(parse_list)
    for line in parse_list:
        if line[0] == 'C':
            repo.CoffeeStands.insert(CoffeeStand(*line[1:]))
        elif line[0] == 'S':
            repo.Suppliers.insert(Supplier(*line[1:]))
        elif line[0] == 'E':
            repo.Employees.insert(Employee(*line[1:]))
        elif line[0] == 'P':
            repo.Products.insert(Product(*line[1:], 0))


if __name__ == '__main__':
    main()






















