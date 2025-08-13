import java.util.Scanner;

public class powerOfTwo {
    public boolean isPowerOfTwo(int n) {
        if(n <= 0){
            return false;
        }
        while(n%2==0){
            n/=2;
        }
        return n==1;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        powerOfTwo obj=new powerOfTwo();
        System.out.print("n : ");
        int n=sc.nextInt();
        System.out.print(n + " is power of 2 : "+obj.isPowerOfTwo(n) );
        sc.close();
    }
}