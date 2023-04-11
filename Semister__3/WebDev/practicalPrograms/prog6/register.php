<?php
    /*
        B.Tech Computer Science and Engineering
        SAURABH YADAV
        202103103510362
    */
?>

<html>

<head>
    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:400,400i,700,900&display=swap" rel="stylesheet">
    <title>Register Message</title>
</head>
<style>
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
    .goTO{
        text-decoration: none;
        font-size: 24px;
        text-transform: uppercase;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        color: #EBF0F5;
    }
    .goTO#sucessText{
        background-color: #88B04B;
    }
    .goTO#failedTxt{
        background-color: #FF1A1A;
    }
    .card {
        background: white;
        padding: 60px;
        border-radius: 4px;
        box-shadow: 0 2px 3px #C8D0D8;
        display: inline-block;
        margin: 0 auto;
    }
</style>

<body>
    <div class="card">
        <?php
            if ($_SERVER['REQUEST_METHOD'] == "POST") {

                $uname = $_POST['uname'];
                $umail = $_POST['umail'];
                $pass1 = $_POST['upass1'];
                $pass2 = $_POST['upass2'];


                $host = "localhost";
                $user = "root";
                $pass = "";
                $db = "userData";
                $port = "3306";

                try {
                    $conn = mysqli_connect($host, $user, $pass, $db, $port);
                    if ($pass1 != $pass2) {
                        echo "Password did not match";
                    } else {
                        try {
                            $sql = "INSERT INTO datails (name,email,password) VALUES (?,?,?)";
                            $smtm = $conn->prepare($sql);
                            $smtm->bind_param('sss', $uname, $umail, $pass2);
                            $smtm->execute();
                            echo '
                            <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
                                <i class="checkmark" id="sucess">✓</i>
                            </div>
                            <h1 id="scressTxt">REGISTERED</h1>
                            <a href="loginDash.php" class="goTo" id="sucessText">Login</a>';

                        } catch (Exception $e) {
                            echo '
                            <div style="border-radius:200px; height:200px; width:200px; background: #FFB3B3; margin:0 auto;">
                                <i class="checkmark" id="fail">X</i>
                            </div>
                            <h1 id="failTxt">FAILED</h1>
                            <a href="index.php" class="goTo" id="failedTxt">Regiser again</a>';
                        }
                    }
                } catch (Exception $ë) {
                    echo "connection f0ailed";
                }
            }
        ?>
    </div>
</body>

</html>