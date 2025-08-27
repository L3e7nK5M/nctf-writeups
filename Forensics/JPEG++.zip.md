# JPEG++.zip

- **Category**: Forensics  
- **Solution**: Extract a hidden ZIP archive embeded within a JPEG. 


| Step | Screenshot |
|------|------------| 
|1. Download mergedBeer.jpg to your preferred location.<br>Based on its extension, it appears to be a JPEG file<br>As planned, inspect the JPEG using WSL or a VM.<br>`file mergedBeer.jpg`<br>`exiftool mergeeBeer.jpg`<br>The resault shows it is a normal JPEG file and There is no flag info.|<img width="861" height="466" alt="image" src="https://github.com/user-attachments/assets/a4e7c95c-e64c-4300-9cf5-853ac26a783f" />|
|2. From the challenge name **JPEG++.zip**, it seems that this file may contain an embedded ZIP archive. But how can we extract a ZIP from a JPEG?<br>There are many [tools](https://qiita.com/knqyf263/items/6ebf06e27be7c48aab2e) that can solve this challenge, but this time let's try using `binwalk`.<br>`binwalk mergedBeer.jpg`|<img width="953" height="102" alt="image" src="https://github.com/user-attachments/assets/adf9494e-6593-4bee-870e-a55e47bee033" />|
|3. Found a ZIP file, then extract the embedded ZIP file using binwalk with option -e.<br>`binwalk -e mergedBeer.jpg`<br>After extraction, a new folder is created in the current directory, which contains the ZIP file.|<img width="954" height="216" alt="image" src="https://github.com/user-attachments/assets/0f17072f-b7e7-4b21-a666-7c52194c6486" /> <br>※ File name may vary depending on your environment. |
|4. Change directory and decompress ZIP file.<br>Then a file named **s3CrET.txt** exists.<br>`cd _mergedBeer.jpg.extracted/ && ls -la `<br>`unzip 566A.zip`|<img width="368" height="159" alt="image" src="https://github.com/user-attachments/assets/e11cb79f-f107-4539-b693-98ecb5327dc5" />|
|5. Open the **s3CrET.txt**.<br>`cat s3CrET.txt` shows the flag divided by [Linefeed](https://e-words.jp/w/%E3%83%A9%E3%82%A4%E3%83%B3%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89.html).<br>Edit the text with `tr` command: `tr -d '\n' < s3CrET.txt` or `cat s3CrET.txt \| tr -d '\n'`.<br><br>🎉 Congratulations! You found the flag.|<img width="306" height="217" alt="image" src="https://github.com/user-attachments/assets/27c8d9e3-7dab-4aea-a301-68d66497d631" />|
