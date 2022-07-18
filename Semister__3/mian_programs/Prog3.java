import java.util.Scanner;

public class Prog3 {
    public static void main(String[] args) {
        //Creationg a common scanner
        Scanner input = new Scanner(System.in);
        
        // Taking input from the user in meter
        System.out.print("Enter the length in meter : ");
        float meter = input.nextFloat();

        // Converting the vlaues
        float foot = meter * 3.28084f;
        float kiloMeter = meter / 1000;
        float centiMeter = meter * 100;

        // Displaying the values
        System.out.println("The values are");
        System.out.println("Kilometer : " + kiloMeter );
        System.out.println("Centimeter : " + centiMeter );
        System.out.println("Foot : " + foot);

        input.close();
    }
}
