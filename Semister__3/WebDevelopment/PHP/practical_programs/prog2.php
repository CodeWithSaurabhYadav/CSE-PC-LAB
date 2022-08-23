<?php
    $percentage = 0;
    $grade = 'A';
    $enroll = (int) readline("Enter your enrollment number : ");

    function percent(){
        $sub1 = (float)readline("Sub1 : ");
        $sub2 = (float)readline("Sub2 : ");
        $sub3 = (float)readline("Sub3 : ");
        $sub4 = (float)readline("Sub4 : ");
        $sub5 = (float)readline("Sub5 : ");
        $percentage = (($sub1+$sub2+$sub3+$sub4+$sub5)*100)/500;
        if ($percentage <= 100 && $percentage >= 0){ return $percentage; }
        else { echo "Invalid Marks"."\n"; }
    }
    function grade($percentage){
        if ($percentage > 90 && $percentage <= 100){ return 'A+'; }
        else if ($percentage > 80){ return 'A'; }
        else if ($percentage > 70){ return 'B+'; }
        else if ($percentage > 60){ return 'B'; }
        else if ($percentage > 50){ return 'C'; }
        else if ($percentage > 40){ return 'D'; }
        else if ($percentage < 40 && $percentage >=0){ return 'F'; }
        else { return "Invalid percent"; }
    }
    switch ($enroll){
        case 362:
            $name = "Saurabh Yadav";
            $percentage = percent();
            $grade = grade($percentage);
            break;
        case 464:
            $name = "Rakesh Shah";
            $percentage = percent();
            $grade = grade($percentage);
            break;
        case 499:
            $name = "Pradeep Prasad";
            $percentage = percent();
            $grade = grade($percentage);
            break;
        default:
            echo "No student exist with ".$enroll."\n";
        }

    echo "\n"."Enroll : ".$enroll."\n";
    echo "Name : ".$name."\n";
    echo "Percentage : ".$percentage."\n";
    echo "Grade : ".$grade."\n";
    

?>