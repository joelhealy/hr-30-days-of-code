# HackerRank: 30 Days of Code - Day 6: Let's Review

import sys


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(0, n):
        input_string = input().strip()
        for j in range(0, len(input_string), 2):
            print(input_string[j], end='')
        print(' ', end='')
        for j in range(1, len(input_string), 2):
            print(input_string[j], end='')
        print()
