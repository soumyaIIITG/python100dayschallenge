def Calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8
Calculategmean(a,b)
c=9
f=78
Calculategmean(c,f)

print("The next program starts here")

def isGreater(a,b):
    if (a>b):
        print("First no. is greater than second")
    else:
        print("Second no is greater than first")
first=int(input("Enter the first no.:"))
second=int(input("Enter the second no.:"))
isGreater(first,second)