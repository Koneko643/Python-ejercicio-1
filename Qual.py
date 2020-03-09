class Qualitats():
    #Defineix les qualitats Força, Magia i Velocitat
    def __init__(self,f,m,v):

        #Atribut on es guarda el valor int que representa la força
        self.__força=f

        #Atribut on es guarda el valor int que representa la magia
        self.__magia=m

        #Atribut on es guarda el valor int que representa la velocitat
        self.__velocitat=v
        
    #Retorna un print amb les característiques de tots els atributs
    def __str__(self):
        return "\t\tForça: "+str(self.__força)+"\n\t\tMàgia: "+str(self.__magia)+"\n\t\tVelocitat: "+str(self.__velocitat)
    
    #Retorna les dades del obj qualitat en forma de str
    def Dev(self):
        return str(self.__força)+"*"+str(self.__magia)+"*"+str(self.__velocitat)