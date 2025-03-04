import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age =  sc.nextInt();
        double bmi = sc.nextDouble();
        String healthcon = sc.next();
        sc.close();
        // System.out.println(healthcon);
        if ((age >= 18 && age <=60) && (bmi >= 18.5 && bmi<=24.9) && (healthcon.equals("False")) ||(age <18 && (bmi >=18.5 && bmi <=24.9))||(age>60 &&(bmi>=18.5 && bmi <=24.9) && healthcon.equals("False"))){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}
