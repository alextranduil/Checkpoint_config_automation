# Checkpoint Router Automation
This Python-based project automates the restoration of Checkpoint router configurations, a task commonly performed after university lab sessions.

### Situation
There are 12 old Checkpoint UTM-1 EDGE W routers. After students complete their labs, the routers need to be restored to their default state.

This script automates the process of restoring the router to a simple, default configuration.

## Setup Instructions
### Quick Start
To get started quickly, download the `CheckpointConfig.exe` file from the latest release and run it.

### Source Code
Clone the repository:

    git clone https://github.com/alextranduil/Checkpoint_config_automation.git

Navigate into the project directory.

Set up a **virtual environment** and install the required packages:

    pip install -r requirements.txt

### Building the Project
To build the executable yourself using PyInstaller:
  
  Install PyInstaller:
  
    pip install pyinstaller
  Run the build command:
    
    pyinstaller --onefile main.py

## Checkpoints and their Recovery

Unfortunately, the "Import Settings" feature does not work, likely because the router's software is outdated.

<img width="1855" height="904" alt="image" src="https://github.com/user-attachments/assets/10be3325-1072-4059-a51a-f370c8b2d93b" />


**To reset a Checkpoint router, you must perform a hardware reset:**
- Long-press the 'RESET' button.

<img width="1280" height="187" alt="image" src="https://github.com/user-attachments/assets/760a5c76-e789-427a-8859-11c82f3f80c1" />

- Wait until the router has finished resetting. The green LED will turn on, as shown in the image below.

![Checkpoint_green_light](https://github.com/user-attachments/assets/03630a3a-a8a5-4b78-af78-3b8ded66b1c4)

- Connect an Ethernet cable from your computer to one of the router's LAN ports.
- Run the script to begin the automated configuration.

## GUI

The user interface, built with **Tkinter**, provides a simple program window for entering the router's parameters (to install ChromeWebDriver). This GUI also allows you to set a new WiFi name for the Checkpoint router and displays a live log of the configuration process in an auto-scrolling text area.

<img width="644" height="644" alt="image" src="https://github.com/user-attachments/assets/4e3b7291-19f6-49d6-a4b5-db16840fc8f0" />
