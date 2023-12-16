import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import string
import pyperclip
from datetime import datetime
import os

class PassGenMaster:
    def __init__(self, root):
        """
        Initialize the PassGenMaster class.

        Parameters:
        - root: The root window for the application.
        """
        self.root = root
        self.root.title("PassGen Master")

        # Password history list
        self.password_history = []

        try:
            # Get the directory of the script
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Set the background image using Pillow
            image_path = os.path.join(script_dir, "space.png")
            img = Image.open(image_path)
            background_image = ImageTk.PhotoImage(img)

            background_label = tk.Label(root, image=background_image)
            background_label.image = background_image  # Keep a reference to prevent the image from being garbage collected
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error setting background image: {e}")

        # Variables for password options
        self.length_var = tk.StringVar(value="12")  # Default password length
        self.use_uppercase_var = tk.BooleanVar(value=True)  # Default to include uppercase letters
        self.use_digits_var = tk.BooleanVar(value=True)  # Default to include digits
        self.use_special_var = tk.BooleanVar(value=True)  # Default to include special characters

        # GUI Elements
        self.create_gui()

    def create_gui(self):
        """
        Create the graphical user interface.
        """
        # Label and entry for password length
        ttk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=20, pady=20)
        entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)
        entry.grid(row=0, column=1, padx=20, pady=20)

        # Checkboxes for password options
        ttk.Checkbutton(self.root, text="Include Uppercase", variable=self.use_uppercase_var).grid(row=1, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Digits", variable=self.use_digits_var).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        ttk.Checkbutton(self.root, text="Include Special Characters", variable=self.use_special_var).grid(row=3, column=0, padx=20, pady=10, sticky="w")

        # Buttons for password generation and actions
        ttk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="w")
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="w")
        ttk.Button(self.root, text="Clear", command=self.clear_password).grid(row=6, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        # Label for the generated password
        self.password_label = ttk.Label(self.root, text="")
        self.password_label.grid(row=7, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        # Label for password strength
        self.strength_label = ttk.Label(self.root, text="Password Strength: ")
        self.strength_label.grid(row=8, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        # Progressbar for password strength
        self.strength_progressbar = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, mode='determinate', length=200)
        self.strength_progressbar.grid(row=9, column=0, columnspan=2, pady=10, padx=20, sticky="w")

        # Button to open the second window
        ttk.Button(self.root, text="Password History", command=self.open_second_window).grid(row=10, column=0, columnspan=2, pady=10, padx=20, sticky="w")

    def generate_password(self):
        """
        Generate a password based on user options.
        """
        length = int(self.length_var.get())
        uppercase = string.ascii_uppercase if self.use_uppercase_var.get() else ""
        digits = string.digits if self.use_digits_var.get() else ""
        special_chars = string.punctuation if self.use_special_var.get() else ""

        all_chars = string.ascii_lowercase + uppercase + digits + special_chars
        password = ''.join(random.choice(all_chars) for _ in range(length))

        # Display the generated password
        self.password_label.config(text=f"Generated Password: {password}")

        # Update the password strength meter
        self.update_strength_meter(password)

        # Add the generated password to the history
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history_entry = f"{timestamp}: {password}"
        self.password_history.append(history_entry)

        # Update the password history listbox in the second window
        if hasattr(self, 'history_listbox'):
            self.history_listbox.insert(tk.END, history_entry)

    def copy_to_clipboard(self):
        """
        Copy the generated password to the clipboard.
        """
        password = self.password_label.cget("text").split(": ")[1]
        pyperclip.copy(password)

    def clear_password(self):
        """
        Clear the displayed password.
        """
        self.password_label.config(text="")

    def update_strength_meter(self, password):
        """
        Update the password strength meter.
        """
        # Simulate password strength calculation
        strength = len(password) * 10
        
        # Cap the strength at a maximum of 100%
        strength = min(strength, 100)

        self.strength_label.config(text=f"Password Strength: {strength}%")
        self.strength_progressbar['value'] = strength

    def copy_selected_password(self):
        """
        Copy a selected password from the history listbox to the clipboard.
        """
        selected_index = self.history_listbox.curselection()
        if selected_index:
            selected_password = self.password_history[selected_index[0]].split(": ")[1]
            pyperclip.copy(selected_password)

    def open_second_window(self):
        """
        Open the second window displaying password history.
        """
        second_window = tk.Toplevel(self.root)
        second_window.title("Password History")

        # Set the geometry of the second window to match the first window
        second_window.geometry(self.root.geometry())

        # Frame to organize widgets in the second window
        frame = ttk.Frame(second_window)
        frame.pack(fill=tk.BOTH, expand=True)

        # Password history listbox
        history_label = ttk.Label(frame, text="Password History:")
        history_label.pack()

        self.history_listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
        self.history_listbox.pack(fill=tk.BOTH, expand=True)

        # Copy to clipboard button
        copy_button = ttk.Button(frame, text="Copy to Clipboard", command=self.copy_selected_password)
        copy_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PassGenMaster(root)
    root.geometry("500x500")
    root.mainloop()
