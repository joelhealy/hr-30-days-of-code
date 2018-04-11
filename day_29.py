import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    if k < 6:
        max_a_and_b = 0
        for a in range(1,n+1):
            for b in range(a+1,n+1):
                cur = a & b
                if cur > max_a_and_b and cur < k:
                    max_a_and_b = cur
        print(max_a_and_b)
    elif k % 16 == 0:
        print(k-2)
    else:
        print(k-1)

