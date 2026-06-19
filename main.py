#run: python3 main.py
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
    
    root = tk.Tk()
    root.title("Sort by Extension")
    root.geometry("1000x200")

    source_folder_entry = ttk.Entry(root, width=100)
    source_folder_entry.grid(row=0, column=1, padx=20, pady=5, sticky="w")
    source_folder_button = ttk.Button(root, text="Add Source Folder", command=lambda: add_source_folder(source_folder_entry))
    source_folder_button.grid(row=0, column=0, padx=20, pady=5, sticky="w")

    dest_folder_entry = ttk.Entry(root, width=100)
    dest_folder_entry.grid(row=1, column=1, padx=20, pady=5, sticky="w")
    dest_folder_button = ttk.Button(root, text="Add Destination Folder", command=lambda: add_dest_folder(dest_folder_entry))
    dest_folder_button.grid(row=1, column=0, padx=20, pady=5, sticky="w")

    options = [".png", ".jpg", ".docx", ".pdf"]
    dropdown = ttk.Combobox(root, width=15, values=options)
    dropdown.grid(row=2, column=0, padx=20, pady=5, sticky="w")
    dropdown.insert(0, "(Select File Type)")
    
    run_button = ttk.Button(root, text="Run", command=lambda: run(dropdown, source_folder_entry, dest_folder_entry))
    run_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    
    root.mainloop()

def add_source_folder(source_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    source_folder_entry.insert(0, folder_path)

def add_dest_folder(dest_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    dest_folder_entry.insert(0, folder_path)

def run(dropdown, source_folder_entry, dest_folder_entry):
    file_type_selection = dropdown.get()
    source_folder = source_folder_entry.get()
    dest_folder = dest_folder_entry.get()

main()