import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();
        float anual_income = sc.nextFloat();
        int credit_score = sc.nextInt();
        float current_debts = sc.nextFloat();
        sc.close();
        if(age>=25 && age<=65){
            if((anual_income>=50000)&&(credit_score>=700)&&(current_debts< 50000)){
                System.out.println("True");
            }
            else{
                System.out.println("False");
            }
        }
        else if(age<25){
            if ((anual_income>=70000)&&(credit_score>=750)&&(current_debts<30000)){
                System.out.println("True");
            }
            else{
                System.out.println("False");
            }
        }
        else if(age>65){
            if((anual_income>=40000)&&(credit_score>=650)&&(current_debts<=20000)){
                System.out.println("True");
            }
            else{
                System.out.println("False");
            }
        }
            
    }
}
