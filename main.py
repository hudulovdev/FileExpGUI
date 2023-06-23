import tkinter as tk
from tkinter import filedialog
import os

def browse_directory():
    directory_path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Directory")
    if directory_path:
        listbox.delete(0, tk.END)  # Clear the existing list
        for item in os.listdir(directory_path):
            listbox.insert(tk.END, item)

# Create the main window
window = tk.Tk()
window.title("File Explorer")

# Create a button to browse for a directory
browse_button = tk.Button(window, text="Browse", command=browse_directory)

# Create a listbox to display the files and directories
listbox = tk.Listbox(window)

# Add the button and listbox to the window
browse_button.pack(pady=10)
listbox.pack()

# Start the GUI event loop
window.mainloop()
