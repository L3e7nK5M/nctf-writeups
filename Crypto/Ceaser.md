#Ceaser

- **Category**: Crypto  
- **Solution**: solve pchipher using Cyber chef

| Step | Screenshot |
|------|------------| 
|1. Open this Challenge, 2 lines are displayed:<br>**}r%uLE9:D0E:>60D9:7E6503J0cfN**<br>and a hint: **The year of his death + 3** (maybe this is the key).|<img width="497" height="190" alt="image" src="https://github.com/user-attachments/assets/3543a1de-23d2-4284-b6c2-8c0896264eb8" />|
|2. Pass the line **}r%uLE9:D0E:>60D9:7E6503J0cfN** to [CyberChef](https://gchq.github.io/CyberChef/).<br>The algorithm is suggested by the challenge name `Ceaser` → use **ROT13 / Caesar cipher** operation.<br>However, BAKE! failed. the shift amount is not correct.|<img width="1126" height="489" alt="image" src="https://github.com/user-attachments/assets/de051ec9-357f-4054-a988-a2f1ced9e8b9" />|
|3. Then use the hint: **The year of his death + 3**<br>`his = Caesar?`<br>Google `The year of Caesar's death`.<br>Then 44 + 3 = 47, so the amount of shift is 47.|<img width="821" height="411" alt="image" src="https://github.com/user-attachments/assets/a67c554c-5425-4307-9854-7846e9dc12aa" />|
|4. Set operation to `ROT47` and BAKE!<br><br>🎉 Congratulations! You found the flag.|<img width="1039" height="477" alt="image" src="https://github.com/user-attachments/assets/d681cb46-ebbb-4e78-96e3-323373b622de" />|
