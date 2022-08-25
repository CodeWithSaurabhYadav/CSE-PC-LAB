import java.util.Random;

public class Prog7 {
    public static void main(String[] args) {

        // Generating a random character array
        String[] array = new String[3];
        for (int i = 0; i < array.length; i++) {
            Random randomChar1 = new Random();
            char randomChar1A = (char) (randomChar1.nextInt(26) + 'A');
            array[i] = randomChar1A + "";
        }
        // Generating a random 4 digit number array
        Random randomNumberPlate = new Random(9999);
        int randomNumberPlateA = randomNumberPlate.nextInt(9999);
        if (randomNumberPlateA < 1000) {
            randomNumberPlateA = randomNumberPlateA + 1000;
        }
        // Printing the random character array and the random number plate
        System.out.format("The number generated is : %s%s%s-%d\n", array[0], array[1], array[2], randomNumberPlateA);
    }
}
