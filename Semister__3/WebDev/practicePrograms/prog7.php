<?php

    //Arithmetic Operators
    $x = 14;
    $y = 3;
    echo "Addition : ",$x + $y."\n"; // addition
    echo "Subtraction : ",$x - $y."\n"; // subtraction
    echo "Multiplication : ",$x * $y."\n"; // multiplication
    echo "Division : ",$x / $y."\n"; // division
    echo "Modulus : ",$x % $y."\n"; // modulus
    echo "Power : ",$x ** $y."\n"; // power

    //Assignment Operators
    echo "Assignment : ",$x = $y,"\n"; // assignment
    echo "Addition : ",$x = $x + $y,"\n"; // addition assignment
    echo "Subtraction : ",$x = $x - $y,"\n"; // subtraction assignment
    echo "Multiplication : ",$x = $x * $y,"\n"; // multiplication assignment
    echo "Division : ",$x = $x / $y,"\n"; // division assignment
    echo "Modulus : ",$x = $x % $y,"\n"; // modulus assignment

    // Comparison Operators
    $x = 100;
    $y = "50";
        // $x = array("a" => "red", "b" => "green");
        // $y = array("c" => "blue", "d" => "yellow");
    echo "Equal to : ",$x == $y,"\n"; // equal to
    echo "Not equal to : ",$x != $y,"\n"; // not equal to
    echo "Identical to : ",$x === $y,"\n"; // identical to
    echo "Not identical to : ",$x !== $y,"\n"; // not identical to
    echo "Greater than : ",$x > $y,"\n"; // greater than
    echo "Less than : ",$x < $y,"\n"; // less than

    // Increment/Decrement Operators
    $y = 7;
    $x = 5;
    $z = $y++;
    $y = $x++;
    $x = $z++;
    echo "x = $x\n";
    echo "y = $y\n";
    echo "z = $z\n";
    echo "\n";
    $z = ++$y;
    $y = ++$x;
    $x = ++$z;
    echo "x = $x\n";
    echo "y = $y\n";
    echo "z = $z\n";

    // Bitwise Operators
    $x = 10;
    $y = 12;
    echo "Bitwise AND : ",$x & $y,"\n"; // bitwise AND
    echo "Bitwise OR : ",$x | $y,"\n"; // bitwise OR
    echo "Bitwise XOR : ",$x ^ $y,"\n"; // bitwise XOR
    echo "Bitwise NOT : ",~$x,"\n"; // bitwise NOT
    echo "Bitwise left shift : ",$x << 2,"\n"; // bitwise left shift
    echo "Bitwise right shift : ",$x >> 2,"\n"; // bitwise right shift

    // Execution Operator
    $output = `date`;
    echo $output;

    // String Operator
    $txt1 = "Hello";
    $txt2 = "World!";
    echo "Concatenation : ".$txt1.$txt2."\n"; // concatenation of strings
    $txt1 .= $txt2;
    echo "Concatenation : ".$txt1."\n"; // concatenation of strings

    // Conditional Assignment Operator
    $x = 10;
    $y = 10;
    $z = 5;
    echo $x <> $y ? "True" : "False"."\n"; // conditional assignment operator
    echo $z = $z ?? "Does not exist","\n"; // null coalescing operator

    // For more dertailed information on the different operators, visit: https://www.w3schools.com/php/php_operators.asp
?>