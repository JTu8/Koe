# -*- coding: utf-8 -*- 
from tkinter import*

def Laske():
    tulos = 0
    luku = 0.0
    luku = float(Entry.get(hauki))

    luku2 = 0.0
    luku2 = float(Entry.get(ahven))

    luku3 = 0.0
    luku3 = float(Entry.get(kuha))

    luku4 = 0.0
    luku4 = float(Entry.get(taimen))

    luku5 = 0.0
    luku5 = float(Entry.get(muut))

    tulos = luku * 1 + luku2 * 1.4 + luku3 * 1.4 + luku4 * 5 + luku5 * 0,5
    Entry.insert(pisteet, 0, tulos)

def Tyhjenna():
    Entry.delete(hauki, 0, END)
    Entry.delete(ahven, 0, END)
    Entry.delete(kuha, 0, END)
    Entry.delete(taimen, 0, END)
    Entry.delete(muut, 0, END)
    Entry.delete(pisteet, 0, END)
    




root = Tk()
root.title("Uistelukilpailu")
frame = Frame(root, borderwidth = 1)
frame.pack()
frame2 = Frame(frame, borderwidth = 0)
frame2.pack()
frame3 = Frame(frame, borderwidth = 5)
frame3.pack()
frame4 = Frame(frame)
frame4.pack()
frame5 = Frame(frame)
frame5.pack()
frame6 = Frame(frame)
frame6.pack()
frame7 = Frame(frame)
frame7.pack()
frame8 = Frame(frame)
frame8.pack()
frame9 = Frame(frame)
frame9.pack()
frame10 = Frame(frame)
frame10.pack()

tekstikentta = Label(frame2, text="Haukien paino")
tekstikentta.pack(side = LEFT)
hauki = Entry(frame2)
hauki.pack(side = LEFT)

tekstikentta2 = Label(frame3, text="Ahventen paino")
tekstikentta2.pack(side = LEFT)
ahven = Entry(frame3)
ahven.pack(side = LEFT)

tekstikentta3 = Label(frame4, text="Kuhien paino")
tekstikentta3.pack(side = LEFT)
kuha = Entry(frame4)
kuha.pack(side = LEFT)

tekstikentta4 = Label(frame5, text="Taimenten paino")
tekstikentta4.pack(side = LEFT)
taimen = Entry(frame5)
taimen.pack(side = LEFT)

tekstikentta5 = Label(frame6, text="Muiden paino")
tekstikentta5.pack(side = LEFT)
muut = Entry(frame6)
muut.pack(side = LEFT)

laske_nappi = Button(frame8, text="Laske", height = 1, width = 10, command = Laske)
laske_nappi.pack(side = LEFT)
tyhjenna_nappi = Button(frame8, text="Tyhjennä", height = 1, width = 10, command = Tyhjenna)
tyhjenna_nappi.pack(side = LEFT)

tekstikentta7 = Label(frame9, text="Tulos")
tekstikentta7.pack(side = LEFT)
pisteet = Entry(frame9)
pisteet.pack(side = LEFT)

root.mainloop()


