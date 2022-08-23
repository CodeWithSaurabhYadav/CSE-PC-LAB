<?php

$r = 7;
$co = 1;

echo "-----This is the pascal triangle pattern-----\n\n";
for ($i = 0; $i < $r; $i++) {
    echo "\t";
    for ($ws = 1; $ws <= $r - $i; $ws++) {
        echo "  ";
    }
        
    for ($j = 0; $j <= $i; $j++) {
        if ($j == 0 || $i == 0)
            $co = 1;
        else
            $co = $co * ($i - $j + 1) / $j;
        echo $co . "   ";
    }
    echo "\n";
}

?>
