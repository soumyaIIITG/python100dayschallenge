for i in range(15):
    print("5 x",i,"=",5*i)
    if(i==10):
        break
print("Loop ko chor kaar nikal gaya")
print("The next loop starts here")
for i in range(15):
    if (i == 10):
        print("Skips the iteration")
        continue
    print("5 x",i,"=",5*i)
