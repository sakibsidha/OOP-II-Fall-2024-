def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
Year = int(input("Enter the number: "))  
# Printing result  
if(is_leap_year(Year)):
    print("Leap Year")
else:
    print("Not a leap year")  