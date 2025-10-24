#  CyberRef – URL Safety Analyzer

CyberRef is a **desktop application built with PySide6** that allows users to analyze website URLs using the **VirusTotal API**.  
It provides a modern graphical interface for scanning URLs, checking for malicious activity, viewing community votes, web trackers, and outgoing links — all in a clean, user-friendly windowed environment.

<img width="224" height="300" alt="CyberRefLogo" src="https://github.com/user-attachments/assets/3adfd06e-7ee7-400e-9512-5f415a8e7ab9" />

---

##  Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Example Output](#example-output)
- [Contributors](#contributors)
- [License](#license)

---

##  Overview

CyberRef uses the [VirusTotal API v3](https://developers.virustotal.com/reference/overview) to inspect URLs and summarize their reputation.  
It fetches:

- **Analysis stats** (Harmless / Malicious / Suspicious counts)
- **Community votes**
- **Outgoing links**
- **Detected web trackers**

These are displayed in a **PySide6 GUI** featuring three main windows:
- **Main Window** – User inputs (URL and API key)
- **Info Window** – Displays app info/help
- **Results Window** – Displays scan results

---

##  Features

- Input validation for URL and API key  
- Integration with **VirusTotal API**  
- Displays:
  - Harmless, Malicious, and Suspicious analysis counts
  - Community voting statistics
  - Outgoing links
  - Web trackers  
- Custom PySide6-based GUI with themed elements and icons
- Navigation between Main, Info, and Results windows
- Error dialogs for invalid inputs

---

##  Installation

###  Clone the repository
```bash
git clone https://github.com/PantelisZara/CyberRef.git
cd CyberRef
```
###  Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install required dependencies
```bash
pip install -r requirements.txt
```
## Usage
Run the application
```bash
python main.py
```
### Enter:

- A URL to scan
- Your VirusTotal API key

### Click Start to begin analysis.

Once the scan is complete, the results Window will show : 

- Scan stats (Harmless / Malicious / Suspicious)
- Community votes
- Outgoing links
- Web trackers
  
 You can then go back or exit using on-screen buttons.

 ## Configuration
 You need a VirusTotal API key:

1. Create an account at [virustotal.com](https://www.virustotal.com/gui/home/url)
2. Retrieve your API key from your profile.
3. Enter it in the application when prompted.

## Example Output


https://github.com/user-attachments/assets/e5ff4189-f9a6-4f62-8d0e-60092c31a1be



## Contributors
- Pantelis Zarakis - Developer & Graphic Designer

## License

This project is licensed under the [MIT License](./LICENSE).  
See the [LICENSE](./LICENSE) file for more details.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
