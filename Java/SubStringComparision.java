
//Hacker Rank
/* Given a string, , and an integer, , complete the function so that it finds the lexicographically smallest and largest substrings of length k.

Function Description :
Complete the getSmallestAndLargest function in the editor below.
getSmallestAndLargest has the following parameters:
string s: a string
int k: the length of the substrings to find

Returns
string: the string ' + "\n" + ' where and are the two substrings */


import java.util.Scanner;

public class SubStringComparision {
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest =s.substring(0,k);
        for(int i=1;i<=s.length()-k;i++){
            String substr=s.substring(i,i+k);
            if(substr.compareTo(smallest)<0){
                smallest=substr;
            }if(substr.compareTo(largest)>0){
                largest=substr;
            }
        }

        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("String : ");
        String s = scan.next();
        System.out.print("K : ");
        int k = scan.nextInt();
        scan.close();
        System.out.println(getSmallestAndLargest(s, k));
    }
}

// Input :
// String welcometojava
// K 3

// Output :
// ava
// wel