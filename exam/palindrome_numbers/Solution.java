import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long l = sc.nextLong();
        long r = sc.nextLong();
        sc.close(); 
        rangeOfNum(l, r);
    }

    public static String Palindrome(long number) {
        String s = Long.toString(number);
        char c;
        String s1 ="";
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
        
            s1 = c + s1; 
      }
    
      return s1;
  } 
  public static boolean isPalindrome(long number){
    String s1 = Long.toString(number);
    return s1.equals(Palindrome(number));
  }
  public static void rangeOfNum(long l, long r){
    for(long i= l ;i<= r;i++){
        if (isPalindrome(i)){
            System.out.print(i+" ");
        }
    
    }
    // System.out.print(" ");
  }   
}