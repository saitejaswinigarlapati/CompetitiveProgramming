public class PerfectNumber {

    public static boolean isPerfectNumber(int n) {
        if (n <= 1) return false;

        int sum = 1; // 1 is always a divisor
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                sum += i;
                if (i != n / i) {
                    sum += n / i;
                }
            }
        }
        return sum == n;
    }

    public static void main(String[] args) {
        int[] numbers = {6, 28, 12, 496, 97};
        for (int num : numbers) {
            System.out.println(num + ": " + (isPerfectNumber(num) ? "Perfect Number" : "Not a Perfect Number"));
        }
    }
}
