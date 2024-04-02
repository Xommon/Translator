import googletrans
from googletrans import Translator
import sys
from tkinter import *
import tkinter.ttk as ttk
import pyperclip

# Create GUI object
window = Tk()
window.title("Mass Google Translator - Micheal Quentin")

# Import translator and languages
translator = Translator()
language_keys = list(googletrans.LANGUAGES.keys())
languages = list(googletrans.LANGUAGES.values())
languages = [word.title() for word in languages]

# Create Fields
fields = list()
class Field:
    def __init__(self, dropdown, entry, copy_button):
        self.dropdown = dropdown
        self.entry = entry
        self.copy_button = copy_button

# Function to translate the text
def translate():
    index = 1
    if len(fields) > 1 and fields[0].entry.get() != '':
        while index < len(fields):
            try:
                fields[index].entry.delete(0, 'end')
                fields[index].entry.insert(0, translator.translate(fields[0].entry.get(), src=language_keys[languages.index(fields[0].dropdown.get())], dest=language_keys[languages.index(fields[index].dropdown.get())]).text)
                index += 1
            except Exception as e:
                print("FATAL ERROR:", e)
                sys.exit(1)

# Function to clear text
def clear_text():
    for field in fields:
        field.entry.delete(0, 'end')

# Function to copy text
def copy_text(row):
    pyperclip.copy(fields[row].entry.get())

# Function to remove field
def remove_entry():
    if len(fields) > 0:
        fields[len(fields)-1].dropdown.destroy()
        fields[len(fields)-1].entry.destroy()
        fields[len(fields)-1].copy_button.destroy()
        fields.pop()

# Function to add field
def add_entry():
    # Create a frame to contain dropdown, entry, and copy button
    frame = Frame(window)
    frame.grid(row=len(fields), column=0, columnspan=3, sticky='ew', pady=5)

    # Dropdown
    dropdown = ttk.Combobox(frame, value=languages)
    dropdown.current(21)
    dropdown.grid(row=0, column=0, padx=(0, 5))

    # Entry
    entry = Entry(frame, width=100)
    entry.grid(row=0, column=1, padx=(0, 5))

    # Copy button
    copy_button = Button(frame, text="Copy", command=lambda row=len(fields): copy_text(row))
    copy_button.grid(row=0, column=2)

    newField = Field(dropdown, entry, copy_button)
    fields.append(newField)
    reposition_buttons()

# Function to reposition buttons
def reposition_buttons():
    # Remove existing buttons
    addButton.grid_forget()
    minusButton.grid_forget()
    translateButton.grid_forget()
    clearButton.grid_forget()

    # Add buttons below the last field
    addButton.grid(row=len(fields)+1, column=0, padx=(0, 5))
    minusButton.grid(row=len(fields)+1, column=1, padx=(0, 5))
    translateButton.grid(row=len(fields)+1, column=2, padx=(0, 5))
    clearButton.grid(row=len(fields)+1, column=3, padx=(0, 5))

# Translate and Clear buttons
translateButton = Button(window, text="Translate", command=translate)
clearButton = Button(window, text="Clear", command=clear_text)

# Add and Minus buttons
addButton = Button(window, text="+", command=add_entry)
minusButton = Button(window, text="-", command=remove_entry)

# Create the first two fields
add_entry()
add_entry()

window.mainloop()
