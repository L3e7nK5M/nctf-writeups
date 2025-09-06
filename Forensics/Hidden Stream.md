# Hidden Stream

- **Category**: Forensics  
- **Solution**: exit zip file in the [ADS](https://cybersecurity-jp.com/security-words/99767) using [FTK imager](https://muchipopo.com/forensic/memorydump/)


| Step | Screenshot |
|------|------------| 
|1. Download `nctf_bakup.dd` to your preferred location.<br>Based on the extension [`dd`](https://qiita.com/gpmrh096/items/70dfdf2a36c0de96d16d), it is a bit-by-bit copy of a disk partition.<br>As planned, inspect the file using WSL or a VM.<br>`file nctf_bakup.dd`<br><br>From the result, the format is Windows [NTFS](https://e-words.jp/w/NTFS.html).|<img width="700" height="74" alt="image" src="https://github.com/user-attachments/assets/c4887713-f3a6-4de7-bbc2-6c5b08d65fb3" />|
|2. There are many ways to analyze this file. This time use FTK Imager.<br>First, add an evidence item and select *image file* as the source, then browse and choose `nctf_bakup.dd`.|<img width="645" height="465" alt="image" src="https://github.com/user-attachments/assets/86d95598-d4f4-417e-b2a3-0fddff9d4bc7" /><img width="504" height="235" alt="image" src="https://github.com/user-attachments/assets/cb1259f1-2e9f-4c28-9c67-7d6755a1cee4" />|
|3. Expanding the evidence tree, a suspicious ZIP file was found inside a JPEG file.<br>Export this file to your preferred location.<br>This file is a kind of [ADS](https://qiita.com/minr/items/c2393f532b2df35f7a9d) (*Alternate Data Stream*), which can hide data inside a file.|<img width="297" height="292" alt="image" src="https://github.com/user-attachments/assets/06c4f851-ea17-44b0-b2f1-3463791b9819" /><img width="619" height="145" alt="image" src="https://github.com/user-attachments/assets/bf7b3fc3-4784-4632-8c89-a157ca8f3d20" />|
|4. Now, open the ZIP file, but it is protected by a password.<br>It is time to crack it using [zip2john](https://omomuki-tech.com/archives/813).<br>`zip2john f14g.zip > pw.hash` <br>※pw.hash is in a format supported by John the Ripper.<br>Then, where is the password list? Try searching the same PC, maybe it exists inside `nctf_bakup.dd`.<br>While searching, you found a suspicious file. Export it and rename it with following command*:<br> `mv 01433 pwlist.txt`<br>*In case of Linux OS.|<img width="979" height="556" alt="image" src="https://github.com/user-attachments/assets/f3607c77-28f9-43c9-ac69-761f6cbba08f" />|
|5. Let's use *John the Ripper* to crack the ZIP password, since the necessary data has been collected.<br>`john pw.hash --wordlist=pwlist.txt`<br>Bingo! Password cracked!|<img width="904" height="310" alt="image" src="https://github.com/user-attachments/assets/c07e8e53-ca19-4153-a4fa-49b31bb57964" />|
|6. Finally, extract and read the flag.<br>`unzip f14g.zip`<br>Enter the cracked password, and *f14.txt* will be extracted.<br>`cat f14.txt` <br><br>🎉 Congratulations! You found the flag.|<img width="461" height="189" alt="image" src="https://github.com/user-attachments/assets/05d259a7-54cc-4056-b5ee-3a396d11bba6" />|

