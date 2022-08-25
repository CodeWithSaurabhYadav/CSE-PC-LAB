<?php

    // Addition Function
    function addition($num1, $num2):float{
        return ($num1 + $num2);
    }
    // Subtraction Function
    function subtract($num1, $num2):float{
        return ($num1 - $num2);
    }
    // Multiplication Function
    function multiplication($num1, $num2):float{
        return ($num1 * $num2);
    }
    // Division Function
    function division($num1, $num2):float{
        if ($num2 == 0) return 0;
        else return ($num1 / $num2);
    }

    // Taking the valures from the user
    $num1 = (float) readline("Number 1 : ");
    $num2 = (float) readline("Number 2 : ");

    // Displaying the values
    echo "The sum is : ",addition($num1, $num2),"\n";
    echo "The difference is : ",subtract($num1, $num2),"\n";
    echo "The product : ",multiplication($num1, $num2),"\n";
    echo "The division is : ",division($num1, $num2),"\n";


?>