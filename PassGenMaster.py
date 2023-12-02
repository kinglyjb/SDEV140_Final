import tkinter as tk
from tkinter import ttk
import random
import string

class PassGenMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("PassGen Master")

        # Variables for password options
        self.length_var = tk.StringVar(value="12")
        self.use_uppercase_var = tk.BooleanVar(value=True)
        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_special_var = tk.BooleanVar(value=True)

        # Color Theme
        self.root.configure(bg="#F0F0F0")  # Set background color
        self.button_bg_color = "#4CAF50"  # Green
        self.button_fg_color = "white"

        # GUI Elements
        self.create_gui()

    def generate_password(self):
        length = int(self.length_var.get())
        uppercase = string.ascii_uppercase if self.use_uppercase_var.get() else ""
        digits = string.digits if self.use_digits_var.get() else ""
        special_chars = string.punctuation if self.use_special_var.get() else ""

        all_chars = string.ascii_letters + digits + special_chars
        password = ''.join(random.choice(all_chars) for _ in range(length))

        # Display the generated password in the Tkinter window
        self.password_label.config(text=f"Generated Password: {password}")

    def create_gui(self):
        # Increase font size for a larger GUI
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))
        style.configure("TCheckbutton", font=("Helvetica", 14))  # Set font for Checkbutton
        style.configure("TLabel", font=("Helvetica", 16))  # Set font for Label


        # GUI Elements
        ttk.Label(self.root, text="Password Length:", background="#F0F0F0").grid(row=0, column=0, padx=20, pady=20)
        entry = ttk.Entry(self.root, textvariable=self.length_var, font=("Helvetica", 14), width=5)
        entry.grid(row=0, column=1, padx=20, pady=20)
        entry.config(background="#E0E0E0")  # Set background color for Entry

        ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.use_uppercase_var, style="TCheckbutton").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Digits", variable=self.use_digits_var, style="TCheckbutton").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Special Characters", variable=self.use_special_var, style="TCheckbutton").grid(row=3, column=0, padx=20, pady=10, sticky="w")

        ttk.Button(self.root, text="Generate Password", command=self.generate_password, style="TButton").grid(row=4, column=0, columnspan=2, pady=20)

        # Label to display the generated password
        self.password_label = ttk.Label(self.root, text="", background="#F0F0F0")
        self.password_label.grid(row=5, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PassGenMaster(root)
    root.geometry("400x350")  # Set the initial size of the window
    root.mainloop()
