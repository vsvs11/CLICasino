#!/bin/bash

# Находим casino.py
CASINO_PATH=$(find $HOME -name "casino.py" -type f | head -n 1)

if [ -z "$CASINO_PATH" ]; then
    echo "Error: casino.py not found!"
    exit 1
fi

echo "Found casino.py at: $CASINO_PATH"

# Добавляем alias в .bashrc
echo "alias casino='python3 \"$CASINO_PATH\"'" >> ~/.bashrc
echo "alias clicasino='python3 \"$CASINO_PATH\"'" >> ~/.bashrc

# Обновляем настройки
source ~/.bashrc

echo "Aliases added successfully!"
echo "Now you can use: casino or clicasino"
