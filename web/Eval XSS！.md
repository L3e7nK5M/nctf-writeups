# Eval XSS!

- **Category**: Web  
- **Solution**: Eval XSS  

---

## Steps

1. Open the page source and you will find `main.js`.  
   <img width="430" height="131" alt="image" src="https://github.com/user-attachments/assets/51802c7f-d2d4-48c5-bf07-5a656aeeb32d" />

2. Open `main.js` and copy the following code:  
   ```javascript
   eval(atob("YWxlcnQoJ1RsUkRSbnRHUUV0RlgyaGhVbVJmZEc5ZlVtVmhaRjlxUVhZME5XTlNTWEIwZlFvPScp"));
  - eval: execute the string as code
  - atob: convert Base64 → string

3. Press F12 to open DevTools and paste the code into the console, then run it.
<img width="884" height="183" alt="image" src="https://github.com/user-attachments/assets/0fa0ec05-d93c-4c8e-b81f-4c52da11a0d7" />

4. The code will show an alert.
<img width="445" height="126" alt="image" src="https://github.com/user-attachments/assets/e6d3475a-0185-4799-b33e-b4dcf5736973" />

5. Take the Base64 string and decode it:
echo "TlRDRntGQEtFX2hhUmRfdG9fUmVhZF9qQXY0NWNSSXB0fQo=" | base64 -d

🎉 Congratulations! You got the FLAG. 
