# Caesar==

- **Category**: Crypto  
- **Solution**: Solve the cipher using CyberChef

| Step | Screenshot |
|------|------------|
|1. Open the challenge. The following line is displayed:<br>QVBHU3tQcm5mcmVfbmFxX29uZnI2NF96dmtycX0=<br><br>Why is '==' added? This looks like Base64 padding.|<img width="621" height="328" alt="image" src="https://github.com/user-attachments/assets/7faabb39-578b-47fa-aa01-be771618aef0" />|
|2. Copy and paste the string **"QVBHU3tQcm5mcmVfbmFxX29uZnI2NF96dmtycX0="** into [CyberChef](https://gchq.github.io/CyberChef/).<br>Apply the **From Base64** operation. |<img width="1676" height="777" alt="image" src="https://github.com/user-attachments/assets/2950268a-20c1-41aa-a1ec-a08e547e0418" />|
|3. The output format looks correct, but the letters are scrambled.<br>Now just try a Caesar shift. |<img width="378" height="156" alt="image" src="https://github.com/user-attachments/assets/107e3185-8ef9-4540-9ed0-62ffacf8cce5" />|
|4. Add the **ROT13** operation and click **BAKE**!<br><br>🎉 Congratulations! You found the flag! |<img width="1206" height="652" alt="image" src="https://github.com/user-attachments/assets/227492d5-fb85-4390-9939-20a20966b002" />|
