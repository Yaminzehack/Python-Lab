## A program that calculates the average of a list of numbers
numbers = [1,2,3,4,5]
if not numbers:
    print("List is empty. Cannot calculate average .")
else:
    avg = sum(numbers) / len(numbers)
    a = (f"The average of the numbers is: {avg}")
    print(a)
    fh = open("output4.txt","a")
    fh.write( str(a) + "\n")
    fh.close()