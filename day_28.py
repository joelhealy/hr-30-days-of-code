import sys
import re

p = re.compile(".+@gmail\.com$")
first_name_list = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if p.match(emailID):
        first_name_list.append(firstName)
first_name_list.sort()
for first_name in first_name_list:
    print(first_name)
