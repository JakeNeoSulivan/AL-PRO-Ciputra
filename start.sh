#!/bin/bash
pip3 install -r ~/e-voting/requirement.txt 
# Aktifkan lingkungan virtual
source ~/e-voting/env/bin/activate

# Jalankan aplikasi Flask
exec python3 /root/e-voting/app.py

