# HackerRank: 30 Days of Code - Day 5: Loops

import sys


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(0, 10):
        i = i + 1
        print(n, "x", i, "=", n*i)

