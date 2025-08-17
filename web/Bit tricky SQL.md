# Bit tricky SQL

- **Category**: Web  
- **Solution**: Bypass Character check then build SQL and password crack

---

| Step | Screenshot |
|------|------------|
| 1. access login page. | <img width="600" height="399" alt="image" src="https://github.com/user-attachments/assets/b6a78576-cfa9-4a45-833d-5949600dd717" /> |
| 2. input SQL `' OR 1 = 1 --` is missed | <img width="600" height="152" alt="image" src="https://github.com/user-attachments/assets/478817a1-30a0-4289-a449-2f8465e56ea3" /> <img width="600" height="75" alt="image" src="https://github.com/user-attachments/assets/77fbfe52-610e-4b84-a96c-47eeadedecee" /> | 
| 3. try to bypass check system <br>or,and,AND ..., then you found the Or is pass the check. | <img width="391" height="133" alt="image" src="https://github.com/user-attachments/assets/f8994442-e981-45b2-ac6e-2e95ccf2b0a4" /><img width="600" height="297" alt="image" src="https://github.com/user-attachments/assets/789b117f-28fb-4170-bd25-00309e303653" />|
| 4. If you look below you will find some HINT. | <img width="600" height="204" alt="image" src="https://github.com/user-attachments/assets/55f54fd0-354b-4ab1-8c47-1238e6238f31" /> |
| 5. first, Try to discover the number of the columns.<br>```ORDER BY [number] -- ```<br>second, Identify table name.(|<img width="600" height="1014" alt="sql1" src="https://github.com/user-attachments/assets/2cf3133b-586a-417e-982f-bdd54d4f660c" />

| 🎉 Congratulations! You got the FLAG.  |
