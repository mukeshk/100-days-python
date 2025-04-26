
def clean_input(input_value):
    input_value= input_value.replace("$","").strip()
    return int(input_value)


print("Welcome to the tip calculator !")

total_bill = clean_input(input("\nWhat was the total bill?"))

tip_in_percentage = clean_input(input("How much tip would you like to give? 10, 12, or 15?"))

no_of_people = int(input("How many people to split the bill?"))

tip_amount = round((total_bill * tip_in_percentage )/ 100,2)

tip_amount_per_person = round(tip_amount/no_of_people,2)

print(f"Each person should pay: ${tip_amount_per_person}")

