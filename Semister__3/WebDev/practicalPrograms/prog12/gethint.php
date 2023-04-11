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
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
</head>

<body>
    <?php
    $host = "localhost";
    $user = "root";
    $pass = "";
    $db = "ajaxdb";
    $port = "3306";
    $conn = mysqli_connect($host, $user, $pass, $db, $port);

    ?>
    <h4>Suggestions are: </h4>
    <?php
    if ($conn) {
        $sql = "SELECT * FROM data";
        $result = $conn->query($sql);
        $row = mysqli_fetch_all($result);
        $conn->close();

        $q = $_REQUEST["q"];
        $dataArray = array();
        $hint = "";

        for ($i = 0; $i < count($row); $i++) {
            array_push($dataArray, $row[$i][0]);
        }
        if ($q !== "") {
            $q = strtolower($q);
            $len = strlen($q);
            foreach ($dataArray as $name) {
                if (stristr($q, substr($name, 0, $len))) {
                    if ($hint === "") {
                        $hint = $name;
                    } else {
                        $hint .= "<br> $name";
                    }
                }
            }
        }
        echo $hint === "" ? "no suggestion" : $hint;
    } else {
        $hint = "Could not load hint";
    }
    ?>
</body>

</html>