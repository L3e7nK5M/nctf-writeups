# Exif

- **Category**: Forensics  
- **Solution**: Display the JPEG file and inspect its Exif metadata.


| Step | Screenshot |
|------|------------| 
|1. Download tiger.jpg to your preferred location.<br>Based on its extension, it appears to be a JPEG file<br>As planned, inspect the JPEG using WSL or a VM.<br>`file tiger.jpg`|<img width="949" height="100" alt="image" src="https://github.com/user-attachments/assets/7f056925-08d9-4de0-bb5e-676433f28f79" />|
| 2. Use another tool to analyze the file.<br>Try [exiftool](https://zenn.dev/ds2169/articles/46b6afd52a0255) to extract metadata.<br>`exiftool tiger.jpg` | <img width="778" height="423" alt="image" src="https://github.com/user-attachments/assets/c50d337a-e189-4c68-b368-6584a178975f" /> |
| 3. 🎉 Congratulations! You found the flag. |
