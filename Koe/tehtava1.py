# -*- coding: utf-8 -*- 
class Kulejtustehtava():

    def __init__(self, kestotunneissa = 10, henkilotarvelkm = 30, tehtavakuvaus = "Tehtävä", kuljetusmatkakm = 34.5):
        self.__kestotunneissa = kestotunneissa
        self.__henkilotarvelkm = henkilotarvelkm
        self.__tehtavakuvaus = tehtavakuvaus
        self.__kuljetusmatkakm = kuljetusmatkakm

    def getTunnit(self):
        return self.__kestotunneissa

    def getHenkilotarvelkm(self):
        return self.__henkilotarvelkm

    def getTehtavakuvaus(self):
        return self.__tehtavakuvaus

    def getKuljetusmatkakm(self):
        return self.__kuljetusmatkakm

class Tyotehtava():

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)


k = Kulejtustehtava()
lopetus = True
lista = []

print ("Kuljetustehtävät:")

while (lopetus):

    kesto = input("Annappa kesto: ")
    kesto = int(kesto)
    lista.append(kesto)

    lukumaara = input("Annappa HENKILOLKM: ")
    lukumaara = int(lukumaara)
    lista.append(lukumaara)

    kuvaus = input("Annappa kuvaus: ")
    kuvaus = str(kuvaus)
    lista.append(kuvaus)

    matka = input("Annappa kuljetusmatka: ")
    matka = float(matka)
    lista.append(matka)

    if (kesto == 0):
        lopetus = False
        print ("AHAA, LOPETIT")


print ("Kuljetustehtävät jotka kestävät > 8 tuntia")





