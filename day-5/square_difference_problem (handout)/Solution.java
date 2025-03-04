import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        long num = sc.nextLong();
        sc.close();
        System.out.println(Difference(num));
    }
    public static long squareSumOfNaturalNum(long num){
        long sum = 0;
        for (long i = num; i>0;i--){
            sum+=i;
        }
    return sum*sum;
    }
    public static long sumOfSquares(long num){
        long sumOfSquare = 0;
        for(long i = num;i>0;i--){
            sumOfSquare+=i*i;
        }
    return sumOfSquare;
    }
    public static long Difference(long num){
        return squareSumOfNaturalNum(num) - sumOfSquares(num);
    }
}