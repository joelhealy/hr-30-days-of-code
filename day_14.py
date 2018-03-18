#  HackerRank: 30 Days of Code - Day 14: Scope

class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
        max_diff = -1
        n = len(self.__elements)
        for i in range(n-1):
            for j in range(i+1, n):
                ij_diff = abs(self.__elements[i] - self.__elements[j])
                if ij_diff > max_diff:
                    max_diff = ij_diff
        self.maximumDifference = max_diff


    def computeDifference(self):
        return self.maximumDifference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
