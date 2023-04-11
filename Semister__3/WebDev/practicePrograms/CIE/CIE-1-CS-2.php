<?php


    function getUserStatements($count){
        $statementArray = array();
        for ($index = 0; $index < $count; $index++){
            $statementArray[] = (String) readline("Enter statement ".($index+1)." : ");
        }
        $splitedArray = array_chunk($statementArray,1);
        
        return $splitedArray;
    }
    
    function removeSplitLine($passedArray){
        $respondArray = array();
        for ($i = 0; $i < count($passedArray); $i++){
            $statement = str_replace("<b>","",$passedArray[$i][0]);
            $respondArray[] = explode(" ",$statement);
        }

        return $respondArray;
    }
    function replaceConsonants($passedArray){
        $consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
        $consonantsArray = str_split($consonants);

        for ($i = 0; $i < count($passedArray); $i++){
            for ($j = 0; $j < count($passedArray[$i]); $j++){
                $passedArray[$i][$j] = str_replace($consonantsArray,'*',$passedArray[$i][$j]);
            }
        }
        
        return $passedArray;
    }

    function printTriangle($passedArray){
        function triangle($n,$word){
            $k = 2 * $n - 2;
            for ($i = 0; $i < $n; $i++){
                for ($j = 0; $j < $k; $j++)
                echo " ";
                $k = $k - 1;
                for ($j = 0; $j <= $i; $j++ ){
                    echo $word[$i]." ";
                }
                echo "\n";
            }
        }
        for ($i = 0; $i < count($passedArray); $i++){
            for ($j = 0; $j < count($passedArray[$i]); $j++){
                triangle(strlen($passedArray[$i][$j]),$passedArray[$i][$j]);
            }
        }
    }

    echo "Start entering your statements : "."\n";
    $statementArray = getUserStatements(5);
    $splitedArray = removeSplitLine($statementArray);
    $vowelsArray = replaceConsonants($splitedArray);

    print_r($statementArray);
    print_r($splitedArray);
    print_r($vowelsArray);
    printTriangle($vowelsArray);

?>
