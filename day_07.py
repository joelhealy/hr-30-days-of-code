#  HackerRank: 30 Days of Code - Day 7: Arrays
#  
#  Task
#
#  Given an array, A, of N integers, print A's elements in reverse
#  order as a single line of space-separated numbers.
#  
#  Input Format
#  
#  The first line contains an integer N, (the size of our array).
#  The second line contains N space-separated integers describing array
#  A's elements.

import sys


if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end='')
        print((' ' if i > 0 else ''), end='')
    print()
    
