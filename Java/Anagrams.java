import java.util.Arrays;
import java.util.Scanner;
public class Anagrams {
    static boolean isAnagram(String a, String b) {

        a = a.replaceAll("\\s", "").toLowerCase();
        b = b.replaceAll("\\s", "").toLowerCase();

        if (a.length() != b.length()) {
            return false;
        }

        char[] aArray = a.toCharArray();
        char[] bArray = b.toCharArray();
        Arrays.sort(aArray);
        Arrays.sort(bArray);

        return Arrays.equals(aArray, bArray);
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("First string: ");
        String a = scan.nextLine();
        System.out.print("Second string: ");
        String b = scan.nextLine();
        scan.close();

        boolean result = isAnagram(a, b);
        System.out.println(result ? "Anagrams" : "Not Anagrams");
    }
}
