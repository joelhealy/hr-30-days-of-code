#  HackerRank: 30 Days of Code - Day 16: Exceptions - String to Integer
#
#  Task 
#  
#  Read a string, S, and print its integer value; if S cannot be
#  converted to an integer, print Bad String.

import sys

S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")
