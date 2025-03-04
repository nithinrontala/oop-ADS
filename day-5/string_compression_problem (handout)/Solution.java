// import java.util.*;
// public class Solution {

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         String s = sc.nextLine();
//         sc.close();
//         System.out.println(compressString(s));
//     }
//     public static String compressString(String s) {
//         String compressed = "";
//         int count = 1;

//         for (int i = 1; i < s.length(); i++) {
//             if (s.charAt(i) == s.charAt(i - 1)) {
//                 count++;
//             } else {
//                 compressed+=s.charAt(i - 1);
//                 if (count > 1) {
//                     compressed+=""+count;
//                 }
//                 count = 1;
//             }
//         }

//         compressed+=s.charAt(s.length() - 1);
//         if (count > 1) {
//             compressed+=""+count;
//         }

//         return compressed.toString();
//     }
// }

// import java.util.Arrays;

// public class Solution {

//     public static void main(String[] args) {
         
//         int [] arr = {1,2,3,4};
//         int []arr2 = {1,2};
//         System.out.println(Arrays.toString(arr));
//         for (int j = 0;j<arr.length;j++){
//             int temp = arr[0];

//             for(int i  = 0;i<arr.length-1;i++){
//                 arr[i] = arr[i+1];
//             }
//             arr[arr.length-1] = temp;
//             System.out.println((Arrays.toString(arr)));
//         }
//     }
// }

// public class Solution {

//     public static void main(String[] args) {
//         String str1= new String("hello");
//         String s2 = " hlll".trim();
//         System.out.println(s2);
//         System.out.println(str1.contains(s2));

//     }
// }