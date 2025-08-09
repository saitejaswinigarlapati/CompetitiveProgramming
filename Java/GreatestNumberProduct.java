import java.util.HashSet;
import java.util.Set;

public class GreatestNumberProduct {
    public int greatest_product_equal_to_element(int[] arr) {
        int max_product = -1;

        // Add all elements of arr to the set
        Set<Integer> arr_set = new HashSet<>();
        for (int num : arr) {
            arr_set.add(num);
        }

        // Check all pairs
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (i != j) {
                    int product = arr[i] * arr[j];
                    if (arr_set.contains(product)) {
                        max_product = Math.max(max_product, product);
                    }
                }
            }
        }

        return max_product;
    }

    public static void main(String[] args) {
        GreatestNumberProduct obj = new GreatestNumberProduct();
        int[] arr = {2, 3, 4, 6, 12};
        int result = obj.greatest_product_equal_to_element(arr);
        System.out.println(result);
    }
}

// Input: ARR = [1, 2, 3, 6, 12]
// Output: 12
 
// Input: ARR = [4, 2, 3, 8]
// Output: 8
