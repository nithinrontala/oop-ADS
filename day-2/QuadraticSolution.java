import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double X1 = (-b + Math.sqrt((b*b)-4*c))/2;
        double X2 = (-b - Math.sqrt((b*b)-4*c))/2;
        System.out.println(X1);
        System.out.println(X2);

        sc.close();
    }

}
