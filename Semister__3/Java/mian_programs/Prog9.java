import java.util.*;

public class Prog9{
    public static void main(String[] args) {
        
        //Initilizing a marix
        int matrix[][] = new int[6][6];
        Random randomValue = new Random(); // random function object

        for (int row = 0; row < matrix.length; row++){
            for (int column = 0; column < matrix.length; column++){
                matrix[row][column] = randomValue.nextInt(2); // Generating 0's and 1's and adding it to the matrix
            }
        }
        
        // Printing the generated matrix
        System.out.println("The generated matrix is :");
        for (int prow = 0; prow < matrix.length; prow++){
            for (int pcolumn = 0; pcolumn < matrix.length; pcolumn++){
                System.out.print((matrix[prow][pcolumn]) + " ");
            }
            System.out.println();
        }
        System.out.println();
        
        /*
        The below two empty arrays are the arrays to
        store the statements of row and column value is 
        EVEN for the generated matrix of 1's and 0's.
        */
        String arrayForOnes[] = new String[matrix.length];
        String arrayForOnesColumn[] = new String[matrix.length];
        String arrayForOnesDigonal[] = new String[matrix.length];


        // Counting 0's and 1's into the generated matrix
        int count2 = 0; // count variable for 1's diagonal
        int count3 = 0; // count variable for 1's diagonal
        for (int crow = 0; crow < matrix.length; crow++){
            int count0 = 0; // count variable for 1's col
            int count1 = 0; // count variable for 1's row
            for (int ccolumn = 0; ccolumn < matrix.length; ccolumn++){
                if (matrix[ccolumn][crow] == 1) count0++;  // Counting number of 1's in column
                if (matrix[crow][ccolumn] == 1) count1++;  // Counting number of 1's in row
                if ( crow == ccolumn) if (matrix[crow][ccolumn] == 1) count2++; // Counting the number of 1's in diagonal
            }
            for (int cncolumn = (matrix.length-1); cncolumn >= 0; cncolumn--){
                if (matrix[cncolumn][crow] == 1) count0++;  // Counting number of 1's in column
                if (matrix[crow][cncolumn] == 1) count1++;  // Counting number of 1's in row
                if ( crow == cncolumn) if (matrix[crow][cncolumn] == 1) count3++; // Counting the number of 1's in diagonal
            }
            if (count0%2 == 0) arrayForOnesColumn[crow] = "The col " + (crow +1 ) + " has even number of 1's"; // Appending the value if count in column is EVEN
            if (count1%2 == 0) arrayForOnes[crow] = "The row " + (crow +1 ) + " has even number of 1's"; // Appending the value if count in row is EVEN
        }
        if (count2%2 == 0) arrayForOnesDigonal[0] = "The diagonal has even number of 1's"; // Appending the value if count in diagonal is EVEN
        else  arrayForOnesDigonal[0] = "The diagonal has odd number of 1's"; // Appending the value if count in diagonal is odd
        System.out.println("For rows : ");
        for (int arrayForOnesRow = 0; arrayForOnesRow < arrayForOnes.length; arrayForOnesRow ++){
            if (arrayForOnes[arrayForOnesRow] != null) // Checking if the particular index value is null or not
                System.out.println(arrayForOnes[arrayForOnesRow]); // If value is not null then dispaling the value
        }
        System.out.println("\nFor columns : ");
        for (int arrayForOnesCol = 0; arrayForOnesCol< arrayForOnesColumn.length; arrayForOnesCol++){
            if (arrayForOnesColumn[arrayForOnesCol] != null) // Checking if the particular index value is null or not
                System.out.println(arrayForOnesColumn[arrayForOnesCol]); // If value is not null then dispaling the value
        }
        System.out.println("\nFor diagonal : ");
        for (int arrayForOnesDig = 0; arrayForOnesDig< arrayForOnesDigonal.length; arrayForOnesDig++){
            if (arrayForOnesDigonal[arrayForOnesDig] != null) // Checking if the particular index value is null or not
                System.out.println(arrayForOnesDigonal[arrayForOnesDig]); // If value is not null then dispaling the value
        }
    }
}