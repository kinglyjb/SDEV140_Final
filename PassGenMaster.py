import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip  # Import pyperclip for copying to clipboard

class PassGenMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("PassGen Master")

        # Variables for password options
        self.length_var = tk.StringVar(value="12")
        self.use_uppercase_var = tk.BooleanVar(value=True)
        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_special_var = tk.BooleanVar(value=True)

        # GUI Elements
        self.create_gui()

    def generate_password(self):
        length = int(self.length_var.get())
        uppercase = string.ascii_uppercase if self.use_uppercase_var.get() else ""
        digits = string.digits if self.use_digits_var.get() else ""
        special_chars = string.punctuation if self.use_special_var.get() else ""

        all_chars = string.ascii_lowercase + uppercase + digits + special_chars
        password = ''.join(random.choice(all_chars) for _ in range(length))

        # Display the generated password in the Tkinter window
        self.password_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").split(": ")[1]
        pyperclip.copy(password)

    def clear_password(self):
        self.password_label.config(text="")

    def create_gui(self):
        # GUI Elements
        ttk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=20, pady=20)
        entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)
        entry.grid(row=0, column=1, padx=20, pady=20)

        ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.use_uppercase_var).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Digits", variable=self.use_digits_var).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Special Characters", variable=self.use_special_var).grid(row=3, column=0, padx=20, pady=10, sticky="w")

        ttk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=20)
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Clear", command=self.clear_password).grid(row=6, column=0, columnspan=2, pady=10)

        # Label to display the generated password
        self.password_label = ttk.Label(self.root, text="")
        self.password_label.grid(row=7, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PassGenMaster(root)
    root.geometry("400x450")  # Set the initial size of the window
    root.mainloop()
