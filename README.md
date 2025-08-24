<div align="center">
  
# UPCORD - CLI

<div align="center">

![Build](https://img.shields.io/badge/build-stable-28a745?style=for-the-badge&logo=github)
![Platform](https://img.shields.io/badge/platform-Linux-0078D6?style=for-the-badge&logo=linux&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/denoyey/UpCord-CLI?style=for-the-badge&logo=git)
![Language](https://img.shields.io/github/languages/top/denoyey/UpCord-CLI?style=for-the-badge&color=informational)
![Technologies](https://img.shields.io/badge/technologies-Python-yellow?style=for-the-badge&logo=terminal)
![Stars](https://img.shields.io/github/stars/denoyey/UpCord-CLI?style=for-the-badge&color=ffac33&logo=github)
![Forks](https://img.shields.io/github/forks/denoyey/UpCord-CLI?style=for-the-badge&color=blueviolet&logo=github)
![Issues](https://img.shields.io/github/issues/denoyey/UpCord-CLI?style=for-the-badge&logo=github)
![Contributors](https://img.shields.io/github/contributors/denoyey/UpCord-CLI?style=for-the-badge&color=9c27b0)

<br />

<img src="https://api.visitorbadge.io/api/VisitorHit?user=denoyey&repo=UpCord-CLI&countColor=%237B1E7A&style=flat-square" alt="visitors"/>

</div>

</div>

## 🔍 Overview

**UpCord-CLI** is a minimalistic and asynchronous command-line wrapper for the Discord API.  
Built for developers and power users who want to automate downloading the latest version of Discord across platforms with ease.
<p align="left">
  <img src="https://github.com/denoyey/UpCord-CLI/blob/main/img/Review-Tools.png" alt="UpCord CLI Screenshot"/>
</p>

## 🐍 Python Required

Make sure Python 3 is installed:

- **Linux**: `python3 --version`

## 🔧 Installation
> Clone and install directly
```terminal
git clone https://github.com/denoyey/UpCord-CLI.git
cd UpCord-CLI
python upcord.py
```

## ✨ Features
- Downloads the latest stable Discord client for your platform
- Provides friendly CLI interface with colorful output
- Cross-platform support
- Smart file re-download prompt

## 🧠 How It Works
1. Picks the correct download URL from Discord's API
2. Downloads the latest Discord client version
3. Saves to `output_upcord/` with a versioned filename
4. If the file already exists, it gives you a choice to skip or re-download

## 💡 Use Cases
- Set up Discord across multiple systems quickly
- Automate deployments or testing environments
- Integrate with custom Discord tooling

## 📁 Output Location
All downloads are saved to:
```bash
output_upcord/
```
> Each file is named based on the detected version and file extension.

## 👥 Contributing
Contributions, issues and feature requests are welcome! <br>
Feel free to <a href="https://github.com/denoyey/UpCord-CLI/issues">open an issue</a> or submit a pull request.

## 📄 License
This project is licensed under the **MIT License**.
See <a href="https://github.com/denoyey/UpCord-CLI/blob/main/LICENSE">LICENSE</a> for more information.

## 📫 Contact
For questions, feedback or collaboration:
- GitHub: <a href="https://github.com/denoyey">@denoyey</a>
- Project: <a href="https://github.com/denoyey/UpCord-CLI">UpCord-CLI</a>
