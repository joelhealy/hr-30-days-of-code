import math

def is_prime(n):
    if n == 1:
        print("Not prime")
    elif n == 2:
        print("Prime")
    elif n % 2 == 0:
        print("Not prime")
    else:
        i = 3
        factor_max = int(math.sqrt(n))
        while i <= factor_max:
            if n % i == 0:
                print("Not prime")
                return
            i = i + 2
        print("Prime")

t = int(input())
for i in range(t):
    n = int(input())
    is_prime(n)

