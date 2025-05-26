from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_running = True
coffer_make = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
while machine_is_running:
    user_choice = input(f"what would you like? {menu.get_items()}")
    if user_choice == 'off':
        machine_is_running = False
    elif user_choice == 'report':
        coffer_make.report()
        money_machine.report()
    else:
        coffee_type = menu.find_drink(user_choice)

        if coffee_type and coffer_make.is_resource_sufficient(coffee_type):

            if money_machine.make_payment(coffee_type.cost):
                coffer_make.report()
                coffer_make.make_coffee(coffee_type)
                coffer_make.report()


