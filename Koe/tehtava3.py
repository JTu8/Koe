# -*- coding: utf-8 -*- 

lopetus = True
print("Palindromipeli\n")

while (lopetus):
    sana = input("Annappa sanasi: ")
    sana = str(sana)

    if (sana == sana[::-1]):
        print("Yes, onnistuit löytämään palindromin!")
        print("Ohjelma on nyt ohi")
        lopetus = False
    else:
        print("Ei ole palindromi, yritä uudelleen!")
