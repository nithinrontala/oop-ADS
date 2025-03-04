import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String Time = sc.nextLine();
        Time_Conversion(Time);
        sc.close();
    }
    public static void Time_Conversion(String Time){
        String[] time = Time.split(":");
        String hours = time[0];
        String minutes = time[1];
        String sec = time[2].substring(0,2);
        String period = time[2].substring(2,4);
        if (period.equals("PM") && !hours.equals("12")){
            hours = String.valueOf(Integer.parseInt(hours)+12);
        }
        if (period.equals("AM") && hours.equals("12")){
            hours = "00";
            
        }
        System.out.printf("%s:%s:%s",hours,minutes,sec);
    }
}
