class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> hashsetS = new HashMap<>();
        HashMap<Character, Integer> hashsetT = new HashMap<>();
        for (int i = 0; i < s.length(); i++){
          hashsetS.put(s.charAt(i), 1+ hashsetS.getOrDefault(s.charAt(i), 0));
          hashsetT.put(t.charAt(i), 1+ hashsetT.getOrDefault(t.charAt(i), 0));
        }
        for (char c : hashsetS.keySet()) {
          if (!hashsetS.get(c).equals(hashsetT.getOrDefault(c, 0))) {
            return false;
            }
        }
        return true;
    }
}