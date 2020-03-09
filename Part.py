from Elem import Elements
from Jug import Jugadors

class Partida:

    #Inicialitza els atributs de la partida
    def __init__(self):

        #Atribut biblioteca on es guarden els objectes dels jugadors, la clau es el nom del jugador
        self.__llistaJugadors={}

        #Atribut biblioteca on es guarden els objectes dels elements, la clau es el nom del element
        self.__llistaElements={}
    
    #Transforma los datos str recibidos del fixero de carga para processarlos en atributos 
    #def Carga(self,dats):

    #Agafa les dades rebudes respecte als elements, comprova que les dades estiguin correctes, transforma les dades en les corresponents, crea el obj del element i l'emmagatzema en un atribut biblioiteca
    def CarregarPartida(self,nom,preu,fungible,quantitat):
        preu=int(preu)
        if fungible=="Perecedero":
            fungible=True
        elif fungible=="Imperecedero":
            fungible=False
        else:
            raise ValueError
        quantitat=int(quantitat)
        self.__llistaElements[nom]=[Elements(nom,preu,fungible),quantitat]
    
    #Confirma si existeix el jugador amb el nom rebut
    def JugConfirm(self,nom):
        confirm=True
        return not nom in self.__llistaJugadors

    #Confirma si existeix el element amb el nom rebut
    def ElemConfirm(self,nom):
        confirm=True
        return not nom in self.__llistaElements

    #Afegeix un jugador
    def NouJugador(self,nom,f,m,v,):
        self.__llistaJugadors[nom]=Jugadors(nom,f,m,v)
    
    #Elimina un jugador
    def ElimJugador(self,nom):
        del self.__llistaJugadors[nom]

    #Resta salut a un jugador a partir d'una funcio del obj, si la funcio retorna Defuncion=True elimina al jugador
    def RestSalut(self,nom,valor):
        Defuncio=self.__llistaJugadors[nom].Decrement(valor)
        if Defuncio:
            self.ElimJugador(nom)

    #Comprova si quedan elements en la partida, en cas contrari executa una excepcio. Si quedan elements en la partida utilitza la funcio del jugador per comprar l'element i resta 1 a la quantitat del element de la partida          
    def ComprarElem(self,nom,elem):
        if self.__llistaElements[elem][1]>0:
            self.__llistaElements[elem][1]-=1
        else:
            raise TypeError
        self.__llistaJugadors[nom].Compra(self.__llistaElements[elem][0])
    
    #Executa la funcio del obj jugador per utilitzar l'element
    def UsarElement(self,nom,elem):
        self.__llistaJugadors[nom].UsElem(self.__llistaElements[elem][0])

    #Mostra els valors dels seus atributs i del atributs del objectes que incorpora mitjançant les funcions corresponents
    def __str__(self):
        print("--------\nPartida: Joc\nElements:\n--------")
        for a in self.__llistaElements:
            print(a)
            print(self.__llistaElements[a][0])
            print("Quantitat en la partida: "+str(self.__llistaElements[a][1]))
            print("--------")
        print("Jugadors:")
        print("--------")
        for a in self.__llistaJugadors:
            print("\t"+a)
            print(self.__llistaJugadors[a])
        return ""
    
    #Transforma los datos de la partida en un str para su almacenamiento posterior en un fixero 
    def Guardar(self):
        Dats=""
        for a in self.__llistaElements:
            Dats=Dats+self.__llistaElements[a][0].Dev()+"-"+str(self.__llistaElements[a][1])+"--*--"
        Dats=Dats[:len(Dats)-5]+"*+*"
        for a in self.__llistaJugadors:
            Dats=Dats+self.__llistaJugadors[a].Dev()+"-o-"
        Dats=Dats[:len(Dats)-3]

        return Dats
    
    #Resetea la biblioteca que conté als jugadors 
    def Borrar(self):
        self.__llistaJugadors={}

    