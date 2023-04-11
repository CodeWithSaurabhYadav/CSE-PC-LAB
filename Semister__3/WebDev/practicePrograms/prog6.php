<?php
    define ("PI", 3.14); // define a constant
    echo PI."\n"; // outputs the value of PI
    echo pi()."\n"; // outputs the value of pi()

    function my_function() {
        echo "Hello World!"."\n";
        echo PI."\n";
    }
    my_function(); // outputs "Hello World!" and the value of PI
?>