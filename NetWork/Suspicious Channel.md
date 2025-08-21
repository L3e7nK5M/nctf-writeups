# Suspicious Channel

- **Category**: Network  
- **Solution**: Solution: Analyze the capture with Wireshark. The traffic is IRC (RFC1459) but running on a non-standard port. Find the chat, then retrieve the flag.
- **HINT**: RFC 1459 — but Non-standard...

---
| Step | Screenshot |
|------|------------|
|1. Open the capture file unknown_port.pcapng in Wireshark.<br>Looking at the packets, but we are not sure.<br>From the protocol hierarchy, various protocols are found, but nothing stands out.So let’s actively use the hint.|<img width="1283" height="480" alt="image" src="https://github.com/user-attachments/assets/d4005f60-26c8-4dc4-9b57-e2d80e651314" /><img width="883" height="364" alt="image" src="https://github.com/user-attachments/assets/b321562b-41f2-4a57-9e39-6328efa230d8" />|
|2. Search for **[RFC 1459](https://solareenlo.com/rfc1459/introduction/index.html)** on Google.<br>It seems like IRC usually uses port 6667|<img width="1234" height="397" alt="image" src="https://github.com/user-attachments/assets/598ebf23-f5fa-4aa8-9d1f-e7eb6791091f" /><img width="774" height="264" alt="image" src="https://github.com/user-attachments/assets/0a9322e7-944d-402c-8db4-b61639b01f82" />|
|3. 3. Return to the packet list and apply a display filter with `tcp.port == 6667`.<br>But we see nothing. This means the IRC traffic is running on a different port. |<img width="796" height="291" alt="image" src="https://github.com/user-attachments/assets/3fe9b2cd-bfa9-498c-8876-4171ee1b9301" />|
|4. Go to **File → Export Objects → IMF** in Wireshark.<br>Save all items.|<img width="819" height="434" alt="image" src="https://github.com/user-attachments/assets/fc21c803-3601-4451-b0c5-9f818634672a" />|
|5. Open the files named <ins>**「test Tue, 01 Jul 2025 15:39:23 -0400」**</ins> and <ins>**「This is important mail」**</ins> with a mail client or text editor.<br>From the first email, you can find the **password**; from the second, you obtain the **zip file**.| <img width="589" height="418" alt="image" src="https://github.com/user-attachments/assets/d1927268-c3eb-47f6-a83a-4f4203b887f2" /> |
|6. Finally, extract the zip file using the password.<br>Both extracted files are identical and contain the same flag.<br><br>🎉 Congratulations! You found the flag.|<img width="649" height="137" alt="image" src="https://github.com/user-attachments/assets/7a68b8e1-de6d-4d48-b463-a2f960e3eab6" /><img width="325" height="103" alt="image" src="https://github.com/user-attachments/assets/73a8236f-fbd7-4ca3-98a3-814c468e5761" />|
