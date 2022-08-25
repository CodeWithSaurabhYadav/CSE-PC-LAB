<<<<<<< HEAD
<?php 

    function generateUserArray(int $usercount):array{
        $count = 1;
        $generatedArray = array(); // Empty array to store value of the arrays
        while ($count <= $usercount){
            $generatedArray[] = (int) readline(">>> "); // Taking the value from the user and appending it to generate an array
            $count++;
        }
        return $generatedArray; // Returning the generated array
    }   

    function uniqueArray($array1, $array2){
        $merge = array_merge($array1, $array2); // Merging the array
        $res = array(); // Creating a temp array for the result

        // Iterating through the merged array and appending the vale to result array
        for ($i = 0; $i < count($merge); $i++){
            $cond = true; // Created for the result array
            for ($j = 0; $j < count($merge); $j++){
                if ($i != $j){  // prevents from check of element with itself 
                    if ($merge[$i] == $merge[$j]){
                        $cond = false; // If the value is repeated in the merge array more than 1 then the $cond is false 
                    }
                }
            }
            if ($cond){
                $res[] = $merge[$i]; // IF the $cond = true then the value is added to res array
            }
        }
        return $res; // Retutning the result array
    }

    // Taking input form the user for the two arrays
    $arrayNum1 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array
    $arrayNum2 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array

    // generating the ubique array out of the 2 arrays above
    $arrayUnique = uniqueArray($arrayNum1,$arrayNum2); // Calling the function to filter out the values

    echo "The unique array generated is :\n";
    print_r($arrayUnique); // Displaying the unique array
?>
=======
<?php 

    function generateUserArray(int $usercount):array{
        $count = 1;
        $generatedArray = array(); // Empty array to store value of the arrays
        while ($count <= $usercount){
            $generatedArray[] = (int) readline(">>> "); // Taking the value from the user and appending it to generate an array
            $count++;
        }
        return $generatedArray; // Returning the generated array
    }   

    function uniqueArray($array1, $array2){
        $merge = array_merge($array1, $array2); // Merging the array
        $res = array(); // Creating a temp array for the result

        // Iterating through the merged array and appending the vale to result array
        for ($i = 0; $i < count($merge); $i++){
            $cond = true; // Created for the result array
            for ($j = 0; $j < count($merge); $j++){
                if ($i != $j){  // prevents from check of element with itself 
                    if ($merge[$i] == $merge[$j]){
                        $cond = false; // If the value is repeated in the merge array more than 1 then the $cond is false 
                    }
                }
            }
            if ($cond){
                $res[] = $merge[$i]; // IF the $cond = true then the value is added to res array
            }
        }
        return $res; // Retutning the result array
    }

    // Taking input form the user for the two arrays
    $arrayNum1 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array
    $arrayNum2 =  generateUserArray(readline("Enter the number of items in array : "));     // Calling the function to generate an array

    // generating the ubique array out of the 2 arrays above
    $arrayUnique = uniqueArray($arrayNum1,$arrayNum2); // Calling the function to filter out the values

    echo "The unique array generated is :\n";
    print_r($arrayUnique); // Displaying the unique array
?>
>>>>>>> 8a5b7f3e0c22a6832004e9bf5338aab59701b6a3
