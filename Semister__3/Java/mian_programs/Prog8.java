import java.util.Arrays;
import java.util.Scanner;

public class Prog8{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        int numbersCount = 10;
        System.out.println("Start entering values from below : ");
        int numbers[] = new int[numbersCount];
        for (int count = 0; count < 10; count++){
            System.out.print((count + 1) +  " >>> ");
            numbers[count] = input.nextInt();
        }

        int reversed[] = new int[numbers.length];
        for (int index = numbersCount-1, indexP = 0; index >= 0 && indexP < numbersCount ; index--, indexP++){
            reversed[indexP] = numbers[index];
        }

        System.out.println("\nThe Reversed numbers are : ");
        System.out.println(Arrays.toString(reversed));

        input.close();
    }
}