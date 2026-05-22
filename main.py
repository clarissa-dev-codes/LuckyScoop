import tkinter as tk
from tkinter import ttk, messagebox
import random

# Import your struct and functions from your separate inventory.py file
from Inventory import Item, load_inventory, save_inventory


class LuckyScoops:
    def __init__(self, root):
        self.root = root
        self.root.title("Lucky Scoops")
        self.root.geometry("1000x850")  # Slightly taller window to fit the input form

        # Pull the inventory list from your separate backend file
        self.inventory = load_inventory()

        # Color Theme Style
        self.bg_color = "#FFD1DC"
        self.root.configure(background=self.bg_color)

        # Create structural layout frames for the screens
        self.main_screen = tk.Frame(self.root, bg=self.bg_color)
        self.inventory_screen = tk.Frame(self.root, bg=self.bg_color)

        # Build both screen structures
        self.build_main_screen()
        self.build_inventory_screen()

        # Show the main home screen first
        self.show_screen(self.main_screen)

    def show_screen(self, screen_frame):
        """Hides all screens and packs the selected one."""
        self.main_screen.pack_forget()
        self.inventory_screen.pack_forget()
        screen_frame.pack(fill="both", expand=True)

    def build_main_screen(self):
        """Builds your Lucky Scoops main menu."""
        nav_frame = tk.Frame(self.main_screen, bg=self.bg_color)
        nav_frame.pack(fill="x", padx=20, pady=10)

        btn_go_to_inv = tk.Button(
            nav_frame,
            text="📋 Open Inventory",
            font=("Arial", 14),
            command=lambda: self.show_screen(self.inventory_screen),
            padx=10, pady=5
        )
        btn_go_to_inv.pack(side="right")

        self.game_label = tk.Label(self.main_screen, text="Choose option:", font=("Arial", 60), bg=self.bg_color)
        self.game_label.pack(pady=60)

        def action_scoop():
            self.game_label.config(text="You clicked Lucky Scoop")

        def action_roll():
            self.game_label.config(text="You clicked Lucky Roll")

        def action_OneMore():
            self.game_label.config(text="You clicked Get One More")

        btn_scoop = tk.Button(self.main_screen, text="Lucky Scoop", font=("Arial", 16), width=20, command=action_scoop)
        btn_scoop.pack(pady=15)

        btn_roll = tk.Button(self.main_screen, text="Lucky Roll", font=("Arial", 16), width=20, command=action_roll)
        btn_roll.pack(pady=15)

        btn_getMore = tk.Button(self.main_screen, text="Get One More", font=("Arial", 16), width=20,
                                command=action_OneMore)
        btn_getMore.pack(pady=15)

    def build_inventory_screen(self):
        """Builds the inventory database list layout screen."""
        header_frame = tk.Frame(self.inventory_screen, bg=self.bg_color)
        header_frame.pack(fill="x", padx=20, pady=15)

        btn_back = tk.Button(header_frame, text="← Back to Menu", font=("Arial", 12),
                             command=lambda: self.show_screen(self.main_screen))
        btn_back.pack(side="left")

        title = tk.Label(header_frame, text="Inventory Database", font=("Arial", 24, "bold"), bg=self.bg_color)
        title.pack(side="left", padx=30)

        # The Scrollable Grid Table layout
        list_frame = tk.Frame(self.inventory_screen)
        list_frame.pack(padx=40, pady=5, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        cols = ("Name", "Price", "Lucky Num", "Color", "Quantity")
        self.tree = ttk.Treeview(list_frame, columns=cols, show="headings", yscrollcommand=scrollbar.set, height=12)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.tree.yview)

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        # Add New Item Form
        form_frame = tk.LabelFrame(self.inventory_screen,
                                   text=" Add Brand New Stock (Auto-generates Color & Lucky Num) ",
                                   font=("Arial", 12, "bold"), bg=self.bg_color, pady=10)
        form_frame.pack(padx=40, pady=15, fill="x")

        # Form Entry Fields
        tk.Label(form_frame, text="Name:", bg=self.bg_color).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(form_frame, width=15)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Price ($):", bg=self.bg_color).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.entry_price = tk.Entry(form_frame, width=10)
        self.entry_price.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Initial Qty:", bg=self.bg_color).grid(row=0, column=8, padx=5, pady=5, sticky="e")
        self.entry_qty = tk.Entry(form_frame, width=8)
        self.entry_qty.grid(row=0, column=9, padx=5, pady=5)

        btn_create = tk.Button(form_frame, text="➕ Add Item", font=("Arial", 10, "bold"), command=self.add_new_item)
        btn_create.grid(row=0, column=10, padx=15, pady=5)

        # The Stock Modifying Control Buttons (Restock / Sell / Reset)
        btn_frame = tk.Frame(self.inventory_screen, bg=self.bg_color)
        btn_frame.pack(pady=15)

        btn_add = tk.Button(btn_frame, text="Bulk Restock", font=("Arial", 12), width=15, command=lambda: self.open_bulk_window("restock"))
        btn_add.pack(side="left", padx=15)

        btn_sub = tk.Button(btn_frame, text="Bulk Sell", font=("Arial", 12), width=15, command=lambda: self.open_bulk_window("sell"))
        btn_sub.pack(side="left", padx=15)

        btn_reset = tk.Button(btn_frame, text="Reset Stock", font=("Arial", 12), width=15, command=self.reset_stock)
        btn_reset.pack(side="left", padx=15)

        btn_delete = tk.Button(btn_frame, text="Delete Item", font=("Arial", 12), width=15, command=self.delete_item)
        btn_delete.pack(side="left", padx=15)

        self.refresh_table()

    # ==========================================
    # DATABASE & VIEW UPDATING CONTROLS
    # ==========================================
    def refresh_table(self):
        """Updates the interactive spreadsheet component display grid."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for index, item in enumerate(self.inventory):
            self.tree.insert("", "end", iid=index,
                             values=(item.thing, f"${item.price:.2f}", item.luckyNum, item.color, item.quantity))

    def get_selected_item_index(self):
        """Captures active row item highlight arrays."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Missing", "Please select an item from the table first!")
            return None
        return int(selected[0])

    def add_new_item(self):
        """Validates entry forms and injects a brand new Item into database tracking."""
        try:
            # 1. Gather text values from form inputs
            name = self.entry_name.get().strip()
            price_text = self.entry_price.get().strip()
            qty_text = self.entry_qty.get().strip()

            # 2. Validation: Ensure no text fields are blank
            if not name or not price_text or not qty_text:
                messagebox.showerror("Input Error", "All fields must be filled out to add a new item.")
                return

            # 3. Validation: Convert text types to match C++ Struct requirements
            price = float(price_text)
            quantity = int(qty_text)

            random_lucky = random.randint(0,9)

            colors = ("Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Black", "White")
            random_color = random.choice(colors)

            # 4. Construct a new Item instance and append it to our backend tracking array
            new_item = Item(thing=name, price=price, luckyNum=random_lucky, color=random_color, quantity=quantity)
            self.inventory.append(new_item)

            # 5. Save file, refresh spreadsheet, and wipe text boxes clean
            save_inventory(self.inventory)
            self.refresh_table()

            self.entry_name.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.entry_qty.delete(0, tk.END)

            messagebox.showinfo("Success", f"'{name}' has been successfully added to your inventory!")

        except ValueError:
            messagebox.showerror("Data Type Error",
                                 "Please ensure numbers are entered correctly:\n- Price must be a number (ex: 12.50)\n- Lucky Num & Qty must be whole numbers (ex: 7)")

    def open_bulk_window(self, mode):
        idx = self.get_selected_item_index()
        if idx is None:
            return

        item = self.inventory[idx]
        action_title = "Bulk Restock" if mode == "restock" else "Bulk Sell"

        popup = tk.Toplevel(self.root)
        popup.title(action_title)
        popup.geometry("350x200")
        popup.config(bg=self.bg_color)

        popup.grab_set()

        popup.geometry(f"+{self.root.winfo_x() + 320}+{self.root.winfo_y() + 250}")

        lbl_info = tk.Label(
            popup,
            text=f"Item: {item.thing}\nCurrent Stock: {item.quantity}",
            font=("Arial", 12, "bold"), bg=self.bg_color
        )
        lbl_info.pack(pady=15)

        lbl_prompt = tk.Label(popup, text="Enter quantity amount: ", font=("Arial", 10), bg=self.bg_color)
        lbl_prompt.pack()

        entry_amount = tk.Entry(popup, font=("Arial", 12), width=10, justify="center")
        entry_amount.pack(pady=10)
        entry_amount.focus_set()

        def process_bulk():
            try:
                amount = int(entry_amount.get().strip())
                if amount <= 0:
                    messagebox.showerror("Input Error", "Please enter a number greater than 0.", parent=popup)
                    return

                if mode == "restock":
                    self.inventory[idx].quantity += amount
                    save_inventory(self.inventory)
                    self.refresh_table()
                    popup.destroy()

                elif mode == "sell":
                    if item.quantity >= amount:
                        self.inventory[idx].quantity -= amount
                        save_inventory(self.inventory)
                        self.refresh_table()
                        popup.destroy()
                    else:
                        messagebox.showerror(
                            "Shortage Error",
                            f"Not enough stock! You only have {item.quantity} available.",
                            parent=popup
                        )
            except ValueError:
                messagebox.showerror("Data Type Error", "Please a valid whole number.", parent=popup)

        btn_submit = tk.Button(popup, text="Confirm", font=("Arial", 10, "bold"), width=12, command=process_bulk)
        btn_submit.pack(pady=10)
        entry_amount.bind("<Return>", lambda e: process_bulk())

    def reset_stock(self):
        idx = self.get_selected_item_index()
        if idx is not None:
            confirm = messagebox.askyesno("Confirm Reset", f"Are you sure you want to reset {self.inventory[idx].thing}'s stock to 0?")
            if confirm:
                self.inventory[idx].quantity = 0
                save_inventory(self.inventory)
                self.refresh_table()

    def restock_item(self):
        idx = self.get_selected_item_index()
        if idx is not None:
            self.inventory[idx].quantity += 1
            save_inventory(self.inventory)
            self.refresh_table()

    def sell_item(self):
        idx = self.get_selected_item_index()
        if idx is not None:
            if self.inventory[idx].quantity > 0:
                self.inventory[idx].quantity -= 1
                save_inventory(self.inventory)
                self.refresh_table()
            else:
                messagebox.showerror("Out of Stock", "Cannot sell item. Quantity is already 0.")

    def reset_stock(self):
        idx = self.get_selected_item_index()
        if idx is not None:
            confirm = messagebox.askyesno("Confirm Reset",
                                          f"Are you sure you want to reset {self.inventory[idx].thing}'s stock to 0?")
            if confirm:
                self.inventory[idx].quantity = 0
                save_inventory(self.inventory)
                self.refresh_table()

    def delete_item(self):
        idx = self.get_selected_item_index()
        if idx is not None:
            item_name = self.inventory[idx].thing

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                f"Are you sure you want to delete {item_name}?"
            )

            if confirm:
                self.inventory.pop(idx)
                save_inventory(self.inventory)
                self.refresh_table()

                messagebox.showinfo("Deleted", f"{item_name} has been deleted.")


# Run Application
if __name__ == "__main__":
    root_window = tk.Tk()
    app = LuckyScoops(root_window)
    root_window.mainloop()
