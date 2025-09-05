# Hidden Stream

- **Category**: Forensics  
- **Solution**: exit zip file in the [ADS](https://cybersecurity-jp.com/security-words/99767) using [FTK imager](https://muchipopo.com/forensic/memorydump/)


| Step | Screenshot |
|------|------------| 
|1. Download `nctf_bakup.dd` to your preferred location.<br>Based on the extension [`dd`](https://qiita.com/gpmrh096/items/70dfdf2a36c0de96d16d), it is a bit-by-bit copy of a disk partition.<br>As planned, inspect the file using WSL or a VM.<br>`file nctf_bakup.dd`<br><br>From the result, the format is Windows [NTFS](https://e-words.jp/w/NTFS.html).|<img width="700" height="74" alt="image" src="https://github.com/user-attachments/assets/c4887713-f3a6-4de7-bbc2-6c5b08d65fb3" />|
|2. There are many ways to analyze this file. This time use FTK Imager.<br>First, add an evidence item and select *image file* as the source, then browse and choose `nctf_bakup.dd`.|<img width="645" height="465" alt="image" src="https://github.com/user-attachments/assets/86d95598-d4f4-417e-b2a3-0fddff9d4bc7" /><img width="504" height="235" alt="image" src="https://github.com/user-attachments/assets/cb1259f1-2e9f-4c28-9c67-7d6755a1cee4" />|
|3. Expanding evidence tree, found suspicious zip file in the jpeg.<br>Export this file to your prefered place.|<img width="297" height="292" alt="image" src="https://github.com/user-attachments/assets/06c4f851-ea17-44b0-b2f1-3463791b9819" /><img width="596" height="322" alt="image" src="https://github.com/user-attachments/assets/e2076456-0842-4bcb-a4bd-d2baa6d40f32" />|
|4. Now that, analyze the jpeg file using `binwalk`<br>||
|4. Then read the flag.<br>`cat '$RECYCLE.BIN/$RFOEVGE.txt'` <br><br>🎉 Congratulations! You found the flag.<br>※Remember to umount.<br>sudo umount /mnt|<img width="552" height="67" alt="image" src="https://github.com/user-attachments/assets/f035e0c5-0442-4a7f-8187-b9fd8fc194d1" />|
