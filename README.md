
# 🎰 CLICasino - Terminal Casino Game

A full-featured casino game that runs directly in your terminal! Play Crash and Sapper games with persistent money system.

## ⚡ Quick Install

### One-command installation:
```bash
curl -sSL https://raw.githubusercontent.com/vsvs11/CLICasino/main/install.sh | bash
```

### Manual installation:
```bash
wget https://raw.githubusercontent.com/vsvs11/CLICasino/main/install.sh
chmod +x install.sh
./install.sh
```

## 🎮 Features

- **🎲 Crash Game** - Bet on multiplying coefficients(in development)
- **💣 Sapper** - Classic minefield game  
- **💰 Money System** - Persistent balance that saves between sessions
- **🎯 CLI Interface** - Full terminal support, no GUI required
- **💾 Auto-Save** - Your progress is automatically saved

## 🚀 Usage

After installation, run:
```bash
casino
```
or
```bash
clicasino
```

## 🎯 Games Available

### Crash
- Place your bet before the crash
- Cash out at the right moment
- Multiply your money

### Sapper  
- Choose field size: 3x3, 3x4, or 4x4
- Find mines without triggering them
- Win up to 2x your bet

## 📁 Project Structure

```
CLICasino/
├── casino.py          # Main game executable
├── casino_money.txt   # Player balance data
├── install.sh         # Installation script      
└── README.md          # This file
```

## 🔧 Requirements

- Python 3.6+
- Linux or Termux
- Internet connection (for installation only)

## 🛠️ Installation Details

The installer will:
1. Create ~/CLICasino directory
2. Download all necessary files
3. Set up terminal aliases
4. Make scripts executable

## ❓ Support

- GitHub Issues: [vsvs11/CLICasino](https://github.com/vsvs11/CLICasino/issues)
- Email: vs9589394@gmail.com

## 📝 License

MIT License - feel free to modify and distribute!

---

