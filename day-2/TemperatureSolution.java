import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        float F = sc.nextFloat();
        double C = (5.0/9.0)*(F-32);
        System.out.printf("%.1f%n",C);

        sc.close();
    }

}
