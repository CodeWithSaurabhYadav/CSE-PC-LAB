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
    <title>Registration Sucssful</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <style>
        * {
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

        .goTO {
            text-decoration: none;
            font-size: 24px;
            text-transform: uppercase;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            color: #EBF0F5;
        }

        .goTO#sucessText {
            background-color: #88B04B;
        }

        .goTO#failedTxt {
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


</head>

<body>
        <?php
        session_start();
        $genOtp = $_SESSION['OTP'];
        $umail = $_SESSION['umail'];

        if ($_SERVER['REQUEST_METHOD'] == "POST") {
            $UserOtp = $_POST['OTP'];
            if ($genOtp == $UserOtp) {

                $host = "localhost";
                $user = "root";
                $pass = "";
                $db = "userData";
                $port = "3306";
                $conn = mysqli_connect($host, $user, $pass, $db, $port);
                if ($conn) {
                    echo '
                    <section class="vh-100" style="background-color: #eee;">
                        <div class="container h-100">
                            <div class="row d-flex justify-content-center align-items-center h-100">
                                <div class="col-lg-12 col-xl-11">
                                    <div class="card text-black" style="border-radius: 25px;">
                                        <div class="card-body p-md-5">
                                            <div class="row justify-content-center">
                                                <div class="col-md-10 col-lg-6 col-xl-5 order-2 order-lg-1">

                                                    <p class="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Change Password</p>

                                                    <form class="mx-1 mx-md-4" action="change.php" method="POST">
                                                        <div class="d-flex flex-row align-items-center mb-4">
                                                            <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                                                            <div class="form-outline flex-fill mb-0">
                                                                <input type="password" id="upass1" class="form-control" name="upass1" required />
                                                                <label class="form-label" for="upass1">New Password *</label>
                                                            </div>
                                                        </div>
                                                        <div class="d-flex flex-row align-items-center mb-4">
                                                            <i class="fas fa-lock fa-lg me-3 fa-fw"></i>
                                                            <div class="form-outline flex-fill mb-0">
                                                                <input type="password" id="upass2" class="form-control" name="upass2" required />
                                                                <label class="form-label" for="upass2">Confirm New Password *</label>
                                                            </div>
                                                        </div>

                                                        <div class="d-flex justify-content-center mx-4 mb-3 mb-lg-4">
                                                            <input type="submit" class="btn btn-primary btn-lg" value="Change Password">
                                                        </div>
                                                    </form>

                                                </div>
                                                <div class="col-md-10 col-lg-6 col-xl-7 d-flex align-items-center order-1 order-lg-2">

                                                    <img src="https://img.freepik.com/premium-vector/password-reset-icon-flat-vector-design_116137-4571.jpg" class="img-fluid" alt="Sample image">

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>';
                } else {
                    echo "connection failed to the server pleaase try again later or check you internary connection";
                }
            } else {
                echo '
            <div style="border-radius:200px; height:200px; width:200px; background: #FFB3B3; margin:0 auto;">
                <i class="checkmark" id="fail">Y</i>
            </div>
            <h1 id="failTxt">Wrong OTP entered</h1>
            <a href="getCredentails.php" class="goTo" id="failedTxt" >Try Again</a>';
            }
        }
        ?>
</body>

</html>