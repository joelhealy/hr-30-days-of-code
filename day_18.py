import sys

class Solution:
    # Write your code here
    def __init__(self):
        self._queue = ""
        self._stack = ""
        
        
    def pushCharacter(self, char):
        self._stack = self._stack + char
        return None
    
    
    def enqueueCharacter(self, char):
        self._queue = self._queue + char
        return None
    
    
    def popCharacter(self):
        char = self._stack[-1]
        self._stack = self._stack[0:-1]
        return char
    
    
    def dequeueCharacter(self):
        char = self._queue[0]
        self._queue = self._queue[1:]
        return char
    

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to._stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from._stack
dequeue the first character from queue
compare both the characters
'''
for i in range( l // 2 ):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

