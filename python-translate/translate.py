from googletrans import Translator


while True:

    sentence = input('Wpisz tekst\n')
    translator = Translator()

    translated_sentence = translator.translate(sentence, src='pl', dest='en')

    print(translated_sentence.text)