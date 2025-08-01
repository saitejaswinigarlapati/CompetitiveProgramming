import java.util.Scanner;

public class PascalTriangle {
    public static void printPascalTriangle(int numRows) {
        for (int i = 0; i < numRows; i++) {
            for (int space = 0; space < numRows - i - 1; space++) {
                System.out.print(" ");
            }

            int value = 1;
            for (int j = 0; j <= i; j++) {
                System.out.print(value + " ");
                value = value * (i - j) / (j + 1);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();

        printPascalTriangle(rows);
    }
}
