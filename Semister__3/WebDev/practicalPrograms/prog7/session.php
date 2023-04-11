<?php
    /*
        B.Tech Computer Science and Engineering
        MANISH YADAV
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
        <h4>
            <?php 
                session_start();
                echo $_SESSION['name'];
            ?>
        </h4>
        <a href="index.php">Go Back</a>
    </div>
</body>
</html>