# Ceaser==repeat

- **Category**: Crypto  
- **Solution**: Solve the cipher using CyberChef


| Step | Screenshot |
|------|------------|
|1. Open this Challenge, long lines are displayed. <br>This time, challenge name suggest Ceaser + Base64 + repeat.|<img width="624" height="398" alt="image" src="https://github.com/user-attachments/assets/58b7c2e1-97ff-414e-8015-ee271a7b6bcb" />|
|2. Pass the encrypted strings to [CyberChef](https://gchq.github.io/CyberChef/).<br>How to set the `Repeat` operation? There is no direct `Repeat` operation, but we can use `LABEL` & `Jump` operations instead.<br>The `Jump` operation can also repeat a specific number of times.|<img width="725" height="245" alt="image" src="https://github.com/user-attachments/assets/097e3008-4a38-41fe-a40e-42a6c74f63c8" /><img width="692" height="123" alt="image" src="https://github.com/user-attachments/assets/6c80f354-6728-451c-9a6c-878d85e67ce6" /><img width="689" height="218" alt="image" src="https://github.com/user-attachments/assets/309ac0b1-79d3-40ce-aa87-4d7f8b0f001f" />|
|3. Then set the operations: `Label` (Name: A) → `From Base64` → `Jump` (Label Name: A).<br>Continue until the format `xxxx{xxxx....}` is displayed.<br>It is displayed after about 20 iterations. |<img width="1097" height="506" alt="image" src="https://github.com/user-attachments/assets/cbef8d00-e673-4c2c-87a2-f51e45dcd547" /><img width="1035" height="381" alt="image" src="https://github.com/user-attachments/assets/7cea0ebc-f255-4b6a-87de-16893d156811" />|
|4. Finally set operation to `ROT13` and BAKE!<br><br>🎉 Congratulations! You found the flag.|<img width="852" height="527" alt="image" src="https://github.com/user-attachments/assets/3dcd1b30-6942-43db-b37f-a89b604490af" />|
