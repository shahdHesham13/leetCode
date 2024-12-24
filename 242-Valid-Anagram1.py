class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     slet = {}
     tlet = {}
     for char in s:
       slet[char]=slet.get(char,0)+1

     for char in t:
        tlet[char]=tlet.get(char,0)+1


     return slet==tlet
     
