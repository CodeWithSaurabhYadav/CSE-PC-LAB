<?php
    /*
        B.Tech Computer Science and Engineering
        MNAISH YADAV
        202103103510389
    */
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookies and Sessions</title>

</head>

<body style="background: #eee;">
    <div class="container d-flex flex-column justify-content-center aligin-item-center my-5 p-4" style="background: #fff;border-radius:12px;box-shadow:2px 2px 4px #ccc;">
        <form class="form" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
            <input type="text" class="form-control" name="name">
            <input type="submit" value="Set values" class="btn btn-dark my-3">
            <a class="btn btn-primary" href="session.php">Show session value</a>
        </form>

        <?php
        session_start();
        if (isset($_SESSION['views']))
            $_SESSION['views'] = $_SESSION['views'] + 1;
        else
            $_SESSION['views'] = 1;
        echo "views = " . $_SESSION['views'].'<br><br>';

        if (count($_COOKIE) > 1) {
            echo 'Previous cookies that was set is : '.$_COOKIE['name'].'<br>';
        } else {
            echo "There are no cookies set previously";
        }

        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            $name = $_POST['name'];
            echo "Session Started<br>";
            $_SESSION['name'] = $_POST['name'];
            setcookie("name", $name, time() + (86400 * 30), "/");
            if (!isset($_COOKIE["name"])) {
                if ($_SESSION['views'] == 2){
                    echo "Cookie '" . $name . "' is set!<br>";
                } else echo "Cookie named '" . $name . "' is not set!";
            } else {
                echo "Cookie '" . $name . "' is set!<br>";
                echo "Value is: " . $_COOKIE["name"];
            }
        }
        ?>
    </div>
</body>

</html>