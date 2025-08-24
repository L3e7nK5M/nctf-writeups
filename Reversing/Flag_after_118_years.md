# Flag_after_118_years

- **Category**: Reversing  
- **Solution**:  bypass or edit sleep function.


| Step | Screenshot |
|------|------------|
|1. Download `nctf_bin_after118years` to your preferred location.<br>As planned, analyze the binary using WSL or a VM.<br>It looks like a Linux ELF binary. When you run it, the message "Analyzing system......" is displayed, but nothing else happens.|<img width="1100" height="158" alt="image" src="https://github.com/user-attachments/assets/e2207beb-79b1-4166-b38a-da274c72c59d" />|
|2. After waiting for a few minutes, still nothing happens. Let's check which functions are used with `nm`.<br>`nm nctf_bin_after118years`|<img width="559" height="533" alt="image" src="https://github.com/user-attachments/assets/fa097159-ea1b-4158-8977-70ac19f91b51" />|
|3. From the result, we can see `main`, `puts`, and also the `sleep` function being called. This explains why the binary never finishes: it is stuck in `sleep`.|<img width="500" height="73" alt="image" src="https://github.com/user-attachments/assets/8dd73724-7919-47fd-bd85-96f84ce6c359" />|
|4. Well, then what time do we have to wait?. there should be stucked arg, try looking at the binary with `objdump`<br>`objdump -M intel -D -j .text nctf_bin_after118years\|grep "<main>:" -A 70`|<img width="752" height="250" alt="image" src="https://github.com/user-attachments/assets/7d32c0f1-7102-438f-8371-a6f8a4ad713c" />|
|5. Appealentry it is stucked `0xdeadbeef`. what seconds is 0xdeadbeef? according to Google, 3.154e+7 / 3735928559(decimal) = about 118 years. we don't wait for years so change the value of 0xdeadbeef you prefered way. 

