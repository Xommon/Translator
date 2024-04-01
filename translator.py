from googletrans import Translator
import sys
from tkinter import*

# Create GUI
window = Tk()

input_field = Entry(window, width=50)
input_field.pack()

def translate():
    # Translate the text
    try:
        translator = Translator()
        output_string = "Spanish: " + translator.translate(input_field.get(), dest='es').text
        Label(window, text=output_string).pack()

        # Languages
        #print("Spanish:", translator.translate(input_text, dest='es').text)
        #print("French:", translator.translate(input_text, dest='fr').text)
        #print("Portuguese:", translator.translate(input_text, dest='pt').text)
        #print("Italian:", translator.translate(input_text, dest='it').text)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

translateButton = Button(window, text="Translate", command=translate)
translateButton.pack()

window.mainloop()