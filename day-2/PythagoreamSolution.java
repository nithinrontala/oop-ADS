import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        float a = sc.nextFloat();
        float b = sc.nextFloat();
        double c = Math.sqrt(a*a + b*b);
        System.out.println(c);
        
        sc.close();
    }

}
