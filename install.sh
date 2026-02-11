#!/bin/bash

# Define Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

clear
echo -e "${RED}"
echo "    VS-ENCRYPT-ELITE INSTALLER    "
echo "    --------------------------    "
echo "    Setup by: Vampire Squad       "
echo -e "${NC}"

# Function to check internet
check_internet() {
    echo -e "${YELLOW}[*] Checking Internet Connection...${NC}"
    if ping -q -c 1 -W 1 google.com >/dev/null; then
        echo -e "${GREEN}[✓] Online${NC}"
    else
        echo -e "${RED}[!] Error: No Internet Connection!${NC}"
        exit 1
    fi
}

# Function for Termux Setup
setup_termux() {
    echo -e "${CYAN}[*] Detect: Termux Environment${NC}"
    echo -e "${YELLOW}[*] Updating System (This may take a while)...${NC}"
    
    pkg update -y && pkg upgrade -y
    
    echo -e "${YELLOW}[*] Installing Core Dependencies...${NC}"
    pkg install python git clang libcrypt openssl -y
    pkg install python-pip -y
    
    # Fix for Pillow/Image libraries if needed later
    pkg install libjpeg-turbo libpng -y 
    
    echo -e "${GREEN}[✓] System Environment Ready!${NC}"
}

# Function for Linux Setup
setup_linux() {
    echo -e "${CYAN}[*] Detect: Linux Environment${NC}"
    
    if [ "$(id -u)" != "0" ]; then
        echo -e "${RED}[!] Please run as root (sudo bash install.sh)${NC}"
        exit 1
    fi

    echo -e "${YELLOW}[*] Updating System...${NC}"
    sudo apt-get update && sudo apt-get upgrade -y
    
    echo -e "${YELLOW}[*] Installing Core Dependencies...${NC}"
    sudo apt-get install python3 python3-pip git build-essential libssl-dev libffi-dev python3-dev -y
    
    echo -e "${GREEN}[✓] System Environment Ready!${NC}"
}

# Main Execution
check_internet

if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    setup_termux
    pip install --upgrade pip
    pip install -r requirements.txt
else
    setup_linux
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
fi

# Finalizing
echo -e "${YELLOW}[*] Setting up permissions...${NC}"
chmod +x vampire.py
chmod +x install.sh

echo -e "\n${GREEN}[✓] INSTALLATION COMPLETE!${NC}"
echo -e "${CYAN}Type command: ${YELLOW}python vampire.py${CYAN} to run the tool.${NC}\n"
