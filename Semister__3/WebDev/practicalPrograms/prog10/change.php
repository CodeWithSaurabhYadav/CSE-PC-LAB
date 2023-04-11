<?php
    /*
        B.Tech Computer Science and Engineering
        SAURABH YADAV
        202103103510362
    */
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        *{
            text-decoration: none;
        }
        body {
            text-align: center;
            padding: 40px 0;
            background: #EBF0F5;
        }
        h1 {
            color: #88B04B;
            font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
            font-weight: 900;
            font-size: 40px;
            margin-bottom: 10px;
        }
        h1#scressTxt {
            color: #88B04B;
        }
        h1#failTxt {
            color: #FF1A1A;
        }
        i {
            font-size: 100px;
            line-height: 200px;
            margin-left: -15px;
        }
        i#sucess {
            color: #9ABC66;
        }
        i#fail {
            color: #FF1A1A;
        }
        .card {
            background: white;
            padding: 60px;
            border-radius: 4px;
            box-shadow: 0 2px 3px #C8D0D8;
            display: inline-block;
            margin: 0 auto;
        }
        #username{
            display: none;
        }
    </style>
</head>
<body>
    <div class="card">
        <?php
            session_start();
            if ($_SERVER['REQUEST_METHOD'] == "POST") {
                $username = $_SESSION['umail'];
                $pass1 = $_POST['upass1'];
                $pass2 = $_POST['upass2'];

                // echo $username."<br>".$pass1."<br>".$pass2;
                
                $host = "localhost";
                $user = "root";
                $pass = "";
                $db = "userData";
                $port = "3306";
                
                if ($pass1 == $pass2){
                    $conn = mysqli_connect($host, $user, $pass, $db, $port);
                    if ($conn){
                        $sql = 'UPDATE datails SET password = (?) WHERE email = (?)';
                        $smtm = $conn->prepare($sql);
                        $smtm->bind_param('ss',$pass1,$username);
                        try {
                            $smtm->execute();
                            echo '
                            <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
                                <i class="checkmark" id="sucess">✓</i>
                            </div>
                            <h1 id="scressTxt">Password Changed</h1>
                            <a  href="index.php" style="font-size: 24px;text-transform: uppercase;padding: 0.5rem 1rem;border-radius: 6px;color: #EBF0F5;background-color: #88B04B;border=0px;"/>Login Again</a>';
                        } catch (Exception $e){
                            echo '
                            <div style="border-radius:200px; height:200px; width:200px; background: #FFB3B3; margin:0 auto;">
                                <i class="checkmark" id="fail">X</i>
                            </div>
                            <h1 id="failTxt">Password Change Failed</h1>
                            <form action="changePass.php" method="POST">
                                <input type="text" value="'.$username.'" id="username" name="username" />
                                <input type="submit" class="goTo" id="sucessText" value="Go Back" style="font-size: 24px;text-transform: uppercase;padding: 0.5rem 1rem;border-radius: 6px;color: #EBF0F5;background-color: #FF1A1A;border=0px;"/>
                            </form>';
                        }
                    } else {
                        echo '
                        <div style="border-radius:200px; height:200px; width:200px; background: #FFB3B3; margin:0 auto;">
                            <i class="checkmark" id="fail">X</i>
                        </div>
                        <h1 id="failTxt">Password Change Failed</h1>
                        <form action="changePass.php" method="POST">
                            <input type="text" value="'.$username.'" id="username" name="username" />
                            <input type="submit" class="goTo" id="sucessText" value="Go Back" style="font-size: 24px;text-transform: uppercase;padding: 0.5rem 1rem;border-radius: 6px;color: #EBF0F5;background-color: #FF1A1A;border=0px;"/>
                        </form>';
                    }
                } else {
                    echo "<h3>Password  didi not match</h3>";
                    echo '<a href="getCredentails.php" class="goTo" id="failedTxt" >Try Again</a>';
                }
            }
        ?>
    </div>
</body>
</html>