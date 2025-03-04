import java.util.Scanner;

public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Boolean a = sc.nextBoolean();
        Boolean b = sc.nextBoolean();
        Boolean c = sc.nextBoolean();
        sc.close();
        if ((a == true && b == true && c == true) || (a == true && c == true) || ((b == true && (a == true || c == true)))){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}