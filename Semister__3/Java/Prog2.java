import java.util.Scanner;

class Prog2{
    public static void main(String[] args) {
        int num1, num2, num3;

        Scanner input = new Scanner(System.in);

        System.out.print("num1 : ");
        num1 = input.nextInt();
        System.out.print("num2 : ");
        num2 = input.nextInt();
        System.out.print("num3 : ");
        num3 = input.nextInt();

        System.out.printf("num1: %d\nnum2: %d\nnum3: %d\n",num1,num2,num3);


        input.close();
    }
}