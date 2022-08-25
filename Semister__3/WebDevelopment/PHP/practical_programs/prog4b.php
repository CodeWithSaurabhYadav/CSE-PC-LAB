<?php

    // Function to get matrix dimensions
    function getDimensions($arrayNum):array{
        $matrixDimensions = array();
        $matrixDimensions[] = (int) readline("Number of rows of Matrix ".$arrayNum." : ");
        $matrixDimensions[] = (int) readline("Number of columns of Matrix".$arrayNum." : ");

        return $matrixDimensions;
    }

    // Function to generate matrix accoriding to the dimensions provided
    function generateMatrix(int $userRow, int $userCol):array{
        $generatedMatrix = array();
        for ($row = 1; $row <= $userRow; $row++){
            $colArray = array();
            for ($col = 1; $col <= $userCol; $col++){
                $colArray[] = (int) readline("( ".$row.", ".$col.") >>> "); // Taking the value from the user and appending it to generate an array
            }
            $generatedMatrix[] = $colArray;
        }
        return $generatedMatrix;     // Returning the generated array
    }

    // Function to multiply 2 matrix
    function matrix_product($mat1,$mat2){
        $res = array();
        for ($row1 = 0; $row1 < count($mat1); $row1++){
            for ($col = 0; $col < count($mat2[0]); $col++){
                for ($row2 = 0; $row2 < count($mat2); $row2++){
                    $res[$row1][$col] += $mat1[$row1][$row2] * $mat2[$row2][$col];
                } 
            }
        }
        return $res;        
    }

    //Program starts from here.
    $matrixDimensions1 = getDimensions(1);
    $matrixDimensions2 = getDimensions(2);

    if ($matrixDimensions1[1] != $matrixDimensions2[0]){
        echo "\nMatrix multiplication for the current 2 matrix is not possible.\n\n";
    }
    else{

        echo "Matrix 1 Elements : \n";
        $mat1 = generateMatrix($matrixDimensions1[0],$matrixDimensions1[1]);
        echo "Matrix 1 Elements : \n";
        $mat2 = generateMatrix($matrixDimensions2[0],$matrixDimensions2[1]);
        $res = matrix_product($mat1,$mat2);

        
        echo "\nThe multiplied Matrix is : \n";
        print_r($res);
    }

?>
