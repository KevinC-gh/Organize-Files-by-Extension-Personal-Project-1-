#run: python3 main.py
#cd workspace/bootdev/personal_project_1
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
    
    root = tk.Tk()
    root.title("Sort by Extension")
    root.geometry("1100x400")
    bg_color = "LightBlue2"
    root.configure(bg=bg_color)

    source_folder_entry = ttk.Entry(root, width=100)
    source_folder_entry.grid(row=0, column=1, padx=20, pady=5, sticky="w")
    source_folder_button = ttk.Button(root, text="Add Source Folder", 
                                      command=lambda: add_source_folder(source_folder_entry))
    source_folder_button.grid(row=0, column=0, padx=20, pady=5, sticky="w")

    dest_folder_entry = ttk.Entry(root, width=100)
    dest_folder_entry.grid(row=1, column=1, padx=20, pady=5, sticky="w")
    dest_folder_button = ttk.Button(root, text="Add Destination Folder", 
                                    command=lambda: add_dest_folder(dest_folder_entry))
    dest_folder_button.grid(row=1, column=0, padx=20, pady=5, sticky="w")

    dropdown_textbox = tk.Text(root, width=6, height=1)
    dropdown_textbox.grid(row=2, column=1, padx=20, pady=5, sticky="w")

    options = [".png", ".jpg", ".docx", ".pdf", ".txt"]
    dropdown = ttk.Combobox(root, width=16, values=options, state="readonly")
    dropdown.grid(row=2, column=0, padx=20, pady=5, sticky="nw")
    dropdown.set("Select File Type(s)")
    dropdown.bind("<<ComboboxSelected>>", 
                  lambda event: list_selected(event, dropdown, dropdown_textbox, options)) 

    include_subfolders = tk.BooleanVar()
    subfolder_checkbox = ttk.Checkbutton(root, text="Include Subfolders", variable=include_subfolders,
                                         onvalue=True, offvalue=False)
    subfolder_checkbox.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    run_button = ttk.Button(root, text="Run",  command=lambda: run(dropdown_textbox, source_folder_entry, 
                                                dest_folder_entry, status_box, include_subfolders))
    run_button.grid(row=3, column=1, padx=20, pady=10, sticky="nw")

    status_box = tk.Label(root, width=100,bg=bg_color, relief="flat",
                          bd=0, highlightthickness=0, fg="firebrick3")
    status_box.grid(row=4, column=1, padx=20, pady=5, sticky="w")
    
    
    root.mainloop()

def add_source_folder(source_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    source_folder_entry.insert(0, folder_path)

def add_dest_folder(dest_folder_entry):
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    dest_folder_entry.insert(0, folder_path)

def list_selected(_, dropdown, dropdown_textbox, options):
    #display selection option, temporarily enable dropdown textbox edits to allow text to display
    dropdown_textbox.config(state="normal")
    dropdown_selection = dropdown.get()
    dropdown_textbox.insert("1.0", f"{dropdown_selection}\n")
    dropdown.set("Select File Type(s)")
    
    #expand dropdown textbox, disable ability for user edits to dropdown textbox
    new_height = dropdown_textbox.cget("height") + 1
    dropdown_textbox.config(height=new_height, state="disabled")
    
    #remove option from dropdown to prevent duplicates
    options.remove(dropdown_selection)
    dropdown.config(values=options)

def run(dropdown_textbox, source_folder_entry, dest_folder_entry, status_box, include_subfolders):   
    if source_folder_entry.get() == '':
        status_box.config(text="Error: No Source Folder selected")
        return
    
    if dest_folder_entry.get() == '':
        status_box.config(text="Error: No Destination Folder selected")
        return

    if dropdown_textbox.get("1.0","end-2c") == '':
        status_box.config(text="Error: No File Types selected")
        return

    file_type_selections = dropdown_textbox.get("1.0","end-2c")
    source_folder = source_folder_entry.get()
    dest_folder = dest_folder_entry.get()
    selections_list = file_type_selections.split("\n")
    
    if include_subfolders.get() == False:
        source_files = os.listdir(source_folder)
        for file_type in selections_list:
            for file in source_files:
                if file.endswith(file_type):
                    full_source_path = os.path.abspath(os.path.join(source_folder, file))
                    full_dest_path = os.path.abspath(os.path.join(dest_folder, file))
                    os.rename(full_source_path, full_dest_path)
                    print(f"{file} moved successfully")
    
    if include_subfolders.get() == True:
        source_file_paths = []
        for path, dirs, files in os.walk(source_folder):
            for file in files:
                source_file_paths.append(os.path.join(path, file))
        for file_type in selections_list:
            for file_path in source_file_paths:
                if file_path.endswith(file_type):
                    file_name = os.path.basename(file_path)
                    full_dest_path = os.path.abspath(os.path.join(dest_folder, file_name))
                    os.rename(file_path, full_dest_path)
                    print(f"{file_name} moved successfully")
                    
main()