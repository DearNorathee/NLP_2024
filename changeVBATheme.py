# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:28:07 2023

@author: Heng2020
"""

import shutil
import tkinter as tk
from tkinter import messagebox

# Define the source file path and the destination directory path
source_path = r"C:\Users\Heng2020\OneDrive\Desktop\Change VBA Theme\VBE7.DLL"
destination_path = r"C:\Program Files\Microsoft Office\root\vfs\ProgramFilesCommonX64\Microsoft Shared\VBA\VBA7.1"

def copy_file(source_path,destination_path):
    try:
        # Construct the complete destination file path
        destination_file_path = destination_path + "\\" + source_path.split("\\")[-1]
        
        # Copy the file
        # shutil.copyfile(source_path, destination_file_path)
        shutil.copy2(source_path, destination_file_path)
        
        # Show a message box to inform the user that the file has been copied
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showinfo("Success", f"File has been copied to {destination_file_path}")
    except Exception as e:
        # If an error occurs, show a message box to inform the user about the error
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Execute the copy_file function
copy_file(source_path,destination_path)
