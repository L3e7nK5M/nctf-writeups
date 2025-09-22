| Step | Screenshot |
|------|------------|
| • Access the website.<br>• Nothing is shown. | <img width="600" height="210" alt="image" src="https://github.com/user-attachments/assets/ec87e35b-382c-4fdd-aa94-3db143cadf56" /> | 
| • View the source code.<br>• You can find `robots`. | <img width="600" src="https://github.com/user-attachments/assets/e55e1dc6-2bff-4945-949a-58cfa6a8d13f" /> |
| • Access `robots.txt`.<br>• You will find hidden directory and files. | <img width="600" height="219" alt="image" src="https://github.com/user-attachments/assets/91f3d255-d0a5-445e-bce0-61bfc691d1ad" /> |
| • Access the directories and files.<br>• It seems only `checkref.php` and `flag.php` can be accessed. | <img width="600" height="154" alt="image" src="https://github.com/user-attachments/assets/a90e2c7d-f5f7-4bba-a8a9-a96df266e221" /> |
| From the filenames we can guess:<br>- `flag.php` contains a flag<br>- `checkref.php` is a check page.<br><br>`checkref.php` is checking the [Referer header](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Referer).<br>`flag.php` suggests [Man-in-the-Middle](https://developer.mozilla.org/ja/docs/Glossary/MitM). | <img width="471" height="410" alt="screenshot" src="https://github.com/user-attachments/assets/3de0d97f-13cb-46ab-840f-f540856b6f98" /> |
| Launch Burp Suite, then intercept the request. | <img width="600" height="512" src="https://github.com/user-attachments/assets/86a4fd26-6c14-4a91-9374-eabecd2a1959" />|
| When viewing the request header of `flag.php`, there is no Referer header.<br>The path that `flag.php` expects is:<br>`https://nctf.xvps.jp/ref/ → checkref.php → flag.php` | <img width="1042" height="422" alt="image" src="https://github.com/user-attachments/assets/0eabcedb-1713-4b22-a0d5-7f0f34f191c6" /> |
| MitM (-。-)y-゜゜゜<br>Add the Referer header. | <img width="593" height="240" alt="image" src="https://github.com/user-attachments/assets/64915435-4643-4045-975c-a58cfcde4e5d" /> |
| You can get the flag. | <img width="378" height="135" alt="image" src="https://github.com/user-attachments/assets/673b76ef-806a-4b90-8bf0-ef3e17e047fb" /> |





