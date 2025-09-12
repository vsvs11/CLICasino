#!/bin/bash

echo "Installing CLICasino..."
echo "Downloading all files..."

# Создаем папку
mkdir -p ~/CLICasino
cd ~/CLICasino

# Скачиваем ВСЕ файлы из репозитория
echo "Downloading casino.py..."
curl -sSL https://raw.githubusercontent.com/vsvs11/CLICasino/main/casino.py -o casino.py

echo "Downloading casino_money.txt..."
curl -sSL https://raw.githubusercontent.com/vsvs11/CLICasino/main/casino_money.txt -o casino_money.txt 2>/dev/null || touch casino_money.txt

echo "Downloading LICENSE..."
curl -sSL https://raw.githubusercontent.com/vsvs11/CLICasino/main/LICENSE -o LICENSE 2>/dev/null || echo "LICENSE not found, skipping"

echo "Downloading README.md..."
curl -sSL https://raw.githubusercontent.com/vsvs11/CLICasino/main/README.md -o README.md 2>/dev/null || echo "README not found, skipping"

# Даем права на выполнение
chmod +x casino.py

# Создаем алиас для запуска
if [[ ! -f ~/.bashrc ]]; then
    touch ~/.bashrc
fi

if ! grep -q "alias casino=" ~/.bashrc; then
    echo "alias casino='python3 ~/CLICasino/casino.py'" >> ~/.bashrc
    echo "Alias added to .bashrc"
fi

echo "Installation complete!"
echo "Type 'casino' to start the game"
echo "Restart terminal or run: source ~/.bashrc"
