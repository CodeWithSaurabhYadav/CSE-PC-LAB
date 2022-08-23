<?php 

    function generateUserArray(int $usercount):array{
        $count = 1;
        $generatedArray = array();
        // array_push($generatedArray,12);
        while ($count <= $usercount){
            $generatedArray[] = (int) readline(">>> "); // Taking the value from the user and appending it to generate an array
            $count++;
        }
        return $generatedArray;     // Returning the generated array
    }   

    function uniqueArray($array1, $array2){
        $universalArray = array_merge($array1, $array2);
        $filteredArray = array();
        // print_r($universalArray);
        for ($index = 0; $index < count($universalArray); $index++){
            $count = 0;
            for ($index2 = 1; $index2 < count($universalArray); $index2++){
                if ($universalArray[$index] == $universalArray[$index2]){
                    $count++;
                    break;
                }
                continue;
            }
            if ($count > 0){
                $filteredArray[] = $universalArray[$index];
            }
        }
        // return $filteredArray;
        return $filteredArray;

    }



    $arrayNum1 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array
    $arrayNum2 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array
    
    $arrayUnique = uniqueArray($arrayNum1,$arrayNum2);      // Calling the function to filter out the values

    echo "The unique values are : ";
    for ($index = 0; $index < count($arrayUnique); $index++){
        echo " ".$arrayUnique[$index];
        if ($index != (count($arrayUnique) - 1)){
            echo ",";
        }
    }
?>