def is_leap_year(year):
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 ==0:
                 print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("LEAP YEAR")
    else:
        print("not a leap year")



is_leap_year(2023)