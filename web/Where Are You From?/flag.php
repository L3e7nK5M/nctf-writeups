<?php 
$referer = $_SERVER['HTTP_REFERER'] ?? '';

 if(strpos($referer, 'checkref.php') === false) {
          http_response_code(403);
	  echo "<h2>So close! Where are you coming from? ('Д')/</h2>";
	  echo "<h3>Access from the correct location, and include your magic ticket.</h3>"
          exit;
 }
 ?>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>Flaged</title>
    </head>
    <body>
        <h1>Congratulatins!!</h1>
        <p>NCTF{r3FEREr_H3Ad3r_HacK}</p>
    </body>
</html>
