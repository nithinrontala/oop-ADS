import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int angle = sc.nextInt();
        sc.close();
        ClassifyAngle(angle);
    }
    public static void ClassifyAngle(int angle){
        if(angle>0 && angle <90){
            System.out.println("Acute");
        }
        else if(angle == 90){
            System.out.println("Right");
        }
        else if(angle>90 && angle<180){
            System.out.println("Obtuse");
        }
        else{
            System.out.println("Invalid");
        }
    }
}