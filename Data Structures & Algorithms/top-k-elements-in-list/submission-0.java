class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //hashmap of int and counter 
        //for loop for nums 
        //if map does not contain
        //add it 
        //if it does add one
        HashMap<Integer,Integer> map = new HashMap<>(); 
        for(int i = 0; i < nums.length; i++){
            if(!map.containsKey(nums[i])){
                //add if nums is not in the 
                map.put(nums[i],1);
            }
            else{
            map.put(nums[i],map.get(nums[i])+1);
            }
        } 
        //bucket sort  
        //create bucket 
        List<Integer>[] bucket = new ArrayList[nums.length+1]; 
        for(int i = 0; i< bucket.length; i++){
            bucket[i] = new ArrayList<>();//initialize the bucket
        }

        //putting numbers in the buckets 
        for(int num : map.keySet()){
            int freq = map.get(num);
            bucket[freq].add(num);
        } 

        //Reading the buckets from high to low
        int [] ans = new int[k];//the size 
        int idx = 0; 
        for(int freq = bucket.length - 1; freq >= 0 && idx < k; freq--){
            for (int num : bucket[freq]){
                ans[idx++] = num; 
                if (idx == k) break;
            }
        }

        return ans;
    }
}
