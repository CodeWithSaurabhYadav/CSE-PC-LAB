<?php

    //Prime number checker
    $number = 2;
    $primeNumberCount = 0;
    $primeNumberSum = 0;
    while ($number <= 100){
        $prime_count = 0;
        $count = 2;
        $half = (int)$number/2;
        while ($count <= $half) {
            if ($number % $count == 0) {
                $prime_count++;
                break;
            }
            $count++;
        }
        if ($prime_count == 0) {
            $primeNumberCount++;
            $primeNumberSum+=$number;
            echo $number." ";
        }
        $number++;
    }
    echo "\nThere are ".$primeNumberCount." prime numbers between 0 and 100.\n";
    echo "The sum of prime numbers between 0 and 100 is ".$primeNumberSum."\n";
    echo "\n";
?>