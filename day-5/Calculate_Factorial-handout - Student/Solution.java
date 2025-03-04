import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        scan.close();
        Factorial(num);
    }
    public static void Factorial(int num){
        int fact = 1;
        for(int i=num;i>0;i--){
            fact*=i;
        }
        System.out.println(fact);
    }
}