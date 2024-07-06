calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):

        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    

def validate_and_execute():
    try:
        userInputNumber = int(num_of_days_element)
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
    userInput = input("enter a number of days my nigga, separate by commas \n")
    list_of_days = userInput.split(",")
    print()
    print(set(userInput.split(",")))

    print(type(list_of_days))
    print(type(set(list_of_days)))
    
    for num_of_days_element in set(userInput.split(",")):
        validate_and_execute()

