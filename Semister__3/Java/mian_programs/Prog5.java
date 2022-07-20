import java.util.Arrays;
import java.util.Scanner;

public class Prog5{
    public static void main(String[] args) {
        //Creationg a common scanner
        Scanner input = new Scanner(System.in);

        // Taking input the numbers
        System.out.print("Number 1: ");
        int num1 = input.nextInt();
        System.out.print("Number 2: ");
        int num2 = input.nextInt();
        System.out.print("Number 3: ");
        int num3 = input.nextInt();
        
        // Aranging the number in descending order
        int[] numbers = {num1,num2,num3};
        Arrays.sort(numbers);
        System.out.println("The numbers in descending order are: ");

        for (int i = (numbers.length-1); i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        input.close();
    }
}