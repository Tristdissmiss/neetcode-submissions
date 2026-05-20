class Solution {
    public boolean isAnagram(String s, String t) {
        //does key-value pairs follow eachother 
        //hashmap is needed 

        //make the string s the inital key standard 
        //make a loop go thru string t 
        //at the end of loop compare if they have the same key value pair 
        //if they do true 
        //else false  
        if(s.length() != t.length()) return false;

        HashMap<Character, Integer> count = new HashMap<>(); 

        for(char x : s.toCharArray()){ //string s
            count.put(x, count.getOrDefault(x,0)+1);
        }

        for(char x: t.toCharArray()){
            if(!count.containsKey(x)) return false;

            count.put(x, count.get(x)-1); 

            if(count.get(x) < 0) return false;
        } 
        return true;

    }
}
