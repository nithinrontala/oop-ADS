import java.util.Scanner;

public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean a = sc.nextBoolean();
        boolean b = sc.nextBoolean();
        boolean c = sc.nextBoolean();
        boolean d = sc.nextBoolean();
        sc.close();
        if ((a == true && d == false )||(b == true && d == false) || (c == true && d == false)){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}