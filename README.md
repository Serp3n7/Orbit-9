# Orbit-9
**The Ultimate Macro-Controller for Developers & Designers**

![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge) ![Firmware](https://img.shields.io/badge/Firmware-KMK%20%2F%20CircuitPython-blue?style=for-the-badge) ![Hardware](https://img.shields.io/badge/Powered%20By-Seeed%20XIAO%20RP2040-green?style=for-the-badge)

---

## ⚡ Overview
**Orbit-9** is a workflow accelerator designed to replace repetitive keystrokes with single-tap efficiency. It combines a 3x3 mechanical grid with analog rotary control and a real-time OLED dashboard.

Whether you are snapping windows to multitask, controlling your media, or zooming through CAD models, Orbit-9 adapts to your workflow instantly.

## 💎 Key Features
* **Adaptive Intelligence:** 3 distinct layers (Navigation, Media, Design) that switch instantly via the encoder button.
* **Visual Feedback:** OLED display confirms your active mode and knob function.
* **Analog Control:** Precision rotary encoder for Volume, Brightness, and Zoom.
* **Window Management:** Dedicated layer for snapping windows and managing virtual desktops.
* **Developer Ready:** Native macros for VS Code, Git, and CAD tools.

---

## 🎛️ Workflow Modes

### 1. Navigator Mode (Default)
*The Multitasking Command Center.*
* **Knob:** `Volume Control`
* **Row 1:** `Desktop Left` • `Task View` • `Desktop Right`
* **Row 2:** `Snap Left` • `Maximize` • `Snap Right`
* **Row 3:** `Alt-Tab` • `Minimize` • `Screenshot`
* **Best For:** Managing multiple windows, splitting screens, and organizing your workspace.

### 2. Media Studio Mode
*The Entertainment Layer.*
* **Knob:** `Screen Brightness`
* **Keys:** Play, Pause, Next, Mute
* **Best For:** Spotify, YouTube, Background music control.

### 3. Design & Dev Mode (Pro)
*The Power User Suite.*
* **Knob:** `Zoom / Scroll` (Ctrl + Wheel)
* **Top Row:** `Undo` • `Copy` • `Paste`
* **Mid Row:** `Toggle Sidebar` • `Save` • `Command Palette`
* **Bot Row:** `Fit View (F6)` • `Format Code` • `Alt-Tab`

---

## 🛠️ Technical Specifications
| Spec | Detail |
| :--- | :--- |
| **Microcontroller** | Seeed Studio XIAO RP2040 |
| **Switch Matrix** | 3x3 (9 Keys) with Kailh Hotswap Sockets |
| **Display** | 0.96" OLED (SSD1306) |
| **Input Device** | EC11 Rotary Encoder |
| **Firmware** | KMK (CircuitPython) |

---

## 🚀 Quick Start
1.  **Flash:** Drag `CircuitPython.uf2` to the `RPI-RP2` drive.
2.  **Install:** Copy the `kmk` library folder to the `CIRCUITPY` drive.
3.  **Deploy:** Copy the `code.py` from this repo to the drive.
4.  **Use:** Click the knob to cycle modes.

---

## 🔌 Pinout Reference (Rev 1.0)
* **OLED:** `D4` (SDA), `D5` (SCL)
* **Encoder:** `D0`, `D1` (Rotation), `D10` (Switch)
* **Matrix Cols:** `D2`, `D3`, `D6`
* **Matrix Rows:** `D7`, `D8`, `D9`

---

## 📦 Bill of Materials
* 1x Seeed XIAO RP2040
* 1x Orbit-9 PCB
* 9x Kailh MX Hotswap Sockets
* 9x 1N4148 Diodes
* 1x EC11 Rotary Encoder
* 1x SSD1306 OLED Display
* 9x Mechanical Switches & Keycaps

---

## 📄 License
**Orbit-9** is Open Source Hardware.
* **Firmware:** MIT License
* **Hardware Design:** CERN-OHL-W

*Designed with ❤️ by [Your Name]*