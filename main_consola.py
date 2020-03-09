#Comprova si el jugador introduit ja esta registrat
def CompJug():
    Name=input("Introdueix el nom del jugador: ")
    Confirm=Joc.JugConfirm(Name)
    return Confirm,Name

#Comprova si el element introduit existeix
def CompElem():
    Name=input("Introdueix el nom del element: ")
    Confirm=Joc.ElemConfirm(Name)
    return Confirm,Name

#Comanda para guardar partida
def Guardar():
    
    nom=input("¡Recorda que si ja existeix una partida amb el mateix nom es sobreescriurà\nIntrodueix el nom de la partida: ")
    fitxer=open("Partidas/"+nom+".txt","w")

    #Es guarda l'informació de la partida en el fitxer seleccionat, si ja existeix es sobreescriu
    part=Joc.Guardar()
    fitxer.write(part)
    fitxer.close()
    
    #Si el fitxer no existia abans es guarda el seu nom en el arxiu que emmagatzema les partides guardades
    fitxerl=open("Partidas/SelecPart.txt","r")
    PartidasG=fitxerl.read()
    PartidasG.split("\n")
    if nom not in PartidasG:
        fitxerw=open("Partidas/SelecPart.txt","a")
        fitxerw.write("\n"+nom)
        fitxerw.close()

#Comando para cargar partida
def Cargar():

    #Es comprova que hi ha partides guardades
    fitxer=open("Partidas/SelecPart.txt","r")
    part=fitxer.read().split("\n")
    fitxer.close()
    if len(part)>0:
        
        #Comprova si la partida a cargar existeix
        Ex1=True
        while Ex1:
            ncarga=input("Introdueix el nom de la partida: ")
            
            #Si la partida existeix comença a carregar la informació
            if ncarga in part and ncarga !="":
                fitxer=open("Partidas/"+ncarga+".txt","r")
                dats=fitxer.read()
                fitxer.close()

                #Es comprova si hi han jugadors en el fitxer a cargar
                if "*+*" in dats:
                    Temp=dats.split("*+*")

                    #Es resetea la llista actual de jugadors per carregar la nova
                    Joc.Borrar()
                    Jug=Temp[1].split("-o-")
                    for a in Jug:
                        Divid=a.split("-.-")
                        Sec1=Divid[0].split("*")
                        Sec2=Divid[1].split("*")

                        #S'inicialitza el jugador amb les dades extretes i es modifica el seu perfil d'acord als seus atributs
                        Joc.NouJugador(Sec1[0],int(Sec2[0]),int(Sec2[1]),int(Sec2[2]))
                        Joc.RestSalut(Sec1[0],50-int(Sec1[2]))

                        #Es comprova si el jugador poseeix elements
                        if len(Divid)==3:
                            Sec3=Divid[2].split("/o/")
                            for a in Sec3:
                                Joc.ComprarElem(Sec1[0],a.split("-")[0])
                    Ex1=False
                    
                    #Es carreguen els elements de la partida 
                    Ele=Temp[0].split("--*--")
                    for a in Ele:
                        info=a.split("-")
                        Joc.CarregarPartida(info[0],info[1],info[2],info[3])
                    Ex1=False

                    
                #Si en la partida a carregar no existeixen usuaris es carreguen només els elements de la partida
                else:
                    Ele=dats.split("--*--")
                    for a in Ele:
                        info=a.split("-")
                        Joc.CarregarPartida(info[0],info[1],info[2],info[3])
                    Ex1=False
                print("Partida carregada")
            
            #Si la partida no existeix l'usuari pot tornar a introduir un nom o tornar al inici
            else:
                print("Aquesta partida no existeix")
                Ex2=True
                while Ex2:
                    again=input("Vol tornar al menu? [Si][No] ")
                    if again =="Si":
                        Ex1=False
                        Ex2=False
                    elif again !="No":
                        print("Comanda desconeguda")
                    else:
                        Ex2=False
    
    #Si no hi ha partides guardades cancela la carrega
    else:
        print("No existeix ninguna partida guardada")

#Afegir jugador
def NuevoJugador():

    #Es demana un nom i es comprova si ja esta registrar amb la funció CompJug()
    Ex2=False
    while not Ex2:
        Ex2,Name1= CompJug()
        if not Ex2:
            print("Aquest jugador ja està registrat")

    #Es demanen les dades del jugador i es comprova si son correctes. S'utilitzen les excepcions per controlar que els valors siguin correctes
    Ex2=True
    while Ex2:

        try:
            Stre=int(input("Introdueix la força del jugador: "))
            Ex2=False
        except:
            print("El valor introduit no es numeric, indrodueixi un valor numeric")
    Ex2=True
    while Ex2:
        try:
            Magi=int(input("Introdueix la màgia del jugador: "))
            Ex2=False
        except:
            print("El valor introduit no es numeric, indrodueixi un valor numeric")
    Ex2=True
    while Ex2:
        try:
            Vel=int(input("Introdueix la velocitat del jugador: "))
            Ex2=False
        except:
            print("El valor introduit no es numeric, indrodueixi un valor numeric")
        
    #Es crea el jugador i s'afegeix al atribut llista del obj Joc
    Joc.NouJugador(Name1,Stre,Magi,Vel)

