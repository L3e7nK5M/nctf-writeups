<?php
 $referer = $_SERVER['HTTP_REFERER'] ?? '';

 if(strpos($referer, 'index.html') === false) {
         http_response_code(403);
         echo "This is <strong>referer</strong> check page";
         exit;
 }

 header("Location: flag.php");
 exit;
?>
