## A program that checks if a given string is a palindrome.
a = input("Enter a Number or String to check palindrome number: ")
b = a[::-1]
if(a==b):
    c = (f"{a} is a palindrome.")
    print(c)
else:
    c = (f"{a} is not a palindrome.")
    print(c)
fh = open("output7.txt","a")
fh.write(c+"\n")
fh.close()