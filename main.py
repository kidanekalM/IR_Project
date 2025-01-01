import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from stemmer import stem 

#corpus collection > Tokenization > stopowrd removal > stemmer > IR structure > UI  

def display_output():
    input_text = entry.get()
    stemW,rootW = stem(input_text)
    output_label.config(text=f"Stem: {stemW} \nRoot: {rootW}")

# Create the main window
root = tk.Tk()
root.title("Ge'ez Stemmer")
root.geometry("400x400")
root.configure(padx=20, pady=20)
root.configure(bg="#f0f0f0")  # Light background color

# Style configuration
style = ttk.Style()
style.theme_use('clam')  # Use a modern theme

# Button styling
style.configure("TButton", padding=10, font=("Helvetica", 16), relief="raised", background="#4CAF50", foreground="white")
style.map("TButton", background=[('active', '#45a049')])

# Label styling
style.configure("TLabel", font=("Helvetica", 20))

# Create a frame for the input area with rounded edges
frame = ttk.Frame(root, padding=20)
frame.pack(pady=10)

# Create an entry widget for text input
entry = ttk.Entry(frame, width=50)
entry.pack(pady=10)

# Set a larger font directly on the entry widget
entry_font = Font(family="Helvetica", size=18)
entry.config(font=entry_font)

# Create a button to submit the input
submit_button = ttk.Button(root, text="Submit", command=display_output)
submit_button.pack(pady=5)

# Create a label to display the output
output_label = ttk.Label(root, text="Stem: ")
output_label.pack(pady=10)


# Run the application
root.mainloop()