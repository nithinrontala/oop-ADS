import java.util.Scanner;

public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        Boolean b = sc.nextBoolean();
        Boolean c = sc.nextBoolean();
        sc.close();
        if ((a >= 18 && b == true)||(c == true)){
            System.out.println("True");
        }
        else{
            System.out.println("False");;
        }
    }
}