from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeMaker = CoffeeMaker()
menu = Menu()

moneyMachine.report()
coffeMaker.report()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"{options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                coffeMaker.make_coffee(drink)

