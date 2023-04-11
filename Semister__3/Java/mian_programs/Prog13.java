import java.util.Scanner;

class CustException extends Exception{
    public CustException(String error){
        super(error);
    }
}

public class Prog13 {
    public static void validateAge(int num1, int num2) throws CustException{
        if (num2 == 0){
            throw new CustException("Divide by Zero Error");
        } else {
            System.out.println("Divisible");
        }
    }
    public static void main(String[] args) {
        Scanner i = new Scanner(System.in);

        System.out.print("Enter number 1 : ");
        int num1 = i.nextInt();
        System.out.print("Enter number 2 : ");
        int num2 = i.nextInt();
        try{
            validateAge(num1,num2);
        } catch (CustException CE){
            System.out.println("Exception Occured");
            System.out.println(CE);
        }
        i.close();
    }
}
