public class Solution {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        System.out.println(nthHappyPrime(n));
    }

    public static boolean isPrime(int n) {
        if(n<=1){
            return false;
        }
        else if(n == 2){
            return true;
        }
        else{
            for(int i=2;i<n;i++){
                if(n%i == 0){
                    return false;
                }
        }
    }
    return true;
}

    public static int sumOfSquares(int n) {
        int t = 0;
        while (n > 0) {
            int rem = n % 10;
            t += rem * rem;
            n = n / 10;
        }
        return t;
    }

    public static boolean isHappy(int n) {
        boolean[] seen = new boolean[1000];
        while (n != 1) {
            if (seen[n]) {
                return false;
            }
            seen[n] = true;
            n = sumOfSquares(n);
        }
        return true;
    }

    public static boolean isHappyPrime(int n) {
        return isHappy(n) && isPrime(n);
    }

    public static int nthHappyPrime(int n) {
        int count = 0;
        int num = 7;
        while (count <= n) {
            if (isHappyPrime(num)) {
                if (count == n) {
                    return num;
                }
                count++;
            }
            num++;
        }
        return -1;
    }

}
