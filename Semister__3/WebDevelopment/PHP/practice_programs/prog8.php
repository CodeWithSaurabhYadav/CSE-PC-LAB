<?php

    // Numbers for opreation
    $num1 = 455;
    $num2 = 34;
    $num3 = 67;

    //   Condition?Expression1:Expression2;
    $max_number = $num1 > $num2 ? ($num1 > $num3 ? $num1 : $num3) : ($num2 > $num3 ? $num2 : $num3);
    echo "The largest number is : ".$max_number."\n";
?>