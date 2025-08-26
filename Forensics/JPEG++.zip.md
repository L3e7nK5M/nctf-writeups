# JPEG++.zip

- **Category**: Forensics  
- **Solution**: Extract a hidden ZIP archive embeded within a JPEG. 


| Step | Screenshot |
|------|------------| 
|1. Download mergedBeer.jpg to your preferred location.<br>Based on its extension, it appears to be a JPEG file<br>As planned, inspect the JPEG using WSL or a VM.<br>`file mergedBeer.jpg`<br>`exiftool mergeeBeer.jpg`<br>The resault shows it is a normal JPEG file and There is no flag info.|<img width="861" height="466" alt="image" src="https://github.com/user-attachments/assets/a4e7c95c-e64c-4300-9cf5-853ac26a783f" />|
|2. From challenge name **JPEG++.zip**, It looks that this file embeded ZIP file but how extract from JPEG to ZIP?<br>many [tool](https://qiita.com/knqyf263/items/6ebf06e27be7c48aab2e) are able to solve this challenge, this time try using binwalk.<br>`binwalk -e mergedBeer.jpg` | 
