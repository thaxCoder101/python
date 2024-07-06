#collect inputs: principal,apr,years

def main():
    print("this is a monthly payment loan calculator")
    print("")

    principal = float(input("enter loan amount : "))
    apr = float(input("enter annual interest rate : "))
    years = int(input("enter amount of years : "))

    monthly_IR = apr / 1200
    months = years * 12
    monthlyPayment = principal * monthly_IR / (1-(1+monthly_IR) **(-months))

    print("the monthly payment for this loan is : %.2f" % monthlyPayment)


main()
    