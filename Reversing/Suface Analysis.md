# Suface Analysis

- **Category**: Reversing  
- **Solution**:  Perform surface analysis of the binary.


| Step | Screenshot |
|------|------------|  
|1. Download `nctf_binary_1.exe` to your preferred location.<br>as planned, analyze the binary using WSL or a VM.<br>It looks like a Windows executable. Even if you run the binary, nothing happens.|<img width="838" height="107" alt="image" src="https://github.com/user-attachments/assets/cc91930e-3a05-45c9-a7c9-2112afabcdea" />|
|2. Do `strings` command.<br>`strings nctf_binary_1.exe \| grep -i nctf`<br>Bingo!☺<br>🎉 Congratulations! You found the flag.|<img width="494" height="53" alt="image" src="https://github.com/user-attachments/assets/cb658c3c-c8bf-4d25-9802-7ed2f0c2e39f" />|
