import java.util.Scanner;

public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean a = sc.nextBoolean();
        boolean b = sc.nextBoolean();
        boolean c = sc.nextBoolean();
        int d = sc.nextInt();
        sc.close();
        if (a == false || b == true && c == true && d > 50){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}