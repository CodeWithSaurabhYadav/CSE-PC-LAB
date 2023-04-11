<?php
    /*
        B.Tech Computer Science and Engineering
        SAURABH YADAV
        202103103510362
    */

    // pascal triangle pattern in PHP language

    $row = 6;
    $col = 1;

    $i = 0;
    while ($i < $row) {
        echo "\t";
        $ws = 1;
        while ($ws <= $row - $i) {
            echo "  ";
            $ws++;
        }
        $j = 0;
        while ($j <= $i) {
            if ($j == 0 || $i == 0)
                $col = 1;
            else
                $col = $col * ($i - $j + 1) / $j;
            $j++;
            echo $col . "   ";
        }
        $i++;
        echo "\n";
    }
?>