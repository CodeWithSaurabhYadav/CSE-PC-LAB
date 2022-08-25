import java.util.*;

public class Prog6 {
    public static void main(String[] args) {
        
        // Adding the scanner 
        Scanner input = new Scanner(System.in);

        // Making the array of vowels
        String[] array = {"a","e","i","o","u","A","E","I","O","U"};
        System.out.println(Arrays.toString(array));

        // Taking the input from the user and converting it to character
        String charVal = input.next();
        char val = charVal.charAt(0);

        // Checking if the character is a vowel or not
        int count = 0;
        for (int i = 0; i < array.length; i++) {
            char cur = array[i].charAt(0);
            if (val == cur) {
                System.out.println("Vowel");
                break;
            } else {
                count++;
            }
        }
        if (count >= array.length) {
            System.out.println("Consonant");
        }
        input.close();
    }

}
