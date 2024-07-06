#define functions needed (sub,add,mul,div)
#print options to the user
#ask for values
#call the functions
#while loop to continue until user exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")

    choice = input("input ur choice \n")

    if choice =="a" or choice =="A":
        print ("Addition")
        a = int(input("enter first number \n"))
        b = int(input("enter first number \n"))
        add(a,b)

    elif choice =="b" or choice =="B":
        print ("subtration")
        a = int(input("enter first number \n"))
        b = int(input("enter first number \n"))
        sub(a,b)

    elif choice =="c" or choice =="C":
        print ("multiplication")
        a = int(input("enter first number \n"))
        b = int(input("enter first number \n"))
        mul(a,b)

    elif choice =="d" or choice =="D":
        print ("division")
        a = int(input("enter first number \n"))
        b = int(input("enter first number \n"))
        div(a,b)

    elif choice =="e" or choice =="E":
        print ("terminated")
        quit()
