class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       hashSet = set()
       for n in nums:
        if n in hashSet:
            return True
        else: 
            hashSet.add(n)
       return False 
      
