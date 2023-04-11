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
    <title>Password Validator</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>
<body style="background: #eee;">
    <div class="container d-flex flex-column justify-content-center aligin-item-center my-5 p-4" style="background: #fff;border-radius:12px;box-shadow:2px 2px 4px #ccc;">
        <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="POST" class="d-flex flex-column">
            <label for="inputPassword5" class="form-label">Password</label>
            <input type="password" id="userPass" name="userPass" class="form-control my-3" aria-describedby="passwordHelpBlock">
            <div id="passwordHelpBlock" class="form-text">
                Your password must be 8-20 characters long, contain letters, special characters, and numbers, and must not contain spaces or emoji.
            </div>
            <input type="submit" class="btn btn-dark my-5" value="Check Password Format">
        </form>
        <?php
            if ($_SERVER['REQUEST_METHOD'] == "POST") {
                $password = $_POST['userPass'];

                $uppercase = preg_match('@[A-Z]@', $password);
                $lowercase = preg_match('@[a-z]@', $password);
                $number    = preg_match('@[0-9]@', $password);
                $specialChars = preg_match('@[^\w]@', $password);
                
                if(!$uppercase || !$lowercase || !$number || !$specialChars || strlen($password) < 8) {
                    echo '
                    <div class="alert alert-danger" role="alert">
                        Password should be 8-20 characters in length and should include at least one upper case letter, one number, and one special character.
                    </div>
                    ';
                }else{
                    echo '
                    <div class="alert alert-success" role="alert">
                        '.$password.' is a Strong password.
                    </div>
                    ';
                }
            }
            
        ?>
    </div>
</body>
</html>