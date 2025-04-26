print("Welcome to the rollercoaster")
height =int(input("What is your height in cm?"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12 :
        bill = 5
        print("You have to pay $5.")
    elif age <= 18:
        bill = 7
        print("You have to pay $7.")
    elif age >=45 and age<=55:
        print("Enjoy the free ride, the bill is on us.")
    else:
        bill = 12
        print("You have to pay $12.")

    rollercoaster_snap_addon = input("Do you want a snap while your having the ride? y for Yes and n for No")
    if rollercoaster_snap_addon:
        bill += 3
        print("You have to pay $3 extra")

    print(f"You have to pay amount: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride")