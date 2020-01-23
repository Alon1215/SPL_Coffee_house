from repository import repo


def print_activities():
    print("Activities")

    all = repo.Activities.find_all()
    for activity in all:
        print(activity)


def print_coffee_stands():
    print("Coffee stands")

    all = repo.CoffeeStands.find_all()
    for stand in all:
        print(stand)


def print_employees():
    print("Employees")
    all = repo.Employees.find_all()
    for employee in all:
        print(employee)


def print_suppliers():
    print("Suppliers")
    all = repo.Suppliers.find_all()
    for sup in all:
        print(sup)


def print_products():
    print("Products")
    all = repo.Products.find_all()
    for prod in all:
        print(prod)


def print_employees_report():
    print("Employees report")
    all = repo.get_emp_report()
    for item in all:
        total = repo.get_total_income(item[0])
        print("%s %s %s %s" % (item[1], item[2], item[3], total))


def print_activities_report():
    print("Activities")
    all = repo.get_active_report()
    for line in all:
        print(line)


def print_all():
    print_activities()
    print_coffee_stands()
    print_employees()
    print_products()
    print_suppliers()
    print()
    print_employees_report()
    print()
    print_activities_report()


print_all()
