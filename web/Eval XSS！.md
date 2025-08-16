# Eval XSS!

- **Category**: Web  
- **Solution**: Eval XSS  

---

| Step | Screenshot |
|------|------------|
| 1. Open the page source.You will find `main.js`. | <img width="600" height="131" alt="image" src="https://github.com/user-attachments/assets/51802c7f-d2d4-48c5-bf07-5a656aeeb32d" /> |
| 2. Open `main.js` and copy the code.<br>- `eval`: execute the string as code<br>- `atob`: convert Base64 → string |```eval(atob("YWxlcnQoJ1RsUkRSbnRHUUV0RlgyaGhVbVJmZEc5ZlVtVmhaRjlxUVhZME5XTlNTWEIwZlFvPScp"));``` | 
| 3. Press **F12** to open DevTools.<br>Paste the code into the console and run it. | <img width="600" height="183" alt="image" src="https://github.com/user-attachments/assets/0fa0ec05-d93c-4c8e-b81f-4c52da11a0d7" /> |
| 4. The code will show an alert. | <img width="600" height="126" alt="image" src="https://github.com/user-attachments/assets/e6d3475a-0185-4799-b33e-b4dcf5736973" /> |
| 5. Take the Base64 string and decode it (bash) |```echo "TlRDRntGQEtFX2hhUmRfdG9fUmVhZF9qQXY0NWNSSXB0fQo=" \| base64 -d<br>```
| 🎉 Congratulations! You got the FLAG.  |
