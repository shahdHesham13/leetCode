class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

     mini = min(len(str1), len(str2))
            
     for length in range(mini, 0, -1):
        if len(str1) % length == 0 and len(str2) % length == 0:
            candidate = str1[:length]
            
            if str1 == candidate * (len(str1) // length) and str2 == candidate * (len(str2) // length):
                return candidate
            
     return ""