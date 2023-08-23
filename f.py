import math

def calculate_f(N):
    num_squares = int(math.sqrt(N))
    num_cubes = int(N**(1/3))
    return num_squares - num_cubes

t = int(input())
for i in range(t):
    x = int(input())
    low = 1
    high = x**3
    while low < high:
        mid = (low + high) // 2
        f_mid = calculate_f(mid)
        if f_mid >= x:
            high = mid
        else:
            low = mid + 1
    print(low)