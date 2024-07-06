x = int(input("enter three digit number \n"))
a = x%10  #will get the last digit
num = x//10  #get tje first 2 digit
b = num%10  #get the last digit of two digit number
c=num//10 #get first digit of two digit number
print (a+b+c)