# EXT Sorter
This program allows users move files from one folder to another based on their file extensions. Users select a source folder, destination folder, and extension types and the program will automatically move all files of the specified extension types.

# Requirements:
Python 3.x or above:
```
https://www.python.org/downloads/
```
# Installation and Running the Program:
To install, navigate to the folder to where you want to have the program and clone the repository:
```
git clone https://github.com/KevinC-gh/EXT-Sorter
```
To run, navigate to the directory where the project is located:
```
cd EXT-Sorter
```
Then run the program using:
```
python3 main.py
```
The user interface window should appear and look like this:


<img width="1207" height="329" alt="EXT-Sorter_screenshot" src="https://github.com/user-attachments/assets/74623548-c5a3-4c83-b698-64b11da95db9"/>


Use the "Add Source Folder" and "Add Destination Folder" to add the folders you want to move to and from. The Source Folder is the folder you're moving files from whereas the destinaton folder is the location you're moving files to. Note that when selecting a folder, you must go into that folder to select it - just clicking on the folder won't actually select it. Use the "Selection" box at the bottom of the window to make sure it's the right file path.


<img width="422" height="283" alt="select_folder" src="https://github.com/user-attachments/assets/139e91b3-ddef-461f-930d-4a8e7f8bb0dd" />


Use the "Select File Type(s) dropdown to select 1 or more file types. These files will appear in a list in the text box to the right of the dropdown. If you make a mistake, you can use the "Undo" button to undo the last selection in the list, or use "Clear All" to remove everything from the list.


<img width="906" height="429" alt="select_options" src="https://github.com/user-attachments/assets/6eb80425-87e4-491b-adbc-7e6a9b7f0601" />


There are a number of special options at the bottom of the dropdown that allow you to select all extension types of a specific category, such as text files, image files, video files, etc. You can use [this website](https://www.geeksforgeeks.org/techtips/list-of-file-formats/) as a guide as to which files are included in each category.

The "Include Subfolders" checkbox determines whether or not the program should check for additional folders within the selected source folder and move items from those folders as well.

Once the source folder, destination folder, and file types are selected, use the "Run" button to run the program. IF files were successfully moved, a message specifying the number of files moved should appear.


<img width="906" height="270" alt="success" src="https://github.com/user-attachments/assets/c138db24-5f30-4e8a-8457-8463911f4c67" />
 
