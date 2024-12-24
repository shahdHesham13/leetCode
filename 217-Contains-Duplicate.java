class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<>();
        for(int n : nums){
            if (hashSet.contains(n)) {
                return true;
            } 
            else {hashSet.add(n);}
        }
        return false;
    }
}