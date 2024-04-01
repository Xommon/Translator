from googletrans import Translator
import sys

def main():
    try:
        translator = Translator()
        input_text = input("Enter the text you want to translate: ")

        # Translate the text to German
        print("Spanish:", translator.translate(input_text, dest='es').text)
        print("French:", translator.translate(input_text, dest='fr').text)
        print("Portuguese:", translator.translate(input_text, dest='pt').text)
        print("Italian:", translator.translate(input_text, dest='it').text)

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
