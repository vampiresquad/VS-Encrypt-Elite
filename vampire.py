#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[+] TOOL: Vampire Squad Ultimate Encryptor
[+] VERSION: 4.5 (Stable Fixed Edition)
[+] AUTHOR: Muhammad Shourov (V4MPIR3)
[+] TEAM: Vampire Squad
[+] FEATURES: AES-256, Auto-Healing, Polymorphism, Responsive UI
"""

import os
import sys
import time
import shutil
import marshal
import zlib
import base64
import subprocess
import re
import random
import string
import getpass
import platform
from datetime import datetime

# ==========================================
# [1] BOOTSTRAPPER & DEPENDENCY MANAGER
# ==========================================
def check_core_systems():
    required_modules = ['pycryptodome', 'colorama']
    missing = []
    
    # Check if modules are installed
    try:
        from Crypto.Cipher import AES
        from Crypto.Protocol.KDF import PBKDF2
        from Crypto.Random import get_random_bytes
        from Crypto.Util.Padding import pad, unpad
    except ImportError: missing.append('pycryptodome')

    try:
        from colorama import Fore, Back, Style, init
    except ImportError: missing.append('colorama')

    # If missing, install them automatically
    if missing:
        print("\033[1;33m[!] System Integrity Check Failed. Initializing Auto-Repair...\033[0m")
        print(f"\033[1;34m[*] Installing required components: {', '.join(missing)}\033[0m")
        
        # [UPDATE] Termux & Linux Specific Fixes (No apt warning)
        if os.path.exists('/data/data/com.termux/files/usr/bin/pkg'):
            print("\033[1;36m[*] Termux detected. Configuring environment...\033[0m")
            subprocess.call('pkg install python-pip libcrypt clang -y', shell=True, stdout=subprocess.DEVNULL)
        elif os.path.exists('/usr/bin/apt-get'):
            # Linux fallback
            subprocess.call('sudo apt-get install python3-pip -y', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing], stdout=subprocess.DEVNULL)
            print("\033[1;32m[✓] Core Systems Restored! Restarting Tool...\033[0m")
            time.sleep(1)
            os.execv(sys.executable, ['python3'] + sys.argv)
        except Exception as e:
            sys.exit(f"\033[1;31m[!] Critical Error: Internet Connection Required.\nTrace: {e}\033[0m")

check_core_systems()

# Imports are safe now
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from colorama import Fore, Back, Style, init

init(autoreset=True)

# ==========================================
# [2] CONFIGURATION & BRANDING
# ==========================================
TOOL_NAME = "Vampire Squad Encryption Elite"
TOOL_VERSION = "v4.5 (Stable)"
AUTHOR = "Muhammad Shourov (V4MPIR3)"
TEAM = "Vampire Squad"
GITHUB = "github.com/vampiresquad"
CONTACT = "vampiresquad.org@gmail.com"

# High Security Config
HEADER = b"VS-SECURE"
SALT_SIZE = 16
IV_SIZE = 16
KEY_SIZE = 32
PBKDF2_ITER = 300000  # High iteration for anti-bruteforce

INTRO_MESSAGES = [
    "Initializing Secure Environment...",
    "Vampire Squad: Where cybersecurity meets innovation",
    f"Developed by {AUTHOR}",
    "All praises for Allah, the Most Merciful"
]

# ==========================================
# [3] UI/UX & ANIMATIONS
# ==========================================
class TermUtils:
    @staticmethod
    def width():
        try: return shutil.get_terminal_size().columns
        except: return 80
    
    @staticmethod
    def clear():
        os.system('clear' if os.name == 'posix' else 'cls') # Universal clear
    
    @staticmethod
    def center(text):
        return text.center(TermUtils.width())
    
    @staticmethod
    def print_c(text, color=Fore.WHITE, style=Style.NORMAL):
        print(color + style + TermUtils.center(text) + Style.RESET_ALL)
    
    @staticmethod
    def border(color=Fore.CYAN):
        print(color + "═" * TermUtils.width() + Style.RESET_ALL)
    
    # Tree Style Input Box
    @staticmethod
    def input_box(prompt_text):
        print("\n" + Fore.YELLOW + " [?] " + prompt_text + Style.RESET_ALL)
        return input(Fore.CYAN + "  └──> " + Style.RESET_ALL).strip()

class Animations:
    @staticmethod
    def type(text, color=Fore.CYAN, delay=0.03):
        # Typewriter effect
        for char in TermUtils.center(text):
            sys.stdout.write(color + char + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def loading(label="Processing", color=Fore.GREEN, total=25):
        # Professional Loading Bar [Responsive]
        width = TermUtils.width()
        bar_w = min(width - len(label) - 15, 30)
        if bar_w < 5: bar_w = 10 # Safety for small screens
        
        for i in range(total + 1):
            percent = i / total
            filled = int(bar_w * percent)
            bar = f"[{'█' * filled}{'░' * (bar_w - filled)}]"
            sys.stdout.write(f"\r{color}" + TermUtils.center(f"{label} {bar} {int(percent * 100)}%") + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.04)
        print()

class Graphics:
    @staticmethod
    def logo():
        # Responsive Logo Detection
        w = TermUtils.width()
        TermUtils.border(Fore.RED)
        
        if w < 50: # Mobile View
            art = [
                "V A M P I R E",
                "S  Q  U  A  D",
                f"ENCRYPTOR {TOOL_VERSION}"
            ]
            for line in art:
                TermUtils.print_c(line, Fore.RED, Style.BRIGHT)
        else: # PC/Tablet View
            art = [
                r" ______                             _            ",
                r"|  ____|                           | |           ",
                r"| |__   _ __   ___ _ __ _   _ _ __ | |_ ___ _ __ ",
                r"|  __| | '_ \ / __| '__| | | | '_ \| __/ _ \ '__|",
                r"| |____| | | | (__| |  | |_| | |_) | ||  __/ |   ",
                r"|______|_| |_|\___|_|   \__, | .__/ \__\___|_|   ",
                r"                         __/ | |                 ",
                r"                        |___/|_|                 "
            ]
            for line in art:
                TermUtils.print_c(line, Fore.RED, Style.BRIGHT)
                
        TermUtils.border(Fore.RED)

    @staticmethod
    def info_box():
        w = TermUtils.width()
        bw = min(w - 4, 56)
        
        info = [
            f"TOOL: {TOOL_NAME}",
            f"AUTHOR: {AUTHOR}",
            f"TEAM: {TEAM}",
            f"GITHUB: {GITHUB}"
        ]
        
        print(Fore.GREEN + f"┌{'─'*bw}┐".center(w))
        for line in info:
            pad = bw - 2 - len(line)
            print(Fore.GREEN + f"│ {Fore.WHITE}{line}{' '*pad} {Fore.GREEN}│".center(w))
        print(Fore.GREEN + f"└{'─'*bw}┘".center(w) + Style.RESET_ALL)

# ==========================================
# [4] CORE CRYPTO ENGINE
# ==========================================
class CryptoEngine:
    @staticmethod
    def encrypt(data, password):
        salt = get_random_bytes(SALT_SIZE)
        key = PBKDF2(password, salt, dkLen=KEY_SIZE, count=PBKDF2_ITER)
        iv = get_random_bytes(IV_SIZE)
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        
        return HEADER + salt + iv + ciphertext

    @staticmethod
    def generate_random_var(length=8):
        # Polymorphism: Random variable names
        return '_' + ''.join(random.choices(string.ascii_letters, k=length))

# ==========================================
# [5] MAIN BUILDER LOGIC
# ==========================================
def run_encryptor():
    TermUtils.clear()
    Graphics.logo()
    Graphics.info_box()
    print("\n")
    TermUtils.print_c("=== SECURE COMPILER MODE ===", Fore.RED, Style.BRIGHT)
    print("\n")

    inp_path = TermUtils.input_box("Enter Python File Path").replace('"', '')

    if not os.path.exists(inp_path):
        TermUtils.print_c("[!] File not found!", Fore.RED)
        time.sleep(2); return

    # Smart Filename Logic
    out_name_input = TermUtils.input_box("Output File Name")
    if out_name_input.endswith('.py'):
        out_name = out_name_input
    else:
        out_name = out_name_input + ".py"

    password = TermUtils.input_box("Set Encryption Password")

    if not password:
        TermUtils.print_c("[!] Password cannot be empty!", Fore.RED)
        time.sleep(2); return

    try:
        # Step 1: Read Source
        Animations.loading("Reading Source", Fore.BLUE, 10)
        with open(inp_path, "r", encoding="utf-8") as f:
            source = f.read()

        # Step 2: Obfuscation Layer
        Animations.loading("Compiling Logic", Fore.MAGENTA, 15)
        compiled = compile(source, "VAMPIRE_CORE", "exec")
        layer1 = base64.b64encode(zlib.compress(marshal.dumps(compiled)))

        # Step 3: Strong Encryption
        Animations.loading("Encrypting AES-256", Fore.RED, 20)
        encrypted_blob = CryptoEngine.encrypt(layer1, password)
        
        # Safe Storage (Base64 String)
        encrypted_blob_str = base64.b64encode(encrypted_blob).decode('utf-8')

        # Step 4: Generating Polymorphic Stub
        v_blob = CryptoEngine.generate_random_var()
        v_pass = CryptoEngine.generate_random_var()
        v_key = CryptoEngine.generate_random_var()
        v_dec = CryptoEngine.generate_random_var()
        v_aes = CryptoEngine.generate_random_var()

        # [CRITICAL UPDATE] Fixed Stub with Dependencies, apt-get & Global Scope
        stub_code = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encrypted by {TOOL_NAME}
import sys, subprocess, base64, zlib, marshal, getpass, time, os, shutil

# --- SILENT BOOTSTRAPPER (Target Machine) ---
def _check_install(lib):
    try: __import__(lib)
    except ImportError:
        # Termux Fix
        if os.path.exists('/data/data/com.termux/files/usr/bin/pkg'):
            subprocess.call('pkg install python-pip libcrypt clang -y', shell=True, stdout=subprocess.DEVNULL)
        # Linux Fix (Stable CLI)
        elif os.path.exists('/usr/bin/apt-get'):
            subprocess.call('sudo apt-get install python3-pip -y', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib], 
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Auto-fix Crypto & Colorama on first run
_check_install('pycryptodome')
_check_install('colorama')

# [FIX] Import colorama globally
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    from Crypto.Cipher import AES
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Util.Padding import unpad
except:
    sys.exit("Error: Security libraries missing. Check internet connection.")

# --- ENCRYPTED PAYLOAD ---
{v_blob} = base64.b64decode("{encrypted_blob_str}")

def run_secure():
    # Helper for UI
    def _line(): 
        try: w = shutil.get_terminal_size().columns
        except: w = 50
        print("\\033[1;36m" + "─" * w + "\\033[0m")
    
    os.system('clear' if os.name == 'posix' else 'cls')
    _line()
    print("\\n\\033[1;31m  [+] VAMPIRE SQUAD PROTECTED FILE\\033[0m")
    print("\\033[1;30m  [+] Security Level: AES-256 (High)\\033[0m\\n")
    _line()
    
    try:
        # Secure Password Prompt
        print("\\n\\033[1;33m [?] Enter Access Password:\\033[0m")
        {v_pass} = getpass.getpass("\\033[1;36m  └──> \\033[0m").strip()
        
        # Slicing Data
        _h = {len(HEADER)}; _s = {SALT_SIZE}; _i = {IV_SIZE}
        
        if len({v_blob}) < _h + _s + _i: sys.exit("Error: File Integrity Check Failed.")

        salt = {v_blob}[_h:_h+_s]
        iv = {v_blob}[_h+_s:_h+_s+_i]
        ct = {v_blob}[_h+_s+_i:]
        
        # Key Derivation & Decryption
        {v_key} = PBKDF2({v_pass}, salt, dkLen={KEY_SIZE}, count={PBKDF2_ITER})
        {v_aes} = AES.new({v_key}, AES.MODE_CBC, iv)
        {v_dec} = unpad({v_aes}.decrypt(ct), AES.block_size)
        
        print("\\n\\033[1;32m [✓] Access Granted. Launching...\\033[0m\\n")
        time.sleep(0.5)
        
        # [FIX] Execution with globals() to support Fore/Style
        exec(marshal.loads(zlib.decompress(base64.b64decode({v_dec}))), globals())

    except ValueError:
        print("\\n\\033[1;31m[!] ACCESS DENIED: Incorrect Password!\\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\\n\\033[1;31m[!] Execution Error: {{e}}\\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    run_secure()
"""

        # Write Output
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(stub_code)
        
        # Make Executable
        os.system(f"chmod +x {out_name}")

        Animations.loading("Finalizing", Fore.GREEN, 10)
        print("\n")
        TermUtils.print_c(f"[✓] SUCCESS! Encrypted Tool Saved: {out_name}", Fore.GREEN, Style.BRIGHT)
        TermUtils.print_c(f"Run using: python {out_name}", Fore.CYAN)
        print("\n")
    
    except Exception as e:
        TermUtils.print_c(f"[!] Error: {str(e)}", Fore.RED)

    input(TermUtils.center("Press Enter to return..."))

