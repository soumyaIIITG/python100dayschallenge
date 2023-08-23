marks = [3,4,5,6,"Soumya",True]
print(marks)
print(len(marks))
print(marks[4])

if 7 in marks:
    print("Yes")
else:
    print("No")
if "Soumya" in marks:
    print("Yes")
else:
    print("No")

print("The next program starts here")
lst = [i for i in range(5)]
print(lst)
lst = [i*3 for i in range(6)]
print(lst)