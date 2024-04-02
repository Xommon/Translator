import googletrans
from googletrans import Translator
import sys
from tkinter import*

# Create GUI object
window = Tk()

# Import translator and languages
translator = Translator()
language_keys = list(googletrans.LANGUAGES.keys())
languages = list(googletrans.LANGUAGES.values())
#print(languages)

# Create Field1
selected1 = StringVar()
selected1.set("english")
dropdown1 = OptionMenu(window, selected1, *languages)
dropdown1.pack(side=LEFT)
entry1 = Entry(window, width=50)
entry1.pack(side=LEFT)

# Create Field2
selected2 = StringVar()
selected2.set("english")
dropdown2 = OptionMenu(window, selected2, *languages)
dropdown2.pack(side=LEFT)
entry2 = Entry(window, width=50)
entry2.pack(side=LEFT)

def translate():
    # Translate the text
    try:
        entry2.delete(0, 'end')
        entry2.insert(0, translator.translate(entry1.get(), src=language_keys[languages.index(selected1.get())], dest=language_keys[languages.index(selected2.get())]).text)
    except Exception as e:
        print("FATAL ERROR:", e)
        sys.exit(1)

def clear_text():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

translateButton = Button(window, text="Translate", command=translate)
translateButton.pack()
clearButton = Button(window, text="Clear", command=clear_text)
clearButton.pack()

window.mainloop()