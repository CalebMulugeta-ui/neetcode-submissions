class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> arr = new HashSet<>();

        for(int i: nums){
            arr.add(i);
        }
 
        if(arr.size() == nums.length){
            return false;
        }
        else{
            return true;
        }
    }
}
