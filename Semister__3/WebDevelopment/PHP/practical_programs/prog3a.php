<<<<<<< HEAD
<?php

    // While Loop prime fibonaci series
    
    // Initilizing the variables
    $num = 0;
    $sum = 1;
    $temp = 0;
    $iterate = 1;
    $count = 20;

    // Iterationg and Printing the fibonaci series
    while ($iterate <= $count){
        $temp = $sum + $num;
        $sum = $num;
        $num = $temp;
        echo $temp." ";
        $iterate++;
    }
=======
<?php

    // While Loop prime fibonaci series
    
    // Initilizing the variables
    $num = 0;
    $sum = 1;
    $temp = 0;
    $iterate = 1;
    $count = 20;

    // Iterationg and Printing the fibonaci series
    while ($iterate <= $count){
        $temp = $sum + $num;
        $sum = $num;
        $num = $temp;
        echo $temp." ";
        $iterate++;
    }
>>>>>>> 8a5b7f3e0c22a6832004e9bf5338aab59701b6a3
?>