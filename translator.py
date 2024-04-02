import googletrans
from googletrans import Translator
import sys
from tkinter import*
import tkinter.ttk as ttk

# Create GUI object
window = Tk()

# Import translator and languages
translator = Translator()
language_keys = list(googletrans.LANGUAGES.keys())
languages = list(googletrans.LANGUAGES.values())
languages = [word.title() for word in languages]
#print(languages)

# Create Fields
fields = list()
class Field:
    def __init__(self, dropdown, entry):
        self.dropdown = dropdown
        self.entry = entry

# Remove field
def remove_entry():
    if len(fields) > 0:
        fields[len(fields)-1].dropdown.destroy()
        fields[len(fields)-1].entry.destroy()
        fields.pop()

# Translate the text
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
        
# Clear text
def clear_text():
    for field in fields:
        field.entry.delete(0, 'end')

# Translate and Clear buttons
translateButton = Button(window, text="Translate", command=translate)
clearButton = Button(window, text="Clear", command=clear_text)

def reposition_buttons():
    translateButton.grid(row=len(fields)+1, column=1)
    clearButton.grid(row=len(fields)+1, column=2)

# Add field
def add_entry():
    dropdown = ttk.Combobox(window, value=languages)
    dropdown.current(21)
    dropdown.grid(row=len(fields), column=0)
    entry = Entry(window, width=100)
    entry.grid(row=len(fields), column=1)
    newField = Field(dropdown, entry)
    addButton.grid(row=len(fields)+1, column=0)
    minusButton.grid(row=len(fields)+1, column=1)
    fields.append(newField)
    reposition_buttons()
addButton = Button(window, text="+", command=add_entry)
minusButton = Button(window, text="-", command=remove_entry)

# Create the first two fields
add_entry()
add_entry()

window.mainloop()