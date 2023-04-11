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
    <title>Enter your cretentials for the password change</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <style>
        body {
            text-align: center;
            padding: 40px 0;
            background: #EBF0F5;
        }

        .card {
            background: white;
            padding: 60px;
            border-radius: 4px;
            box-shadow: 0 2px 3px #C8D0D8;
            display: inline-block;
            margin: 0 auto;
        }

        form {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        #umail {
            font-family: 'Josefin Sans', sans-serif;
            width: 450px;
            font-size: 20px;
            text-align: center;
        }
    </style>
</head>

<body>
    <div class="card">
        <?php
        echo '
            <div class="container d-flex justify-content-center">
                <form action="passwordReset.php" method="POST">
                    <span class="my-5">ENTER YOUR EMAIL ADDRESS.</span>
                    <input type="email" name="umail" id="umail" class="form-control" max="999999" min="000000"/>
                    <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4 my-5">
                        <input type="submit" class="btn btn-primary btn-lg" value="CONFIRM">
                    </div>
                </form>
            </div>
            <a href="index.php" class="goTo" id="failedTxt" >Go back</a>
        ';
        ?>
    </div>
</body>

</html>