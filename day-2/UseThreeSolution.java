import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String n1 = sc.next();
        String n2 = sc.next();
        String n3 = sc.next();
        String out = "Hi " + n3 + ", " + n2 + ", and " + n1 + ".";

        System.out.println(out);

        sc.close();
    }

}
