<?php
    /*
        B.Tech Computer Science and Engineering
        SAURABH YADAV
        202103103510362
    */
?>

<!DOCTYPE html>
<html>

<head>

    <title>AJAX</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">

    <script>
        function showHint(str) {
            if (str == "") {
                document.getElementById("suggestions").innerHTML = "";
                return;
            }
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("suggestions").innerHTML = this.responseText;
                }
            }
            xmlhttp.open("GET", "gethint.php?q=" + str, true);
            xmlhttp.send();
        }
    </script>
</head>

<body style="background: #eee;">
    <div class="container my-5 p-5" style="background: #fff;border-radius:12px;box-shadow:2px 2px 4px #ccc;">
        <form class="mx-md-5">
            <input type="text" class="form-control" placeholder="Start typing here...." onkeyup="showHint(this.value)"/>
        </form>
        <div class="my-3" id="suggestions">suggestions will be loaded here</div>
    </div>
</body>

</html>