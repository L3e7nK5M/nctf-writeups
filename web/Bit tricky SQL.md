# Bit tricky SQL

- **Category**: Web  
- **Solution**: Bypass Character check then build SQL and password crack

---

| Step | Screenshot |
|------|------------|
| 1. access login page. | <img width="442" height="399" alt="image" src="https://github.com/user-attachments/assets/b6a78576-cfa9-4a45-833d-5949600dd717" /> |
| 2. input SQL `' OR 1 = 1 --` is missed | <img width="431" height="152" alt="image" src="https://github.com/user-attachments/assets/478817a1-30a0-4289-a449-2f8465e56ea3" /> <img width="505" height="75" alt="image" src="https://github.com/user-attachments/assets/77fbfe52-610e-4b84-a96c-47eeadedecee" /> | 
| 3. try to bypass check system <br>or,and,AND ..., then you found the Or is pass the check. | <img width="391" height="133" alt="image" src="https://github.com/user-attachments/assets/f8994442-e981-45b2-ac6e-2e95ccf2b0a4" /><img width="552" height="297" alt="image" src="https://github.com/user-attachments/assets/789b117f-28fb-4170-bd25-00309e303653" />|
| 4. If you look below you will find some HINT. | <img width="548" height="217" alt="image" src="https://github.com/user-attachments/assets/34c97c67-1174-45d0-86ef-c9d4532d1fb9" /> |
| 5. try injectiTake the Base64 string and decode it (bash) |```echo "TlRDRntGQEtFX2hhUmRfdG9fUmVhZF9qQXY0NWNSSXB0fQo=" \| base64 -d<br>```
| 🎉 Congratulations! You got the FLAG.  |
