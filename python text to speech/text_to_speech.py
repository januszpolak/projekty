def main():

    from gtts import gTTS 
    import os

    mytext = input('Wprowadź swój tekst, który będzie przekonwertowany na mowę:')

    language = 'pl'
      
    myobj = gTTS(text=mytext, lang=language, slow=False) 
  
    myobj.save("output.mp3") 
    os.system("mpg321 output.mp3")

    restart = input('Jescze raz? wpisz tak lub nie  ')
    if restart == 'tak':
        main()
    else:
        quit()

main()
