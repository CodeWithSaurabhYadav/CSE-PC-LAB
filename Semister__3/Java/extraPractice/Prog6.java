import java.util.Scanner;

public class Prog6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter first number: ");
        float num1 = input.nextFloat();
        System.out.print("Enter second number: ");
        float num2 = input.nextFloat();
        System.out.print("Enter third number: ");
        float num3 = input.nextFloat();

        float temp = num1;

        if (num2 > temp) {
            temp = num3;
        } else if (num2 > temp) {
            temp = num2;
        }
        System.out.println("The largest number is: " + temp);

        input.close();
    }
}
