#  HackerRank: 30 Days of Code - Day 10: Binary Numbers
#  
#  Task
#
#  Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.import sys


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
