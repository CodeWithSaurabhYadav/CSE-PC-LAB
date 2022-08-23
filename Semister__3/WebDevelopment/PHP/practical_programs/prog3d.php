<?php

    function generateUserArray(int $usercount){
        $count = 1;
        $usrCredintials = array();
        while ($count <= $usercount){
            echo "user : ".$count."\n"; 
            $usrCredintials[readline("Username : ")] = readline("Password : ");
            $count++;
        }
        return $usrCredintials;
    }
    $usrCredintials = generateUserArray(readline("Enter number of users : "));
    echo "\n"."The users are : "."\n";
    echo "Username => Password (The format is line this)"."\n\n";
    foreach($usrCredintials as $username => $password){
        echo $username." => ".$password."\n";
    }

?>