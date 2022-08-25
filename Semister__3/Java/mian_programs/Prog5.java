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
        
        int temp = num1;
        if ( num1 > num2 && num1 > num3){
            System.out.println("1st condition");

            if ( num2 < num3){
                num2 = num3;
                num3 = temp;
            }
        }
        else if ( num2 > num1 && num2 > num3){
            System.out.println("2nd condition");
            num1 = num2;
            num2 = temp;

            if ( num2 < num3){
                num2 = num3;
                num3 = temp;
            }
        }
        else if ( num3 > num1 && num3 > num2){
            System.out.println("2nd condition");
            num1 = num3;
            num3 = temp;

            if ( num2 < num3){
                num2 = num3;
                num3 = temp;
            }
        }

        System.out.println(num1 + " " + num2 + " " + num3);
        input.close();
    }
}