#Eliminar jugador
def ElimJug():

    #Es demana un nom i es comprova si no esta registrar amb la funció CompJug()
    Ex2=True
    while Ex2:
        Ex2,Name2= CompJug()
        if Ex2:
            print("Aquest jugador no està registrat")
        
    #S'utilitza la funcio del obj Joc per eliminar el obj del jugador de la llista de jugadors
    if not Ex2:
        Joc.ElimJugador(Name2)

#Decrementa salut
def RestarSalut():

    #Es comprova que el jugador seleccionat existeix en la llista del obj Joc
    Ex2=True
    while Ex2:
        Ex2,Name3= CompJug()
        if Ex2:
            print("El jugador seleccionat no existeix")
      
    #Es comprova que el valor a restar es valid, s'utilitza una excepcio per comprovar qu el valor introduit sigui correcte
    Ex2=True
    while Ex2:
        try:
            Rest=int(input("Introdueix el valor de salut a restar: "))
            Ex2=False
        except:
            print("El valor introduit no es numeric, indrodueixi un valor numeric")

    #S'utilitza la funcio del obj Joc per decrementar la salut al jugador seleccionat
    Joc.RestSalut(Name3,Rest)

#Comprar element
def Buy():

    #Es comprova que el jugador seleccionat existeix en la llista del obj Joc
    Ex2=True
    while Ex2:
        Ex2,Name4= CompJug()
        if Ex2:
            print("El jugador seleccionat no existeix")

    #Es comprova que el element seleccionat existeix en la llista del obj Joc
    Ex2=True
    while Ex2:
        Ex2,NameEle= CompElem()
        if Ex2:
            print("El element seleccionat no existeix")
        
    #S'elimina la riquessa del usuari, se li transfereix el element i es redueix l'element de la llista del obj Joc. S'utilitzen excepcions per identificar si el jugador no pot realitzar l'accio i perque
    try:
        Joc.ComprarElem(Name4,NameEle)
    except ValueError:
        print("El jugador no disposa de diners suficients per comprar aquest element")
    except TypeError:
        print("L'element seleccionat s'ha esgotat")

def UseElem():
    
    #Es comprova que el jugador seleccionat existeix en la llista del obj Joc
    Ex2=True
    while Ex2:
        Ex2,Name5= CompJug()
        if Ex2:
            print("El jugador seleccionat no existeix")

    #Es comprova que el element seleccionat existeix en la llista del obj Joc
    Ex2=True
    while Ex2:
        Ex2,NameEle= CompElem()
        if Ex2:
            print("El element seleccionat no existeix")

    #Es comprova si el jugador té l'element i si es fungible o no. Si es fungible s'esborra l'element de la seva llista.
    try:
        Joc.UsarElement(Name5,NameEle)
    except:
        print("El jugador no poseeix aquest element")


#S'importen els fitxers .py de les classes utilitzades
from Part import Partida

#S'estableix previament un fitxer .txt on s'almacena l'informació del elements
FitxerElements="Elements.txt"

#Extracció de l'informació del fitxer
fitxer=open(FitxerElements,"r")
elem=fitxer.readlines()
fitxer.close()

#S'inicia la partida i s'estableixen les condicions inicials. El programa també comprova si el fitxer Elements.txt te algú error en els valor
Joc=Partida()
print("Partida iniciada")
ElemError=False
try:
    for a in elem:
        if a[len(a)-1]=="\n":
            a=a[0:len(a)-1]
        info=a.split("-")
        Joc.CarregarPartida(info[0],info[1],info[2],info[3])
except:
    print("Ha ocorregut un error en els elments predefinits de la partida, comprobi que la sintaxi es la correcta")
    ElemError=True
#Menu d'usuari
Ex1=True
while Ex1:

    #Si s'ha detectat algun error en el fitxer Elements.txt el programa s'acaba
    if ElemError:
        break

    #Es comproba l'opció escollida i si l'entrada de l'usuari es valida
    Ex2=True
    while Ex2:
        Opc=input("Seleccioni una opcion:\n[1]:\tAfegir un jugador\n[2]:\tEliminar un jugador\n[3]:\tDecrementar salut\n[4]:\tComprar element\n[5]:\tUsar element\n[6]:\tMostrar partida\n[7]:\tCargar partida\n[8]:\tGuardar partida\n[9]:\tFinalitzar partida\nOpció: ")
        if Opc=="1" or Opc=="2" or Opc=="3" or Opc=="4" or Opc=="5" or Opc=="6" or Opc=="7" or Opc=="8" or Opc=="9":
            Ex2=False
        else:
            print("Command desconegut\nRecora que les opcions són: [1] [2] [3] [4] [5] [6] [7] [8] [9]")

    #Afegir un jugador
    if Opc=="1":
        NuevoJugador()

    #Eliminar Jugador
    if Opc=="2":
        ElimJug()
    
    #Decrementar salut
    if Opc=="3":
        RestarSalut()

    #Comprar element
    if Opc=="4":
        Buy()
    
    #Usar element
    if Opc=="5":
        UseElem()

    #Mostrar partida
    if Opc=="6":
        print(Joc)
    
    #Carga les dades de una partida anterior
    if Opc=="7":
        Cargar()

    #Guarda les dades introduides sobre la partida en un fitxer
    if Opc=="8":
        Guardar()
    
    #Finalitza la partida
    if Opc=="9":
        break
        
