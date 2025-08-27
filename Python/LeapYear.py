def checkLeapYear(year):
    if(year %4==0 and year%100 !=0) or(year %400 ==0):
        return True
    return False

y=[2023,2024,1900,2000]
for i in y:
    print(f"{i} : {'Leap Year' if checkLeapYear(i) else 'Not a Leap Year'}")