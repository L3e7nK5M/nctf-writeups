# Bit tricky SQL

- **Category**: Web  
- **Solution**: Bypass character check → build SQL → crack password

---

| Step | Screenshot |
|------|------------|
| 1. Access the login page. | <img width="600" height="399" alt="image" src="https://github.com/user-attachments/assets/b6a78576-cfa9-4a45-833d-5949600dd717" /> |
| 2. Test a basic SQL injection payload:<br>`' OR 1 = 1 --` (but it fails). | <img width="600" height="152" alt="image" src="https://github.com/user-attachments/assets/478817a1-30a0-4289-a449-2f8465e56ea3" /><br><img width="600" height="75" alt="image" src="https://github.com/user-attachments/assets/77fbfe52-610e-4b84-a96c-47eeadedecee" /> |
| 3. Try to bypass the filter.<br>Check variations like `or`, `and`, `AND` ... finally you find that **`Or` (capital O)** is allowed. | <img width="391" height="133" alt="image" src="https://github.com/user-attachments/assets/f8994442-e981-45b2-ac6e-2e95ccf2b0a4" /><br><img width="600" height="297" alt="image" src="https://github.com/user-attachments/assets/789b117f-28fb-4170-bd25-00309e303653" /> |
| 4. Look carefully, you will find a **HINT** in the page. | <img width="600" height="204" alt="image" src="https://github.com/user-attachments/assets/55f54fd0-354b-4ab1-8c47-1238e6238f31" /> |
| 5. Discover the number of columns:<br>```sql<br>ORDER BY [number] --<br>``` | <img width="600" height="1014" alt="sql1" src="https://github.com/user-attachments/assets/2cf3133b-586a-417e-982f-bdd54d4f660c" /> |
| 6. Identify the database type.<br>The hint says *Lightweight DB* → this app uses **SQLite**. | <img width="858" height="452" alt="image" src="https://github.com/user-attachments/assets/54a6a642-fdbf-4b7e-8e51-8576b9b27116" /> |
| 7. In SQLite, there is no traditional DB name (file-based).<br>So instead of databases, enumerate **table names** using `sqlite_master`. | [SQLite file format reference](https://sqlite.org/appfileformat.html) |


