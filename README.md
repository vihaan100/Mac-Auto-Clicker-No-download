# 🖱️ macOS Dynamic High-Speed Auto-Clicker

A lightweight, high-performance Python-based auto-clicker built specifically for macOS (optimized for Apple Silicon M1/M2/M3/M4 chips and macOS Sequoia+). It tracks your mouse live across the screen, triggers instantly with a physical toggle key, and allows you to adjust click frequencies dynamically using your arrow keys.

## 🚀 Key Features
* **Live Mouse Tracking:** Spams clicks wherever you move your cursor.
* **Instant Toggle Key:** Uses the backtick key (`` ` `` / `~`) to toggle instantly with zero latency.
* **Dynamic Speed Control:** Use the **UP** arrow key to click faster, and the **DOWN** arrow key to click slower.
* **Native Speed Boost:** Leverages the native Unix shell and `cliclick` to click hundreds of times per second.

---

## 🛠️ Requirements & Installation

Open your **Terminal** application (`Cmd + Space`, type "Terminal", hit Enter) and execute the following setup commands:

### 1. Install Homebrew & Cliclick
```bash
# Install Homebrew (package manager)
/bin/bash -c "\$(curl -fsSL https://githubusercontent.com)"

# Link Homebrew to your Terminal environment
echo 'eval "\$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "\$(/opt/homebrew/bin/brew shellenv)"

# Install the native clicking tool
brew install cliclick
```

### 2. Install Python Dependencies
```bash
# Install the keyboard listening library to the active environment
python3 -m pip install pynput --break-system-packages
```

---

## 🎮 How to Run

1. Open Terminal and navigate to the project directory:
   ```bash
   cd ~/Desktop/mac-autoclicker
   ```
2. Start the script:
   ```bash
   python3 clicker.py
   ```
3. **Controls Menu:**
   * Press **`` ` `` (Backtick)** to turn clicking **ON** or **OFF**.
   * Press **UP ARROW** to increase clicking speed.
   * Press **DOWN ARROW** to slow down clicking speed.
   * Press **ESC** to stop and exit the program entirely.

---

## ⚠️ Mandatory System Permissions
Because this script monitors background keystrokes and controls your mouse hardware, macOS blocks it by default. 

**You must grant Terminal Accessibility permissions:**
1. Run this command in Terminal to bypass hidden nested menus and launch the exact settings pane:
   ```bash
   open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
   ```
2. In the configuration window that opens, switch the toggle next to **Terminal** to **ON** (Blue).
3. If Terminal is missing from the list, click the `+` button, enter your password, go to `Applications > Utilities`, select `Terminal`, and enable its toggle.

---

## 🔍 Troubleshooting & Common Errors

### 1. Error: `ModuleNotFoundError: No module named 'pynput'`
* **Why it happens:** Python is looking for the package in a different directory or environment layer.
* **Fix:** Force installation specifically into your primary environment using:
  ```bash
  python3 -m pip install pynput --break-system-packages
  ```

### 2. Error: `Failed to build pyobjc-core` / PEP 517 Wheel Compilation Failures
* **Why it happens:** Your Mac's default Python installer (`pip`) is outdated and trying to build underlying macOS architecture elements manually from raw code.
* **Fix:** Update your compilation dependencies first, then try again:
  ```bash
  python3 -m pip install --upgrade pip setuptools wheel
  python3 -m pip install pyobjc-core pyobjc-framework-Cocoa pyobjc-framework-Quartz
  python3 -m pip install pynput --break-system-packages
  ```

### 3. Error: `Error: 'cliclick' not found. Install it via homebrew.`
* **Why it happens:** The script is running, but the Homebrew directory path isn't mapped to your terminal config profile yet.
* **Fix:** Manually execute the path mapping strings:
  ```bash
  echo 'eval "\$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
  eval "\$(/opt/homebrew/bin/brew shellenv)"
  ```

### 4. The script logs `[STARTED]`, but no clicking actually happens
* **Why it happens:** macOS's gatekeeper quarantine system is silently blocking `cliclick` from communicating with your system hardware.
* **Fix:** Lift the internet download quarantine from the program file via Terminal:
  ```bash
  xattr -d com.apple.quarantine /opt/homebrew/bin/cliclick 2>/dev/null || true
  chmod +x /opt/homebrew/bin/cliclick
  ```

### 5. Emergency Stop: The clicker is running out of control and I can't click stop
* **Why it happens:** At hyper-speed, mouse clicks intercept user interface selections before your computer registers a standard trackpad press.
* **Fix:** Press `Cmd + Space` to summon Spotlight, search for **Terminal**, open it, paste this command, and press Enter to kill the engine:
  ```bash
  killall cliclick
  ```

