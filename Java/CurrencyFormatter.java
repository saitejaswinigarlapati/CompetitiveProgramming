/*
Given a double-precision number, 'payment' , denoting an amount of money, use the NumberFormat class' getCurrencyInstance method to convert 'payment' into the US, Indian, Chinese, and French currency formats. Then print the formatted values as follows:

US: formattedPayment
India: formattedPayment
China: formattedPayment
France: formattedPayment

Sample Input : 12324.134
Sample Output :
US: $12,324.13
India: Rs.12,324.13
China: ￥12,324.13
France: 12 324,13 €
*/

import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class CurrencyFormatter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Payment : ");
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat usF = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat indiaF = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        NumberFormat chinaF = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat franceF = NumberFormat.getCurrencyInstance(Locale.FRANCE);

        String us = usF.format(payment);
        String india = indiaF.format(payment);
        String china = chinaF.format(payment);
        String france = franceF.format(payment);

        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
