## A program that generates a multiplication table for a given number.
num=int(input("Enter a Number to find multiplication table: "))
fh=open('output9.txt','a')
fh.write(f"multiplication table of {num}\n")
for i in range(1,11):
    print(num, 'x', i, '=', num*i)
    j=num*i
    fh.write(f"{str(num)} X {str(i)} = {str(j)} \n")
fh.close()