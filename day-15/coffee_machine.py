from art import coffee_cup
from data import coffee_types,machine_resources,coffee_type_data

SHUTDOWN_COMMAND ="off"
REPORT_COMMAND = "report"

print(coffee_cup)
coffee_machine_status_on = True

profit = 0

def print_status_report(machine,header,profit):
    print(f'''
    ------------------------
    **** Machine Status : {header}****
    ------------------------
    ''')
    print(f"Water : {machine['water']}ml ")
    print(f"Milk : {machine['milk']}ml ")
    print(f"Coffee : {machine['coffee']}g ")
    print(f"Money : {profit} ")

def check_resource_sufficient(coffee_type,inventory):
    for item in inventory:
        if inventory[item] - coffee_type_data[coffee_type]['ingredients'][item] < 0:
            print(f"Sorry there is no enough {item}")
            return False

    return True

def collect_money():
    quarters = int(input("enter the quarters: "))
    dimes = int(input("enter the dimes: "))
    nickels= int(input("enter the nickels: "))
    pennies = int(input("enter the pennies: "))
    total_value_in_dollars = round((quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01),2)
    print(f" Total Value in ${total_value_in_dollars}")
    return total_value_in_dollars

def deduct_from_inventory(coffee_data,machine):
    machine['water']-=coffee_data['water']
    machine['milk'] -= coffee_data['milk']
    machine['coffee'] -= coffee_data['coffee']


def collect_and_process(coffee_type,coffee_data,machine):
    global profit
    payment = collect_money()
    refund = 0
    money_collected = 0
    coffee_charge = coffee_data['money']

    if coffee_charge > payment:
        print("Sorry that's not enough money. Money refunded.")
        return

    if coffee_charge < payment:
        refund = payment - coffee_charge
        refund = round(refund,2)
        money_collected = round(payment - refund, 2)
        print(f"Here is the ${refund} in change")
    else:
        money_collected = payment

    print(f"\n\n {money_collected} \n\n")

    print_status_report(machine," Report before purchasing :"+coffee_type,profit)
    profit += money_collected
    deduct_from_inventory(coffee_data['ingredients'],machine)
    print_status_report(machine," Report after purchasing :"+coffee_type,profit)
    print(f"Here is your {coffee_type}. Enjoy!")

while coffee_machine_status_on:
    user_choice = input(f"What would you like ? {coffee_types} :").lower()
    if user_choice == 'off':
        coffee_machine_status_on = False
    elif user_choice=='report':
        print_status_report(machine_resources,'Report')
    else:
        check_resource_sufficient(user_choice,machine_resources)
        collect_and_process(user_choice,coffee_type_data[user_choice],machine_resources)
