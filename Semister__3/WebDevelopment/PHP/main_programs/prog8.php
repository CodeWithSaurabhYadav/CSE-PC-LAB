<?php
    function createArray(&$row, &$col){

        $generatedArray = array();

        for ($arrayRow = 0; $arrayRow < $row; $arrayRow++){
            echo "Row ".($arrayRow+1)." values."."\n";
            $tempArray = array();
            for ($arrayCol = 0; $arrayCol < $col; $arrayCol++){
                $value = (int) readline(">>> ");
                $tempArray[$arrayCol] = $value;
            }
            $generatedArray[$arrayRow] = $tempArray;
        }
        return $generatedArray;
    }

    // Multipling the values
    function multiplyMatrix($matrix1,$matrix2){
        
        $multipiledMatrix = array();

        for ($arrayRow = 0; $arrayRow < count($matrix1); $arrayRow++){
            for ($arrayCol = 0; $arrayCol < count($matrix1[0]); $arrayCol++){
                for ($arry2Col = 0; $arra2Col < count($matrix2); $arra2Col++){
                    
                }
            }
        }
    }

    //Taking the size of the array
    $userArrayRow = (int) readline("Matrix 1 row : ");
    $userArrayCol = (int) readline("Matrix 1 col : ");
    $userArray2Row = (int) readline("Matrix 2 row : ");
    $userArray2Col = (int) readline("Matrix 2 col : ");

    if ($userArrayCol != $userArray2Row){
        echo "Invalid matrix combination for multiplication.\n";
    } else {
        $userArray = createArray($userArrayRow,$userArrayCol);
        $userArray2 = createArray($userArray2Row,$userArray2Col);
        $productArray = multiplyMatrix($userArray,$userArray2);
    }

?>