print("Welcome to the Python pizza deliveries!")
size = input("What size pizza do you want? S, M or L:?")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")

pizza_cost = 0;
if size == 'S':
    pizza_cost = 15
    if pepperoni == 'Y':
        pizza_cost+= 2
elif size == 'M':
    pizza_cost = 20
    if pepperoni == 'Y':
        pizza_cost+= 3
elif size == 'L':
    pizza_cost =  25
    if pepperoni == 'Y':
        pizza_cost+= 3
else:
    print("You typed the wrong inputs.")
if extra_cheese == 'Y':
    pizza_cost+= 1

print(f"Your final bill is: {pizza_cost}");