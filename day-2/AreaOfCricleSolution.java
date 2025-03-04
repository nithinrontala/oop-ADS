import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a = sc.nextFloat();
        float pi = 3.14159f;
        float ar = pi * (float) a*a;
        System.out.printf("%.2f\n", ar);
        sc.close();
    }
}
