# What Sees Isn’t Everything.md

- **Category**: Crypto  
- **Solution**: Read the password hidden (white out) in the body of the email, then open the ZIP file using it. After that, follow the message: switch from division to modulo operations.  

| Step | Screenshot |
|------|------------|
|1. Download `Check_the_attached_file.eml`.<br>Open the email with your mail app.<br>It seems there is the `FLAG` in the attached ZIP file.|<img width="783" height="444" alt="image" src="https://github.com/user-attachments/assets/ff35bc2c-cff0-476f-8050-54b26b69354f" />|
|2. Try to open the ZIP file, but it is protected with a password.<br>Where is the password?<br>The hint is in the challenge name ***What Sees Isn’t Everything***.<br>Look at the body of the email again.<br>Select all body text, then hidden password is displayed: `HunterHunter`.|<img width="667" height="425" alt="image" src="https://github.com/user-attachments/assets/89cb2023-6db3-4e2a-8290-8715fe8b9b15" />|
|3. Open the ZIP file using password: `HunterHunter`.<br>Once extracted, there is crypted lines<br>*/4E/43/54/46/7B/4D/69/58/37/55/72/65/5F/68/37/4D/6C/5F/4D/34/69/6C/5F/40/4E/44/5F/43/52/59/70/74/7D*|<img width="694" height="514" alt="image" src="https://github.com/user-attachments/assets/ea87cb80-dc27-4259-88b9-bf364dbead16" /><img width="942" height="305" alt="image" src="https://github.com/user-attachments/assets/34e7833b-dc93-4d69-abf5-5c0227b99289" />|
|4. The challenge message says: `After opening the ZIP file, switch from division to modulo operations.`<br>This means replace `/` → `%`.<br>Use CyberChef: set operation *Find/Replace* with recipe *Find: / Replace: %*.<br>Then `%` characters appear.<br>Does this text look familiar to you?<br>This is [URL Encoded](https://e-words.jp/w/URL%E3%82%A8%E3%83%B3%E3%82%B3%E3%83%BC%E3%83%89.html).|<img width="1363" height="450" alt="image" src="https://github.com/user-attachments/assets/13dc3ce5-8ccb-44b7-8046-1fe3cd10d66b" /><img width="698" height="121" alt="image" src="https://github.com/user-attachments/assets/9cfcbd20-76d8-42d9-8ae8-4453a12a001d" />|
|5. Try add operation `URL Decode`. <br><br>🎉 Congratulations! You found the flag.|<img width="1356" height="500" alt="image" src="https://github.com/user-attachments/assets/3b8d52de-2018-4b7b-aebd-dfe53c20c251" />|
