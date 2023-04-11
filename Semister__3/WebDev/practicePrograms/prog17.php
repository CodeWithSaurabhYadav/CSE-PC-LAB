<?php 

    function intArguments(int $value){
        return is_int($value);
    }
    function returnFloat():float{
        return 45;
    }

    echo intArguments(45)."\n";
    echo returnFloat()."\n";
?>