# ==========================================
# [6] MENU SYSTEM
# ==========================================
def intro_sequence():
    TermUtils.clear()
    for msg in INTRO_MESSAGES:
        Animations.type(msg, Fore.CYAN, 0.02)
        time.sleep(0.3)
    
    TermUtils.clear()
    Graphics.logo()
    Graphics.info_box()
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Animations.type(f">> SYSTEM ONLINE AT {current_time} <<", Fore.GREEN, 0.02)
    time.sleep(1)

def main_menu():
    intro_sequence()
    while True:
        TermUtils.clear()
        Graphics.logo()
        Graphics.info_box()
        print("\n")
        
        TermUtils.border(Fore.CYAN)
        TermUtils.print_c("MAIN MENU", Fore.YELLOW, Style.BRIGHT)
        TermUtils.border(Fore.CYAN)
        
        # Menu Options
        TermUtils.print_c("[1] Encrypt Python File (AES-256)", Fore.GREEN)
        TermUtils.print_c("[2] Join Vampire Squad (Exit)", Fore.RED)
        TermUtils.border(Fore.CYAN)
        
        # Tree Input
        choice = TermUtils.input_box("Select Option")
        
        if choice == '1':
            run_encryptor()
        elif choice == '2':
            TermUtils.clear()
            Animations.type("Shutting down... Stay Ethical.", Fore.RED)
            break
        else:
            TermUtils.print_c("[!] Invalid Option", Fore.RED)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
