import java.util.Scanner;

public class Prog2{
    public static void main(String[] args) {

        //Creationg a common scanner
        Scanner input = new Scanner(System.in);
        System.out.println("This is a basic calculator\n");

        //Taking input the operations
        System.out.println("1) Addition\n2)Subtraction\n3)Multiplication\n4)Division");
        System.out.print("\nChoose operation number: ");
        int operation = input.nextInt();

        //Taking input first number
        System.out.print("Enter number 1 : ");
        float num1 = input.nextFloat();
        //Taking input second number
        System.out.print("Enter number 2 : ");
        float num2 = input.nextFloat();

        //Switch-Case to see which operation we need to perform
        switch (operation) {
            case 1 :
                System.out.println("Addition");
                float sum = num1 + num2;
                System.out.println("The answer is : " + sum);
                break;
            case 2 :
                System.out.println("Subtraction");
                float difference = num1 - num2;
                System.out.println("The answer is : " + difference);
                break;
            case 3 :
                System.out.println("Multiplication");
                float product = num1 + num2;
                System.out.println("The answer is : " + product);
                break;
            case 4 :
                System.out.println("Division");
                float division = num1 / num2;
                System.out.println("The answer is : " + division);
                break;
            default:
                System.out.println("Invalid Operator!!!");

        input.close();
        }
    }
}