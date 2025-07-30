import java.util.HashMap;

public class SubArraySum {
    public int subarraySum(int[] nums, int k) {
        int count = 0, prefixSum = 0;
        HashMap<Integer, Integer> sumMap = new HashMap<>();
        sumMap.put(0, 1);

        for (int num : nums) {
            prefixSum += num;
            if (sumMap.containsKey(prefixSum - k)) {
                count += sumMap.get(prefixSum - k);
            }
            sumMap.put(prefixSum, sumMap.getOrDefault(prefixSum, 0) + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        SubArraySum sol = new SubArraySum();
        int[] nums = {1, 1, 1};
        int k = 2;
        System.out.println("Count: " + sol.subarraySum(nums, k));
    }
}
