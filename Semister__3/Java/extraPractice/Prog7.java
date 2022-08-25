import java.util.Scanner;

public class Prog7 {
    public static void main(String[] args) {
        
        // Creationg a common scanner
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your age : ");
        int age = input.nextInt();

        switch (age) {
            case 1:
                System.out.println("You are a 1 year old");
                break;
            case 2:
                System.out.println("You are a two year old");
                break;
            case 3:
                System.out.println("You are a three year old");
                break;
            case 4:
                System.out.println("You are a four year old");
                break;
            case 5:
                System.out.println("You are a five year old");
                break;
            case 6:
                System.out.println("You are a six year old");
                break;
            case 7:
                System.out.println("You are a seven year old");
                break;
            default:
                System.out.println("Your are a " + age + " year old");
        }

        
        input.close();
    }
}
