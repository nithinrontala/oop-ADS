import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int Area = 2*(a*a)+2*(b*b);
        System.out.printf("%d",Area);

        sc.close();
    }

}
