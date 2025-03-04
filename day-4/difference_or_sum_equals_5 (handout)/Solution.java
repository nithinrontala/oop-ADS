import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        sc.close();
        Difference_Sum(x, y);
    }
    public static void Difference_Sum(int x, int y){
        int a = x-y;
        int sum = x+y;
        if(Math.abs(a)== 5 || sum ==5){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    } 
}