public class LeapYear{
    static boolean checkLeapYear(int year){
        if((year %4==0 && year % 100 != 0 ) || (year%400 ==0)){
            return true;
        }
        return false;
    }
    public static void main(String[] args){
        int[] years={2023,2024,1900,2000};
        for (int year : years) {
            if (checkLeapYear(year)) {
                System.out.println(year + ": Leap Year");
            } else {
                System.out.println(year + ": Not a Leap Year");
            }
        }
    }
}