## A program that sorts a list of numbers in ascending or decending order.
a = [1,5,4,66,55,65,77,96,91,99]
print("Before sort")
print(a)
print("After ascending sort")
a.sort()
print(a)
print("After reverse or descending sort")
a.sort(reverse=True)
print(a)
fh = open("output8.txt","a")
fh.write("After ascending sort\n"+ str(a) + "\n")
fh.write("After reverse or descending sort\n" + str(a) + "\n")
fh.write("After reverse or descending sort\n"+ str(a) + "\n")
fh.close()