<?php

    // While Loop prime fibonaci series
    
    // Initilizing the variables
    $num = 0;
    $sum = 1;
    $temp = 0;
    $iterate = 0;

    // Iterationg and Printing the fibonaci series
    while ($iterate <= 100000){
        $temp = $sum + $num;
        $sum = $num;
        $num = $temp;
        echo $temp." ";
        $iterate++;
    }
?>