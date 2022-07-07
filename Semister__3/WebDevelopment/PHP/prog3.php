<?php
    $num = 34; // Global Varaible
    echo "The value of num outside the function is : ".$num."\n";
    function myFunction() {
        echo "The value of num inside the function is : ".$num."\n";
    }
    myFunction();
?>