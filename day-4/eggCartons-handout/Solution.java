import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inches = sc.nextInt();
        sc.close();
        Fabric_Yard(inches);
    }

    public static void Fabric_Yard(int inches) {
        int out = (int) Math.ceil((double) inches / 12);
        System.out.println(out);
    }
}
