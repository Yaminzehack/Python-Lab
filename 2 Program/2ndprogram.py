# 2. A program that calculates the area and perimeter of a rectangle.
l=int(input("enter length:"))
w=int(input("enter width:"))
area=l*w
perimeter=2*(l+w)
print("area of rectangle is: ",area)
print("perimeter of rectangle is:",perimeter)
fh = open("output2.txt","a")
fh.write("area of rectangle is:" + str(area)+"\n")
fh.write("perimeter of rectangle is:" + str(perimeter)+"\n")
fh.close()