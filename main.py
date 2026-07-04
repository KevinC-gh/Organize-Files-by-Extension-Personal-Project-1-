#run: python3 main.py
#cd workspace/bootdev/personal_project_1
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def main():
    
    root = tk.Tk()
    root.title("Sort by Extension")
    root.geometry("1200x400")
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

    dropdown_textbox = tk.Text(root, width=30, height=1)
    dropdown_textbox.grid(row=2, column=1, padx=20, pady=5, sticky="w")

    options = [".3gp", ".7z", ".aac", ".arc", ".arj", ".asp", "aspx", ".au", ".avi", ".bat",
               ".bin", ".bmp", ".c", ".com", ".cpp", ".cs", ".css", ".csv", ".doc", ".docx",
               ".dta", ".eml", ".eps", ".exe", ".gif", ".gz", ".htm", "html", ".hqx", ".java",
               ".jpeg", ".jpg", ".js", ".mov", ".mp3", ".mp4", ".mpg", ".msg", ".pdf", ".pl",
               ".png", ".py", ".ra", ".rar", ".rss", ".rtf", ".sh", ".sit", ".snd", ".swift",
               ".tar", ".tif", ".ts", ".txt", ".wav", ".webp", ".wma", ".wmv", ".wps", ".xhtml",
               ".xlsx", ".z", ".zip", 
               "All Text Formats", "All Image Formats", "All Audio Formats", "All Video Formats",
               "All Program File Formats", "All Compressed/Archive Formats", "All Web Page File Formats"]
    
    dropdown = ttk.Combobox(root, width=27, values=options, state="readonly")
    dropdown.grid(row=2, column=0, padx=20, pady=5, sticky="nw")
    dropdown.set("Select File Type(s)")
    dropdown.bind("<<ComboboxSelected>>", 
                  lambda event: list_selected(event, dropdown, dropdown_textbox, options))

    undo_button = ttk.Button(root, text="Undo", command=lambda: undo_last_file_type(dropdown_textbox))
    undo_button.grid(row=2, column=1, pady=5)

    include_subfolders = tk.BooleanVar()
    subfolder_checkbox = ttk.Checkbutton(root, text="Include Subfolders", variable=include_subfolders,
                                         onvalue=True, offvalue=False)
    subfolder_checkbox.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    run_button = ttk.Button(root, text="Run",  command=lambda: run(dropdown_textbox, source_folder_entry, 
                                                dest_folder_entry, status_box, include_subfolders))
    run_button.grid(row=3, column=1, padx=20, pady=10, sticky="nw")

    status_box = tk.Label(root, width=100,bg=bg_color, relief="flat",
                          bd=0, highlightthickness=0, fg="firebrick3",
                          anchor="w", font=("Arial", 12, "bold"))
    status_box.grid(row=4, column=1, padx=20, pady=10, sticky="w")
    
    root.mainloop()

def add_source_folder(source_folder_entry):
    source_folder_entry.delete(0, tk.END)
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    source_folder_entry.insert(0, folder_path)

def add_dest_folder(dest_folder_entry):
    dest_folder_entry.delete(0, tk.END)
    folder_path = filedialog.askdirectory(initialdir="/mnt/c/users", title="Select Folder")
    dest_folder_entry.insert(0, folder_path)

def list_selected(_, dropdown, dropdown_textbox, options):
    #display selection option, temporarily enable dropdown textbox edits to allow text to display
    dropdown_textbox.config(state="normal")
    dropdown_selection = dropdown.get()
    dropdown_textbox.insert(tk.END, f"{dropdown_selection}\n")
    dropdown.set("Select File Type(s)")
    
    #expand dropdown textbox, disable ability for user edits to dropdown textbox
    new_height = dropdown_textbox.cget("height") + 1
    dropdown_textbox.config(height=new_height, state="disabled")
    
    #remove option from dropdown to prevent duplicates
    options.remove(dropdown_selection)
    dropdown.config(values=options)

def get_file_type_selections(dropdown_textbox):
    
    file_type_selections = dropdown_textbox.get("1.0","end-2c")
    
    if "All Text Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Text Formats", 
                                                            ".txt\n.rtf\n.docx\n.csv\n.doc\n.wps\n.wpd\n.msg")
    
    if "All Image Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Image Formats", 
                                                            ".jpg\n.jpeg\n.webp\n.gif\n.tif\n.tif\n.bmp\n.eps")
    
    if "All Audio Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Audio Formats", 
                                                            ".mp3\n.wma\n.snd\n.wav\n.ra\n.au\n.acc")

    if "All Video Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Video Formats", 
                                                            ".mp4\n.3gp\n.avi\n.mpg\n.mov\n.wmv")

    if "All Program File Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Program File Formats", 
                                                            ".c\n.cpp\n.java\n.py\n.js\n.ts\n.cs\n.swift\n.dta\n.pl\n.sh\n.bat\n.com\n.exe")
    
    if "All Compressed/Archive Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Compressed/Archive Formats",
                                                            ".rar\n.zip\n.hqx\n.arj\n.tar\n.arc\n.sit\n.gz\n.z")
    
    if "All Web Page File Formats" in file_type_selections:
        file_type_selections = file_type_selections.replace("All Web Page File Formats",
                                                            ".html\n.htm\n.xhtml\n.asp\n.css\n.aspx\n.rss")
    
    return file_type_selections

def undo_last_file_type(dropdown_textbox):
    dropdown_textbox.delete()


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

    source_folder = source_folder_entry.get()
    if os.path.isdir(source_folder) == False:
        status_box.config(text="Error: Invalid Source Folder")
        return
    
    dest_folder = dest_folder_entry.get()
    if os.path.isdir(dest_folder) == False:
        status_box.config(text="Error: Invalid Destination Folder")
        return
    
    file_type_selections = get_file_type_selections(dropdown_textbox)
    source_folder = source_folder_entry.get()
    dest_folder = dest_folder_entry.get()
    selections_list = file_type_selections.split("\n")

    if include_subfolders.get() == False:
        counter = 0
        source_files = os.listdir(source_folder)
        for file_type in selections_list:
            for file in source_files:
                if file.endswith(file_type):
                    full_source_path = os.path.abspath(os.path.join(source_folder, file))
                    full_dest_path = os.path.abspath(os.path.join(dest_folder, file))
                    os.rename(full_source_path, full_dest_path)
                    counter += 1
        if counter == 0:
            status_box.config(text=f"No valid files found in {os.path.basename(source_folder)}")
        else:
            status_box.config(fg="green4", text=f"{counter} file(s) moved from {os.path.basename(source_folder)} to {os.path.basename(dest_folder)}")
    
    if include_subfolders.get() == True:
        source_file_paths = []
        counter = 0
        for path, dirs, files in os.walk(source_folder):
            for file in files:
                source_file_paths.append(os.path.join(path, file))
        for file_type in selections_list:
            for file_path in source_file_paths:
                if file_path.endswith(file_type):
                    file_name = os.path.basename(file_path)
                    full_dest_path = os.path.abspath(os.path.join(dest_folder, file_name))
                    os.rename(file_path, full_dest_path)
                    counter += 1
        if counter == 0:
            status_box.config(text=f"No valid files found in {os.path.basename(source_folder)} or subfolders")
        else:
            status_box.config(fg="green4", text=f"{counter} file(s) moved from {os.path.basename(source_folder)} to {os.path.basename(dest_folder)}")

main()