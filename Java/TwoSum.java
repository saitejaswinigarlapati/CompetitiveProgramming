import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pair_index = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            if (pair_index.containsKey(target - num)) {
                return new int[] { i, pair_index.get(target - num) };
            }

            pair_index.put(num, i);
        }

        return new int[] {};
    }
}

public class TwoSum {
    public static void main(String[] args) {
        Solution obj = new Solution();

        int[] nums = {2, 7, 11, 15};
        int target = 9;

        int[] result = obj.twoSum(nums, target);

        System.out.println("Output indices: " + Arrays.toString(result));
    }
}
