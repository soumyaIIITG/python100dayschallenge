def average(*numbers):
    sum = 0;
    for i in numbers:
        sum = sum + i
    print("The average is:",sum/len(numbers))

average(5,6,4,67)
print("The next program starts here")
def average(*numbers):
    sum = 0;
    for i in numbers:
        sum = sum + i
    return (sum/len(numbers))

c = average(5,6,4,67)
print(c)


