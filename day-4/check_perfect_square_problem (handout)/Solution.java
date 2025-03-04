import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.close();
        System.out.println(PerfectNumber(x));
    }

    public static String PerfectNumber(int x) {
        for (int i = 0; i * i <= x; i++) {
            if (i * i == x) {
                return "True";
            }
        }
        return "False";
    }
}
