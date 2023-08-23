# Write a program to print the fibonacci series
a=0
b=1
n=int(input("Enter the term till which you want to take input:"))
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c = a+b
    a = b
    b = c
    print(c,end=" ")

#Same program using recursion
def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))

length = int(input("Enter number of terms:"))

print("Fibonacci sequence using Recursion :")
for iter in range(length):
    print(gen_seq(iter))


