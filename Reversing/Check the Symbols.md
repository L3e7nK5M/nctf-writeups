# Check the Symbols

- **Category**: Reversing  
- **Solution**: Find the hidden function and call it. Required knowledge: Dynamic analysis  

| Step | Screenshot |
|------|------------| 
|1. Download `nctf_binary_3.elf` to your preferred location.<br>As planned, analyze the binary using WSL or a VM.<br>Do the following commands:<br>`file nctf_binary_3.elf`<br>`strings nctf_binary_3.elf \| grep -i nctf`<br>`./nctf_binary_3.elf`|<img width="1102" height="156" alt="image" src="https://github.com/user-attachments/assets/68a9789c-2bd3-4d89-81b2-553d2e7b1361" />The result of executing the binary shows no flag.<br>However, there is a hint from the displayed message: **"I wonder if this prints anything. ⚠️ hiddenFunc()"**|
|2. Search for `hiddenFunc` with [nm](https://linuxcommand.net/nm/):<br>`nm nctf_binary_3.elf`<br>In the text section, this function is found.|<img width="412" height="326" alt="image" src="https://github.com/user-attachments/assets/f78cde72-2d3d-49cb-8215-b70d8d27d4e9" />|
|3. Additionally, Try analyzing the main function with [objdump](https://linuxcommand.net/objdump/).<br>It seems that **hiddenFunc** is not called from the main function.|<img width="1053" height="308" alt="image" src="https://github.com/user-attachments/assets/a6997aec-0156-483e-bff5-0e777e890703" />|
|4. Do [Dynamic analysis](https://e-words.jp/w/%E5%8B%95%E7%9A%84%E8%A7%A3%E6%9E%90.html) and call hiddenFunc with [gdb (how to use)](https://inaz2.hatenablog.com/entry/2014/05/03/044943).|<img width="435" height="64" alt="image" src="https://github.com/user-attachments/assets/bac2a056-e453-4682-baff-555b6e65d8c8" />|
|5. List functions.<br>`info functions`<br>There are two: `main` and `hiddenFunc`.|<img width="362" height="134" alt="image" src="https://github.com/user-attachments/assets/4f16f5b2-c0d1-448a-93a3-f102449f618a" />|
|6. Then set a breakpoint at the main function.<br>`b main`<br>Run the code.<br>`run`<br>`b`, `n` are aliases for `break`, `next`.|<img width="718" height="289" alt="image" src="https://github.com/user-attachments/assets/1c2e6c76-39aa-4c90-bd59-fe67c933d7dc" />|
|7. We have confirmed the program runs normally, let's try calling **hiddenFunc**. ※Note: don’t forget `()` → `hiddenFunc()`<br>Bingo! ☺<br>🎉 Congratulations! You found the flag.|<img width="416" height="42" alt="image" src="https://github.com/user-attachments/assets/2e4be3db-6d0c-4983-9c36-a02791f46893" />|

