<?php 

    function generateUserArray(int $usercount){
        $count = 1;
        $generatedArray = array();
        // array_push($generatedArray,12);
        while ($count <= $usercount){
            $generatedArray[] = (int) readline(">>> ");
            $count++;
        }
        return $generatedArray;
    }

    function uniqueArray($array1, $array2){
        $uniqueValue = array();
        for ($array1Index = 0, $array1Index < count($array1); $array1Index++){
            for ($array1Index2 = 0, $array1Index2 < count($array1); $array1Index2++){
                echo "hello";
            }
        }
    }


    $arrayNum1 =  generateUserArray(readline("Enter the number of items in array : "));
    $arrayNum2 =  generateUserArray(readline("Enter the number of items in array : "));
    
    $arrayUnique = uniqueArray($arrayNum1,$arrayNum2);
    print_r($arrayUnique);
?>