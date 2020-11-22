setup:
	@echo "[*] Installing dependencies..."
	@python3 -m pip install -r requirements.txt --user
	@echo "[+] Dependencies installed"
	@echo "[*] Setting up..."
	@chmod +x follow_ios_devs.py
	@echo "[+] Installation complete"
	@echo "Start the script by entering the following: ./follow_ios_devs.py"
