class Solution(object):
    def makeGood(self, s):
     stack = []
     for c in s:
        if stack and (ord(stack[-1]) - ord(c) == 32 or ord(c) - ord(stack[-1]) == 32 ):
                stack.pop()
        else:
                stack.append(c)
     return "".join(stack)

        