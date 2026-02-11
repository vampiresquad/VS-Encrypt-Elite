# 🧛 VS-Encrypt-Elite (v4.5)

![Python](https://img.shields.io/badge/Language-Python3-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-green?style=for-the-badge&logo=linux)
![Security](https://img.shields.io/badge/Security-AES--256-red?style=for-the-badge&logo=gnu-privacy-guard)
![Size](https://img.shields.io/badge/Size-Lightweight-orange?style=for-the-badge)

**VS-Encrypt-Elite** is the ultimate Python obfuscation and encryption tool developed by **Vampire Squad**. It is designed to secure your python source codes using military-grade **AES-256 (CBC Mode)** encryption with advanced auto-healing capabilities.

This tool ensures that your code remains safe from reverse engineering while being fully executable on both **Termux (Android)** and **Linux (PC)** environments.

---

## 🔥 Key Features
- **🛡️ AES-256 Encryption:** Protects your code with the highest standard of encryption.
- **💊 Auto-Healing Stub:** The encrypted file automatically detects and installs missing dependencies (`colorama`, `pycryptodome`) on the victim's device.
- **📱 Responsive UI:** Automatically adjusts the interface for Mobile or Desktop screens.
- **🔇 Silent Execution:** No annoying `apt/pkg` warnings during runtime.
- **🧬 Polymorphism:** Generates random variable names for every encryption to bypass static analysis.
- **🚀 One-Click Setup:** Comes with an advanced installer that sets up your entire Termux/Linux environment.

---

## 📸 Installation & Usage

### 1️⃣ For Termux (Android)
Just copy and paste the following commands:

```bash
pkg update && pkg upgrade -y
pkg install git -y
git clone https://github.com/vampiresquad/VS-Encrypt-Elite.git
cd VS-Encrypt-Elite
chmod +x install.sh
bash install.sh
python vampire.py
```
```bash
### 2️⃣ For Linux (Kali/Ubuntu)

sudo apt update && sudo apt install git -y
git clone https://github.com/vampiresquad/VS-Encrypt-Elite.git
cd VS-Encrypt-Elite
chmod +x install.sh
sudo bash install.sh
python3 vampire.py

```
## ⚙️ How It Works
The encryption process of **VS-Encrypt-Elite** involves a multi-layer security approach to ensure maximum protection:

1.  **Source Compilation:** The tool first compiles your raw Python script (`.py`) into bytecode objects.
2.  **Compression & Encoding:** The bytecode is compressed using `zlib` to reduce size and then encoded into `Base64` to handle binary data safely.
3.  **AES-256 Encryption:** The compressed data is encrypted using **AES-256 (CBC Mode)** with a PBKDF2 key derivation function (300,000 iterations), making it virtually impossible to brute-force.
4.  **Stub Generation:** A unique "Stub" code is generated for every encryption. This stub includes:
    * **Auto-Healing Module:** Checks and installs missing dependencies (`colorama`, `pycryptodome`) on the target device automatically.
    * **Anti-Debugging:** Runs the code directly in the system memory (RAM) without writing the decrypted source to the disk.
5.  **Polymorphism:** Variable names in the loader are randomized each time to evade static analysis and antivirus detection.

---

## ⚠️ Disclaimer
**VS-Encrypt-Elite** is developed strictly for **educational purposes** and to help developers protect their intellectual property.

* **Ethical Use:** The author is not responsible for any misuse, damage, or illegal activities caused by this tool.
* **No Warranty:** This tool is provided "as is" without any warranty. Use it at your own risk.
* **Attribution:** If you use this code or part of it in your project, please give proper credit to the original author.

**By using this tool, you agree to these terms.**

---

## 👨‍💻 Author & Credits
This tool is proudly developed and maintained by **Vampire Squad**.

* **Developer:** Muhammad Shourov (V4MPIR3)
* **Team:** Vampire Squad
* **GitHub:** [vampiresquad](https://github.com/vampiresquad)
* **Contact:** vampiresquad.org@gmail.com

---
<div align="center">
  <b>🛡️ Secured by Vampire Squad Technology 🛡️</b>
</div>

