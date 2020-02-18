from tkinter import *    # importuje bibkiotekę
okno = Tk()                 # uruchamiam okno dialogowe
okno.title("Wpisz swoje imie!") # napis na ramce
okno.geometry('350x200')         #wielkość okna
przywitanie = Label(okno, text="Witaj")   # wprowadza napis do okna
przywitanie.grid(column=0, row=0)    # zdefiniowanie gdzie ten napis ma sie znajdować
imie = Entry(okno,width=10)   # wycięcie do wpisania swojego imienia
imie.grid(column=1, row=0)    # zdefiniowanie gdzie te wcięcie ma się znajdować
def clicked():              # definiuje funkcję
    przywitanie2 = "Witamy Ciebie  " + imie.get()   # to co pwisaliśmy imie tu się wyświetla
    przywitanie.configure(text= przywitanie2)
przycisk = Button(okno, text="Naciśnij przycisk", command=clicked)
# naciśnij przycisk a uruchomi się funkcja
przycisk.grid(column=2, row=0) # położenie przycisku
okno.mainloop()                 #uruchomienie pętli
