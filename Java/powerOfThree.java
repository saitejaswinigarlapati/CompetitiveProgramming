import java.util.Scanner;

public class powerOfThree {
    public boolean isPowerOfThree(int n) {
        if(n<=0){
            return false;
        }
        while(n%3==0){
            n=n/3;
        }
        return n==1;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        powerOfThree obj = new powerOfThree();

        System.out.print("Enter a number : ");
        int n=sc.nextInt();
        System.out.print(n+" is power of 3 " + obj.isPowerOfThree(n));
        sc.close();
    }
}