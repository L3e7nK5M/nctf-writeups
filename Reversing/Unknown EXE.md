# Unknown EXE

- **Category**: Reversing  
- **Solution**:  Perform surface analysis of the binary.


| Step | Screenshot |
|------|------------|  
|1. Download `nctf_binary_2.exe` to your preferred location.<br>As planned, analyze the binary using WSL or a VM.<br>It looks like just `Data`. Even if you execute the binary, nothing happens.|<img width="668" height="245" alt="image" src="https://github.com/user-attachments/assets/da4f7d15-be12-4969-8ef0-0fe5b52f5035" />|
|2. It does not seem to be a proper Windows binary...<br>Look at just the binary header and result shows this binary is Windows.`xxd nctf_binary_2.exe \| head` <br>Then found [MS-DOS stub](https://yaya.lsv.jp/dos_stub/).<br>This means that this is a Windows binary.<br>|<img width="638" height="236" alt="image" src="https://github.com/user-attachments/assets/6c1371c3-7519-45e5-a2f1-1027aa7dabd2" />|
But why does it not execute?|
