class Solution(object):
    def calPoints(self, operations):
       stack = []
       for c in operations:
         if c == 'C':
            stack.pop()
         elif c == 'D':
            stack.append(2*stack[-1])
         elif c == '+':
            stack.append(stack[-2]+stack[-1])
         else:
            stack.append(int(c))

       return sum(stack)


        