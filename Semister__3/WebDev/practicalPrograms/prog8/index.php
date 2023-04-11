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
    <title>File Upload and Download</title>

    <style>
    </style>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container-md my-5">
        <div class="alert alert-primary" role="alert">
            You can upload any type of file here.
        </div>
        <div>
            <form action="<?php $_SERVER['PHP_SELF']?>" enctype="multipart/form-data" method="POST" class="d-flex flex-column justify-content-center align-items-center">
                <input class="form-control form-control-lg" type="file" name="file">
                <button class="btn btn-secondary my-3" type="submit">Upload File</button>
            </form>

            <?php
                if ($_SERVER['REQUEST_METHOD'] == "POST"){
                    $fileUpload = $_FILES['file'];
                    move_uploaded_file($fileUpload["tmp_name"],"uploads/".$fileUpload['name']);
                }
            ?>

        </div>
        <div class="container">
            <h3 class="my-3">Uploaded Files</h3>
            <table class="table">
                <tr>
                    <th scope="col">File name</th>
                    <th scope="col">Download Link</th>
                </tr>
                <?php
                $files = scandir('uploads');
                for ($fileCount = 2; $fileCount < count($files); $fileCount++){
                    ?>
                    <tr scope="row">
                        <td><?php echo $files[$fileCount] ?></td>
                        <td><a download="<?php echo $files[$fileCount] ?>" href="uploads/<?php echo $files[$fileCount] ?>" class="btn btn-primary">Download Now</a></td>
                    </tr>
                <?php
                }
                ?>
            </table>
        </div>
    </div>
</body>
</html>