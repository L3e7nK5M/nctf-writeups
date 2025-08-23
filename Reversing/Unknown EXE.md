# Unknown EXE

- **Category**: Reversing  
- **Solution**:  Perform surface analysis of the binary.


| Step | Screenshot |
|------|------------|  
|1. Download `nctf_binary_2.exe` to your preferred location.<br>As planned, analyze the binary using WSL or a VM.<br>It looks like just `Data`. Even if you execute the binary, nothing happens.|<img width="668" height="245" alt="image" src="https://github.com/user-attachments/assets/da4f7d15-be12-4969-8ef0-0fe5b52f5035" />|
|2. It does not seem to be a proper Windows binary...<br>Look at just the binary header and result shows this binary is Windows.<br>Check it using the command:`xxd nctf_binary_2.exe \| head` <br>Then found [MS-DOS stub](https://yaya.lsv.jp/dos_stub/).<br>This means that this is a Windows binary.<br>|<img width="615" height="229" alt="image" src="https://github.com/user-attachments/assets/d20f13e0-5e71-4599-9321-ac458fd5c65d" />|
|3. But why does it not execute?<br>Do you know [Magic Number](https://wa3.i-3-i.info/word12868.html)?<br>Let's view the binary: the file header is written as `00 00`.<br>The magic number of an executable should be `4D 5A`, so you should change the value from `00 00` to `4D 5A`.|<img width="179" height="55" alt="image" src="https://github.com/user-attachments/assets/7e437585-1dff-4ff6-ac57-54efa9bb5a87" />|
|4. Edit the binary with your preferred tool.<br>In this example, we use hexedit.<br>Change the value as shown in the picture.|<img width="759" height="210" alt="image" src="https://github.com/user-attachments/assets/a2f093c7-2c46-4efc-b264-48849cc33923" />|
|5. Save and exit (for hexedit: press Ctrl + X, then Y).<br>Now, run the binary again.<br><br>🎉 Congratulations! You found the flag!|<img width="431" height="59" alt="image" src="https://github.com/user-attachments/assets/7698215a-6437-4be2-956c-f3d77c9a75ae" />|
