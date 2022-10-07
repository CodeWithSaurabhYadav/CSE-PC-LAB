<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practical 5</title>
</head>

<body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/program5/script.php">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Dropdown
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled">Disabled</a>
                    </li>
                </ul>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>

    <?php
    if ($_SERVER['REQUEST_METHOD'] == "POST") {
        $Email = $_POST['email'];
        $Password = $_POST['password'];
        $gender = $_POST['gen'];
        $mobNumber = $_POST['mobNumber'];
        $depart = filter_input(INPUT_POST, 'depart');

        echo '
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Email : </strong>' . $Email . '<br><strong>Password : </strong>' . $Password . '<br><strong>Mobile Number : </strong>' . $mobNumber . '<br><strong>Department : </strong>' . $depart . '<br><strong>Gender : </strong>' . $gender . '
        </div>
        ';
    }
    ?>

    <div class="container mt-3">
        <form action="<?php $_SERVER["PHP_SELF"] ?>" method="POST">
            <div class="mb-3">
                <label for="name" class="form-label">Full Name</label>
                <input type="text" name="name" class="form-control" id="name">
            </div>
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="mobNumber" class="form-label">Mobile Number</label>
                <input type="number" name="mobNumber" class="form-control" id="mobNumber" aria-describedby="emailDOB">
                <div id="emailHelp" class="form-text">We'll never share your mobile bumber with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="mobNumber" class="form-label">Gender</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="gen" id="gen1" value="Male">
                    <label class="form-check-label" for="gen1">
                        Male
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="gen" id="gen2" value="Female">
                    <label class="form-check-label" for="gen2">
                        Female
                    </label>
                </div>
            </div>
            <div class="mb-3">
                <div class="input-group mb-3">
                    <label class="input-group-text" for="depart">Department</label>
                    <select class="form-select" id="depart" name="depart">
                        <option selected>Choose...</option>
                        <option value="B-Tech CSE">B-Tech CSE</option>
                        <option value="B-Tech IT">B-Tech IT</option>
                        <option value="B-Tech Mechanical">B-Tech Mechanical</option>
                        <option value="B-Tech Chemical">B-Tech Chemical</option>
                    </select>
                </div>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="Engineering Graphics" id="sub1">
                <label class="form-check-label" for="sub1">Check me</label>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" name="password" class="form-control" id="password">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>


    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

</body>

</html>
