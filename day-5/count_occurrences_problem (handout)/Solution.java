import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String first = sc.nextLine();
        String second = sc.nextLine();
        sc.close();
        System.out.println(CountOccurances(first, second));
    }

    public static int CountOccurances(String first, String second) {
        int count = 0;
        // if((first == " ")||(second==" ")){
        //     return 0;
        // }
        for (int i = 0; i <= first.length() - second.length(); i++) {
            if (first.substring(i, i + second.length()).equals(second)) {
                count++;
            }
        }
        return count;
    }
}
