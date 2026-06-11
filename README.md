# Lucky Scoops 🍦

Lucky Scoops is a complete, windowed desktop app written in Python using Tkinter. It features an interactive multi-screen game interface bundled inside a pastel-pink theme. The application lets users run bulk simulation orders across three unique mini-games, saving everything automatically to a local database.

## 🚀 Download the Application

You do not need Python or PyCharm installed to run this app! **Please note: this is a Windows application only**

1. Go to the [Lucky Scoops Releases Page](https://github.com/clarissa-dev-codes/LuckyScoop/releases/tag/v1.0) on GitHub.
2. Download the **`LuckyScoops_v1.0.zip`** folder.
3. Extract the zip file on your computer.
4. Double-click **`LuckyScoops.exe`** to launch the app!

---

## 📦 Business Stream Operations

This application mirrors the exact inventory management workflows used by modern viral stream businesses (such as Instagram and TikTok "Scoop & Sort" storefronts). It automates the process of scooping material mixes, counting prize results, and checking for reward multipliers:

* **Lucky Scoop 🍦:** Mimics a custom order fill. You type in how many scoops the customer purchased, and the app simulates a physical scoop drop (gathering 15–30 random items per scoop). It totals the prize count for the customer while lowering your live stock.
* 
* **Lucky Roll 🎲:** Handles lucky number bonus rounds. Enter the number of items rolled. The system draws 3 winning digits. If a customer's drawn item carries a matching lucky number, it automatically rewards them with a free extra item.
* 
* **Get One More 🎟️:** Handles lucky color bonus rounds. Enter the order volume. The app draws a random target lucky color. If any items in the customer's scoop match that accent color, they are automatically awarded a free extra item.


---

## ✨ Features

* **Multi-Screen Navigation:** Fluent frame swapping inside a unified layout envelope. No messy sub-windows.
* **Bulk Processing Operations:** Custom numeric entries to run large-scale games or mass restock items instantly.
* **Smart Asset Auto-Generation:** Streamlined entry forms that automatically calculate a random lucky digit (0–9) and pick an accent theme color trait from a curated pastel palette list.
* **Safe Input Validation:** Full database blockades that completely prevent negative inventory counts or empty text entry crashes.
* **Persistent Local Storage:** Reads and writes tracking parameters instantly to a local, human-readable `inventory.json` file.
* **Quality of Life Hooks:** Keyboard shortcut bindings allowing swift `[Enter]` form submissions.

---

## 🛠️ File Architecture

The project splits frontend structural visual layers clean away from storage backend operation math models:

* **`main.py`** - Manages the graphical layout environment, views, frame states, popup systems, and button click handlers.
* **`inventory.py`** - Defines the underlying `Item` schema model blueprint using Python dataclasses and regulates serialization layers.
* **`LuckyScoop.py`** - Controls the bead selection calculations and real-time inventory count subtraction loops.
* **`LuckyRoll.py`** - Dictates the dice matching slot-machine calculations and loop extension overrides.
* **`GetOneMore.py`** - Regulates the color-matching lottery queue algorithms.
