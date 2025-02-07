# 🔐 Image Encryption & Decryption Tool

This project provides a **simple image encryption and decryption tool** using **pixel manipulation** via **Python** and **Bash scripting**. The tool allows users to:

✅ **Encrypt an image** using XOR operations.  
✅ **Decrypt an image** using the same XOR key.  
✅ **Display encrypted and decrypted images** using path-based selection.  

Both **Python** and **Bash** implementations are available for flexibility.

---

## 🚀 Features
- **Encrypt an image** using a user-provided key.
- **Decrypt an image** using the same key.
- **Display encrypted & decrypted images**.
- **Menu-based selection** for easy usage.
- Works on **Linux, Windows, and macOS**.
---

## 📌 Installation & Usage Guide

### Step 1: Download the Script
Clone this repository using Git:
```bash
git clone https://github.com/NIKITATAPALI/PRODIGY_CS_02.git
```
Or manually create the script files:
```bash
nano image_encryption.py  # For Python
nano image_encryption.sh  # For Bash
```
Copy and paste the respective script into the file and save.

### Step 2: Install Required Dependencies
For Python:
```bash
pip install pillow
```

### Step 3: Make the Script Executable (For Bash)
```bash
chmod +x image_encryption.sh
```

### Step 4: Run the Script
For Python:
```bash
python3 image_encryption.py
```
For Bash:
```bash
./image_encryption.sh
```

### Step 5: Choose an Option
1. Encrypt an Image
2. Decrypt an Image
3. Show Encrypted Image
4. Show Decrypted Image
5. Exit

#### Example:
```bash
Choose an option:
1. Encrypt an Image
2. Decrypt an Image
3. Show Encrypted Image
4. Show Decrypted Image
5. Exit
Enter your choice (1/2/3/4/5): 1
Enter the path to the input image: example.png
Enter the path to save the output image: encrypted_example.png
Enter the encryption key (integer): 123
Encryption successful!
```

---

## 🔧 Dependencies
### Python Version:
- `pillow`

### Bash Version:
- Requires `convert` (ImageMagick)

To install ImageMagick:
```bash
sudo apt install imagemagick
```

---

## 🛠 Tested On:
- **Ubuntu**
- **Debian**
- **Kali Linux**
- **Windows (Python version only)**

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Want to contribute? Fork the repo and submit a pull request.

---

## 📢 Find Me On:
<p align="left">
  <a href="https://github.com/NIKITATAPALI/.git" target="_blank"><img src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
</p>

---

## ⚠️ Disclaimer

<i>This project is created for educational purposes only. Unauthorized use of encryption to bypass security measures is illegal. Use this tool responsibly and ensure compliance with applicable laws.</i>

---

### 🎉 Thanks to all contributors!
