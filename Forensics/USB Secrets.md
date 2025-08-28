# JPEG++.zip

- **Category**: Forensics  
- **Solution**: mount usb.img your strage and read the flag.


| Step | Screenshot |
|------|------------| 
|1. Download usb.img to your preferred location.<br>Based on the `usb` or `img`, it appears to be a USB image file.<br>As planned, inspect the file using WSL or a VM.<br>`file usb.img`<br><br>The file analysis indicates that the image uses a DOS-style MBR and contains one active FAT32 (LBA) partition with ID `0x0c`.<br>[FAT32 reference](https://zenn.dev/hidenori3/articles/3ce349c02e79fa) |<img width="719" height="60" alt="image" src="https://github.com/user-attachments/assets/e8b029d0-2bcd-4798-b239-2e5bb76ad27a" />|
|2. Let's examine the structure of the image using [mmls](https://www.kazamiya.net/Sleuthkit/mmls)<br>`mmls usb.img`<br>From the result, we can see that a FAT32 partition starts at sector 8.<br>This offset will be used to mount the filesystem or extract embedded files.|<img width="544" height="166" alt="image" src="https://github.com/user-attachments/assets/6572fe09-4e67-41b4-8e57-5053bf450766" />|
|3. Try mounting the image.<br>According to `mmls`, the FAT32 partition starts at sector 8.<br>Multiply by 512 to get the byte offset: 8 × 512 = 4096.<br>Use this offset to mount the partition:<br>`sudo mount -o loop,offset=4096 usb.img /mnt`<br>`cd /mnt`<br>`ls -la ./*`<br>We searched through the mounted directories and discovered a suspicious file named `$REFORGED.tx` inside the [$RECYCLE.BIN](https://learn.microsoft.com/ja-jp/style-guide/a-z-word-list-term-collections/r/recycle-bin) folder.|<img width="475" height="323" alt="image" src="https://github.com/user-attachments/assets/e2194db8-331b-42cb-b9a5-c9b5bb79f46f" />|
|4. Then read the flag.<br>`cat '$RECYCLE.BIN/$RFOEVGE.txt'` <br><br>🎉 Congratulations! You found the flag.<br>※Remember to umount.<br>sudo umount /mnt|<img width="552" height="67" alt="image" src="https://github.com/user-attachments/assets/f035e0c5-0442-4a7f-8187-b9fd8fc194d1" />|
|5. Cheat Mode (Not Recommended 😴)<br>`strings usb.img`<br><br>There are many ways to solve this challenge. Try your own way. Here are some useful tools for reference<br>GUI:FTK,autopsy <br>CUI:binwalk,foremost|<img width="265" height="100" alt="image" src="https://github.com/user-attachments/assets/ca670256-3bb3-45d6-a6d2-10a57bd145d3" /><img width="451" height="103" alt="image" src="https://github.com/user-attachments/assets/9e398175-ae72-45cb-ba66-cb7cc4ca56be" />|
