## a program that calculates the factorial of a number
sum = 1
i = 1
n = int(input("Enter a value to find factorial: "))
while i<=n:
    sum=sum*i
    i=i+1
print(f"Factorial of {n} is {sum} ") 
fh = open("output6.txt","a")
fh.write(f"Factorial of {n} is {sum}\n")
fh.close()
    