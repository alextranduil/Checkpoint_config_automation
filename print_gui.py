import tkinter as tk

def print_to_gui(message, text_output):
    """
    Function to print messages to the GUI.
    """
    text_output.insert(tk.END, message + '\n')
    text_output.yview(tk.END)  # Auto-scroll to the bottom