# Lucky Scoops (Not finished)

Lucky Scoops is a modern, windowed desktop application built in Python using Tkinter. It features a complete multi-screen system disguised in a beautiful pastel-pink theme. The application tracks, processes, and maintains product stocks using custom C++ style structs bridged into a local JSON database system.

## ✨ Features

* **Multi-Screen Navigation:** Fluent frame swapping inside a unified layout envelope.
* **Database Tracking System:** Uses a custom C++ style structure to track product Name, Price, Lucky Number, Color, and Quantity.
* **Bulk Processing Operations:** Custom numerical popup windows (`tk.Toplevel`) to handle mass restocks or item sales, built with safe input validation to completely prevent negative inventory numbers.
* **Smart Data Entry Auto-Generation:** Streamlined creation dashboard that automatically calculates random lucky numbers (1–100) and extracts beautiful accent color traits from a curated palette list.
* **Persistent Local Storage:** Reads and writes instantly to a localized `inventory.json` file.
* **Quality of Life Hooks:** Keyboard shortcut bindings allowing swift `[Enter]` submissions on interactive forms.

---

## 🛠️ File Structure

The project decouples frontend structural code layers clean away from storage backend operations:

* **`main.py`** - Manages the graphical layout environment, views, frame states, popup systems, validation controls, and user interactions.
* **`inventory.py`** - Defines the underlying `Item` schema model blueprint using Python dataclasses, handles file I/O operations, and regulates serialization layers.
* **`inventory.json`** - The storage file where inventory entries are safely kept.

---
<!--
## 🚀 Getting Started

### Prerequisites
You only need Python 3.x installed on your computer. This application uses standard Python modules, meaning no extra environment setup or `pip install` setups are required.


### Installation & Execution
1. Clone this repository to your local directory:
   ```bash
   git clone https://github.com
   ```
2. Navigate directly into the project folder workspace:
   ```bash
   cd Lucky-Scoops
   ```
3. Run the primary window layout:
   ```bash
   python main.py
   ```

---

## 🎮 How To Use

1. **Main Menu:** Explore interactive game buttons or click **Open Inventory** in the top corner.
2. **Add New Products:** Type in a product name, price, and initial count at the bottom form, then click **Add Item**. The application will automatically assign a random lucky number and theme color trait.
3. **Select Grid Data:** Click any item row entry inside the scrollable tracker view.
4. **Modify Assets:** Click **Bulk Restock** or **Bulk Sell**, type your desired quantity adjustments into the popup field, and hit `[Enter]` on your keyboard or click confirm.
5. **Full Database Erasure:** Cleanly remove data profiles entirely out of file memory by highlighting a row and clicking the **Delete Item** action.

--->
