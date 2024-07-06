calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):

        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    

def validate_and_execute():
    try:
        userInputNumber = int(days_and_unit_dict["days"])
        if userInputNumber > 0:
            calculatedValue = days_to_units(userInputNumber)
            print(calculatedValue)
        elif userInputNumber ==0:
            print("u ented zero")
        else:
             print("u entered a negative number, enter a correct number")
    except ValueError:
        print("ue input is not a nmber nigga")

userInput = ""
while userInput != "exit":
    userInput = input("enter a number of days my nigga and conversion unit \n")
    days_and_unit = userInput.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": "hours"}
    print((days_and_unit_dict))
    validate_and_execute

my_list = ["20","30"]
print(my_list)

my_dictionary = {"days":20, "unit": "hours"}
print(my_dictionary["days"])

