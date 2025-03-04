import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        sc.close();
        System.out.println(PrimeNum(num));
    }
    public static String PrimeNum(int num){
        if(num<=1){
            return "False";
        }
        else if(num == 2){
            return "True";
        }
        else{
            for(int i=2;i<num;i++){
                if(num%i == 0){
                    return "False";
                }
        }
    }
    return "True";
}
}