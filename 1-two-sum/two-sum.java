class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> lookup = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (lookup.containsKey(comp)) {
                int[] result = new int[]{lookup.get(comp), i};
                return result;
            }
            lookup.put(nums[i], i);
        } 
        return null;
    }
}