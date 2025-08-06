import java.util.Scanner;

public class BuildPalindrome {
    public static boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }

    public static String buildPalindrome(String s) {
        for (int i = 0; i < s.length(); i++) {
            String suffix = s.substring(i);
            if (isPalindrome(suffix)) {
                StringBuilder prefix = new StringBuilder(s.substring(0, i));
                return s + prefix.reverse().toString();
            }
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter string :");
        String s = sc.nextLine();
        System.out.println(buildPalindrome(s));
    }
}

// Input : abc
// Output : abcba

// Intput :race
// Output :racecar