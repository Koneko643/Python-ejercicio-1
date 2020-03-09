class Elements:

    #S'inicialitzen els atributs a partir de la informació rebuda
    def __init__(self,n,p,f):

        #Atribut string que guarda el nom del element
        self.__nom=n

        #Atribut int que guarda el preu del element
        self.__preu=p

        #Atribut bool que determina si es fungible o no
        self.__fungible=f
    
    #Es mostra tota l'informació dels atributs del element
    def __str__(self):
        if self.__fungible:
            fungi="Si"
        else:
            fungi="No"
        print("\t\tPreu: "+str(self.__preu)+"\n\t\tFungible: "+fungi)
        return ""
    
    #Retorna les dades del element en forma de str
    def Dev(self):
        if self.__fungible==True:
            Fun="Perecedero"
        else:
            Fun="Imperecedero"
        Dats=self.__nom+"-"+str(self.__preu)+"-"+Fun
        return Dats
    
    #Retorna el atribut preu
    def Preu(self):
        return self.__preu
    
    #Retorna el atribut fungible
    def Fungi(self):
        return self.__fungible
    
    #Retorna el atribut nom
    def Namae(self):
        return self.__nom