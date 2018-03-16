#  HackerRank: 30 Days of Code - Day 11: 2D Arrays
#  
#  Given a 6 x 6 Array, A:
#
#    1 1 1 0 0 0
#    0 1 0 0 0 0
#    1 1 1 0 0 0
#    0 0 0 0 0 0
#    0 0 0 0 0 0
#    0 0 0 0 0 0
#
#  We define an hourglass in A to be a subset of values with indices
#  falling in this pattern in A's graphical representation:
#
#    a b c
#      d
#    e f g
#
#  There are 16 hourglasses in A, and an hourglass sum is the sum of an
#  hourglass' values.
#
#  Task
#
#  Calculate the hourglass sum for every hourglass in A, then print the
#  maximum hourglass sum.


import sys


def hourglass_sum(arr, i, j):
    retval = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
             arr[i+1][j+1] + \
             arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    return retval


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max_hourglass_sum = hourglass_sum(arr, 0, 0)
for i in range(4):
    for j in range(4):
        hgs = hourglass_sum(arr, i, j)
        if hgs > max_hourglass_sum:
            max_hourglass_sum = hgs

print(max_hourglass_sum)


