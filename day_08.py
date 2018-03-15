#  HackerRank: 30 Days of Code - Day 8: Dictionaries and Maps
#  
#  Task
#
#  Given n names and phone numbers, assemble a phone book that maps
#  friends' names to their respective phone numbers. You will then be
#  given an unknown number of names to query your phone book for. For
#  each name queried, print the associated entry from your phone book
#  on a new line in the form name=phoneNumber; if an entry for name is
#  not found, print Not found instead. 

import sys


if __name__ == "__main__":
    n = int(input().strip())
    phone_book = {}
    for i in range(n):
        line_items = input().strip().split()
        phone_book[line_items[0]] = line_items[1]

    name = input().strip()
    while name:
        if name in phone_book:
            print("{0}={1}".format(name, phone_book[name]))
        else:
            print("Not found")
        name = input().strip()
