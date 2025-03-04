import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        sc.close();
        longestWord(word);
    }

    public static void longestWord(String word) {
        String[] words = word.split(" ");
        String longest = "";
        int maxLength = 0;

        for (String w : words) {
            if (w.length() >= maxLength) {
                maxLength = w.length();
                longest = w;
            }
        }

        System.out.println(longest);
    }

    public static void Count(String word) {
        String[] words = word.split(" ");
        System.out.println(words.length);
    }
}
