## A program that checks if a given year is a leap year
year = int(input("Enter a year to check if it's a leap year: "))
leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if leap_year:
    a=(f"{year} is a leap year.")
    print(a)
else:
    a=(f"{year} is not a leap year.")
    print(a)
fh=open('output5.txt','a')
fh.write(str(a)+'\n')
fh.close()