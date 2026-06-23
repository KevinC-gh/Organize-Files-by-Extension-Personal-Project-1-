#run: python3 main.py
#cd workspace/bootdev/personal_project_1
import os
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

    dropdown_entry = ttk.Entry(root, width=50)
    dropdown_entry.grid(row=2, column=1, padx=20, pady=5, sticky="w")

    options = [".png", ".jpg", ".docx", ".pdf", ".txt"]
    dropdown = ttk.Combobox(root, width=16, values=options, state="readonly")
    dropdown.grid(row=2, column=0, padx=20, pady=5, sticky="w")
    dropdown.set("Select File Type(s)")
    dropdown.bind("<<ComboboxSelected>>", lambda event: list_selected(event, dropdown, dropdown_entry))

    run_button = ttk.Button(root, text="Run", command=lambda: run(dropdown, source_folder_entry, dest_folder_entry))
    run_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    root.mainloop()

def add_source_folder(source_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    source_folder_entry.insert(0, folder_path)

def add_dest_folder(dest_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    dest_folder_entry.insert(0, folder_path)

def list_selected(_, dropdown, dropdown_entry):
    dropdown_selection = dropdown.get()
    dropdown_entry.insert(tk.END, dropdown_selection)
    dropdown.set("Select File Type(s)")

def run(dropdown, source_folder_entry, dest_folder_entry):
    file_type_selection = dropdown.get()
    source_folder = source_folder_entry.get()
    dest_folder = dest_folder_entry.get()
    
    source_files = os.listdir(source_folder)
    for file in source_files:
        if file.endswith(file_type_selection):
            full_source_path = os.path.abspath(os.path.join(source_folder, file))
            full_dest_path = os.path.abspath(os.path.join(dest_folder, file))
            os.rename(full_source_path, full_dest_path)
            print(f"{file} moved successfully")

main()