<?php

    //PHP DATA TYPES

    $StringDT = "Hello world!"; // String Datatype
    var_dump($StringDT);
    $IntDT = 45; // String Datatype
    var_dump($IntDT);
    $FloatDT = 45.45; // Float Datatype
    var_dump($FloatDT);
    $BoolDT = true; // Boolean Datatype
    var_dump($BoolDT);
    $cars = array("Volvo","BMW","Toyota"); // Array Datatype
    var_dump($cars);
    $NullDT = null; // Null Datatype
    var_dump($NullDT);

    //PHP CONSTANTS
    echo PHP_VERSION."\n"; // outputs the version of PHP
    echo __FILE__; // outputs the path and filename of the current script
    echo __LINE__."\n"; // outputs the current line number of the file
    echo __DIR__."\n"; // outputs the path of the current script

    function myfun(){
        echo __FUNCTION__."\n"; // outputs the name of the current function
    }
    myfun();
    class myclass{
        public function myfunClass(){
            echo __CLASS__."\n"; // outputs the name of the current class
        }
        public function myfunMethod(){
            echo __METHOD__."\n"; // outputs the name of the current method
        }
        public function myfunNamespace(){
            echo __NAMESPACE__."\n"; // outputs the name of the current namespace
        }
    }
    $obj = new myclass();
    $obj->myfunClass();
    $obj->myfunMethod();
    $obj->myfunNamespace();
    // THERE ARE MANY MORE PRE-DEFINED VARIABLES CONSTANTS AVAILABLE IN PHP
?>