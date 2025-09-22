# Suspicious Channel

- **Category**: Network  
- **Solution**: Solution: Analyze the capture with Wireshark. The traffic is IRC (RFC1459) but running on a non-standard port. Find the chat, then retrieve the flag.
- **HINT**: RFC 1459 — but Non-standard...

---
| Step | Screenshot |
|------|------------|
|1. Open the capture file unknown_port.pcapng in Wireshark.<br>Looking at the packets, but we are not sure.<br>From the protocol hierarchy, various protocols are found, but nothing stands out.So let’s actively use the hint:***RFC 1459 — but Non-standard...***|<img width="1283" height="480" alt="image" src="https://github.com/user-attachments/assets/d4005f60-26c8-4dc4-9b57-e2d80e651314" /><img width="883" height="364" alt="image" src="https://github.com/user-attachments/assets/b321562b-41f2-4a57-9e39-6328efa230d8" />|
|2. Search for **[RFC 1459](https://solareenlo.com/rfc1459/introduction/index.html)** on Google.<br>It seems like IRC usually uses port 6667.|<img width="1234" height="397" alt="image" src="https://github.com/user-attachments/assets/598ebf23-f5fa-4aa8-9d1f-e7eb6791091f" /><img width="774" height="264" alt="image" src="https://github.com/user-attachments/assets/0a9322e7-944d-402c-8db4-b61639b01f82" />|
|3. Return to the packet list and apply a display filter with `tcp.port == 6667`.<br>But we see nothing. <br> consider *Non-standard*, This means the IRC traffic is running on a different port. |<img width="796" height="291" alt="image" src="https://github.com/user-attachments/assets/3fe9b2cd-bfa9-498c-8876-4171ee1b9301" />|
|4. Let's take a different approach. Again, google `IRC` and check for some common commands, for example `PRIVMSG`. |<img width="735" height="518" alt="image" src="https://github.com/user-attachments/assets/55573acb-cfaf-41c1-b5fc-bbf52734e456" />|
|5. Try this command to search. <br> In the display filter, set: `frame contains "PRIVMSG"`<br> We found some `PRIVMSG` packets. This time, the IRC communication was running on port **6666** instead of the standard one (6667).<br><br>Let's locate this packet as usual: right-click and **Follow → TCP Stream**.|<img width="1166" height="201" alt="image" src="https://github.com/user-attachments/assets/cac8360f-63ff-4787-8adb-badb1117978b" /><img width="891" height="468" alt="image" src="https://github.com/user-attachments/assets/25168b21-a9ab-418d-9607-b7763f84d964" />|
|6. We found a **NICK/USER** command followed by a `JOIN` to server channel ***#s3cr3t***. Inside the chat, there was an interesting message:<br>**XOR Key: A , Encrypted Flag: DI^LqcXIUIeGGkdnU>DNUi:d^X:;w**<br>It seems like that the flag is encrypted, you may need to decrypt it using the given XOR key.|<img width="921" height="726" alt="image" src="https://github.com/user-attachments/assets/898f1f80-5f1a-4e7c-a600-b570830e8bb1" />|
|7. This is time for Chef!<br>Input:`DI^LqcXIUIeGGkdnU>DNUi:d^X:;w`<br>Operations:`XOR`<br>Recipe: set Key `A`<br><br>🎉 Congratulations! You found the flag.|<img width="1378" height="720" alt="image" src="https://github.com/user-attachments/assets/62a09c29-422d-4821-bd0a-d448087a2524" />|

