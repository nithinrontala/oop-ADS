import java.util.*;
public class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        Frequency(s);
    }
    public static void Frequency(String s){
        String s1 = "";
        int count = 0;
        for (int i = 0; i<s.length()-1;i++){
            if (s.charAt(i) == s.charAt(+1)){
                count+=1;
                s1+=count;
            }
            else if(s.charAt(i)!=s.charAt(i+1)){
                count = 0;
            }

            s1+=count;
            System.out.println(s1);
        }
    }
}