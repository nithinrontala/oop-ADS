import java.util.Scanner;

public class Solution {
    public static void main(String[] bk){
        Scanner sc = new Scanner(System.in);

        double pi = 3.14159;
        float r = sc.nextFloat();
        double Area = pi * (r*r);
        System.out.printf("%.2f%n",Area);

        sc.close();
    }

}