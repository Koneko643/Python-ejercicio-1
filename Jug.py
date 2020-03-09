#S'importen els fitxers .py de les classes utilitzades
from Qual import Qualitats

class Jugadors:

    #Inicialitza els atributs predefinits i es crea l'atribut obj quali amb els atributs seleccionats pel usuari
    def __init__(self,nom,f,m,v):

        #Atribut que guarda el objecte que gestiona les qualitats (força,magia i velocitat)
        self.__quali=Qualitats(f,m,v)

        #Atribut string que guarda el nom del jugador
        self.__nom=nom

        #Atribut int que guarda el valor de la riquessa
        self.__riquessa=100

        #Atribut int que guarda el valor de la salut
        self.__salut=50

        #Atribut llista que guarda els elements que poseeix
        self.__elements=[]
    
    #Es mostren totes les característiques dels atributs incluent els atributs del atribut obj Quali
    def __str__(self):
        print("\t\tRiquessa: "+str(self.__riquessa)+"\n\t\tSalut: "+str(self.__salut))
        print(self.__quali)
        print("\t\tElements del jugador: ")
        for a in self.__elements:
            print("\t\t\t"+a.Namae())
        return "--------"
    
    #Retorna les dades de la partida en forma de str
    def Dev(self):
        Dats=self.__nom+"*"+str(self.__riquessa)+"*"+str(self.__salut)+"-.-"+self.__quali.Dev()+"-.-"
        for a in self.__elements:
            Dats=Dats+a.Dev()+"/o/"
        Dats=Dats[:len(Dats)-3]
        return Dats


    #Es resta salut al jugador i es comprova si la salut es menor que 0
    def Decrement(self,valor):
        self.__salut-=valor
        return self.__salut<=0

    #Es comprova si el jugador pot comprar un objecte, en cas afirmatiu s'afegeix a la llista dels seus elements, en cas contrari s'aixeca una excepcio
    def Compra(self,elem):
        if self.__riquessa>=elem.Preu():
            self.__elements.append(elem)
            self.__riquessa-=elem.Preu()
        else:
            raise ValueError
    
    #Es comprova si l'element a utilitzar esta en la llista d'elements del usuari, en cas negatiu s'aixeca una excepcio, en cas afirmatiu es comprova si es fungible o no. Si es fungible s'elimina de la llista del jugador
    def UsElem(self,elem):
        if elem in self.__elements:
            if elem.Fungi():
                self.__elements.remove(elem)
        else:
            raise TypeError
    