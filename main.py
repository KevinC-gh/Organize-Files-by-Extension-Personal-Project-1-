#run: python3 main.py
import os
from pathlib import Path
import tkinter as tk

def main():
    
    window = tk.Tk()
    window.title("Sort by Extension")
    window.geometry("500x300")
        
    window.mainloop()


    #print("============ SORT BY EXTENSION ============")
    #source_folder = Path(input("Source folder (enter full path of folder where you're moving files FROM): "))
    #dest_folder = Path(input("Destination folder (enter full path of folder where you want to move files TO: "))
    #ext_type = Path(input("Select extension type: "))


main()