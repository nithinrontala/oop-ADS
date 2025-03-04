import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int p = sc.nextInt();
        double r = sc.nextDouble();
        int t = sc.nextInt();
        sc.close();
        CompoundIntrest(p,r,t);
    }
    public static void CompoundIntrest(int p, double r, int t) {
        double a = p*Math.pow((1+r/100),t)-p;
        System.out.printf("%.2f\n",a);
    }
}