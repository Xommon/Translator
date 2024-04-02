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

# Add field
def add_entry():
    dropdown = ttk.Combobox(window, value=languages)
    dropdown.current(21)
    dropdown.grid(row=len(fields), column=0)
    entry = Entry(window, width=100)
    entry.grid(row=len(fields), column=1)
    newField = Field(dropdown, entry)
    fields.append(newField)

# Remove field
def remove_entry():
    if fields.len() > 0:
        fields[len(fields)-1].dropdown.destroy()
        fields[len(fields)-1].entry.destroy()
        fields[len(fields)-1].pop()

# Create Field1
#dropdown1 = ttk.Combobox(window, value=languages)
#dropdown1.current(21)
#dropdown1.grid(row=0, column=0)
#entry1 = Entry(window, width=100)
#entry1.grid(row=0, column=1)

# Create Field2
#dropdown2 = ttk.Combobox(window, value=languages)
#dropdown2.current(21)
#dropdown2.grid(row=1, column=0)
#entry2 = Entry(window, width=100)
#entry2.grid(row=1, column=1)
        
# Create the first two fields
add_entry()
add_entry()
add_entry()
add_entry()

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
        

def clear_text():
    for field in fields:
        field.entry.delete(0, 'end')

translateButton = Button(window, text="Translate", command=translate)
translateButton.grid(row=len(fields), column=1)
clearButton = Button(window, text="Clear", command=clear_text)
clearButton.grid(row=len(fields), column=2)

window.mainloop()