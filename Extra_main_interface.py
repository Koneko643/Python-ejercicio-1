#Comprova si el jugador introduit ja esta registrat o si les dades introduides son correctes
def NPlayer(Name,Forç,Mag,Vel):
    Confirm1=Joc.JugConfirm(Name)
    Confirm2=True
    try:
        Forç=int(Forç)
        Mag=int(Mag)
        Vel=int(Vel)
    except:
        Confirm2=Confirm2=False

    #Si no es detecta cap error es crea el jugador i s'afegeix al atribut llista del obj Joc
    if Confirm1 and Confirm2:
        Joc.NouJugador(Name,Forç,Mag,Vel)
    
    #Si es detecta algun error salta una popup especifica per el error detectat
    elif not Confirm1:
        messagebox.showwarning("No es pot registrar","Aquest jugador ja esta registrat")
    elif not Confirm2:
        messagebox.showwarning("No es pot registrar","Les dades introduides als atributs no son correctes")

#Comprova si el jugador introduit esta registrat
def DPlayer(Name):
    Confirm=Joc.JugConfirm(Name)

    #Si no es detecta cap error s'elimina el jugador de la llista del obj Joc
    if not Confirm:
        Joc.ElimJugador(Name)

    #Si es detecta algun error salta una popup especifica per el error detectat
    else:
        messagebox.showwarning("No es pot eliminar","Aquest jugador no esta registrat")

#Comprova si el jugador esta registrat i el valor entrat es correcte
def DDPlayer(Name,Dany):
    Confirm1=Joc.JugConfirm(Name)
    Confirm2=True
    
    try:
        Dany=int(Dany)
    except:
        Confirm2=False

    #Si no es detecta cap error se li resta el valor introduit al jugador seleccionat
    if not Confirm1 and Confirm2:
        Joc.RestSalut(Name,Dany)
    
    #Si es detecta algun error salta una popup especifica per el error detectat
    elif Confirm1:
        messagebox.showwarning("No es pot restar la salut","Aquest jugador no esta registrat")

    #Si es detecta algun error salta una popup especifica per el error detectat
    elif not Confirm2:
        messagebox.showwarning("No es pot restar la salut","Els valors entrats no son correctes")

#Comprova si el jugador esta registrat, si el element esta registrat i si el jugador te els diners suficients per comprar el element
def CPlayer(Name,Item):
    Confirm1=Joc.JugConfirm(Name)
    Confirm2=Joc.ElemConfirm(Item)

    if not Confirm1 and not Confirm2:

        #Si no es detecta cap error se li afegeix el element introduit al jugador seleccionat i se li resta la seva riquessa
        try:
            Joc.ComprarElem(Name,Item)

        #Si es detecta algun error salta una popup especifica per el error detectat
        except ValueError:
            messagebox.showwarning("No es pot comprar l'objecte","El jugador no disposa dels diners suficients")

        #Si es detecta algun error salta una popup especifica per el error detectat
        except TypeError:
            messagebox.showwarning("No es pot comprar l'objecte","L'element seleccionat s'ha esgotat")
    
    #Si es detecta algun error salta una popup especifica per el error detectat
    elif Confirm1:
        messagebox.showwarning("Error en les dades introduides","El jugador seleccionat no existeix")
    
    #Si es detecta algun error salta una popup especifica per el error detectat 
    elif Confirm2:
        messagebox.showwarning("Error en les dades introduides","L'element seleccionat no existeix")

#Comprova si el jugador esta registrat, si el element esta registrat i si el jugador poseeix l'element seleccionat
def UPlayer(Name,Item):
    Confirm1=Joc.JugConfirm(Name)
    Confirm2=Joc.ElemConfirm(Item)

    if not Confirm1 and not Confirm2:

        #Si el item es fungible aquest s'elimina de la llista d'elements del jugador
        try:
            Joc.UsarElement(Name,Item)

        #Si es detecta algun error salta una popup especifica per el error detectat
        except TypeError:
            messagebox.showwarning("No es pot usar l'objecte","El jugador no poseeix d'aquest objecte")
    
    #Si es detecta algun error salta una popup especifica per el error detectat
    elif Confirm1:
        messagebox.showwarning("Error en les dades introduides","El jugador seleccionat no existeix")
    
    #Si es detecta algun error salta una popup especifica per el error detectat
    elif Confirm2:
        messagebox.showwarning("Error en les dades introduides","L'element seleccionat no existeix")

#Comanda per rebre les dades de la partida
def InfoPart():

    #Es carrega la informació en codi de tota la partida mitjançant una funcio de classe 
    
    dats=Joc.Guardar()
    Inf=""
    #Es comprova si hi han jugadors en el fitxer a cargar
    if "*+*" in dats:

        #Es carreguen els jugadors de la partida
        Temp=dats.split("*+*")
        Jug=Temp[1].split("-o-")
        Inf=Inf+"Jugadors:\n"
        for a in Jug:
            Divid=a.split("-.-")
            Sec1=Divid[0].split("*")
            Sec2=Divid[1].split("*")
            Din=100
            Items=""
            #Es comprova si el jugador poseeix elements
            if len(Divid)==3:
                Sec3=Divid[2].split("/o/")
                for a in Sec3:
                    Din-=int(a.split("-")[1])
                    Items=Items+"\n\t\t\t"+a.split("-")[0]
            else:
                Items="\n"
            Inf=Inf+"\n\t"+Sec1[0]+"\n\t\tForça: "+Sec2[0]+"\n\t\tMàgia: "+Sec2[1]+"\n\t\tVelocitat: "+Sec2[2]+"\n\t\tSalut: "+Sec1[2]+"\n\t\tRiquessa: "+str(Din)+"\n\t\tItems del jugador: "+Items
       
        #Es carreguen els elements de la partida 
        Ele=Temp[0].split("--*--")
        Inf=Inf+"\nElements:\n"
        for a in Ele:
            info=a.split("-")
            Inf=Inf+"\n\t"+info[0]+"\n\t\tPreu: "+info[1]+"\n\t\tFungible: "+info[2]+"\n\t\tQuantitat: "+info[3]+"\n"

                    
    #Si en la partida a carregar no existeixen usuaris es carreguen només els elements de la partida
    else:
        Ele=dats.split("--*--")
        Inf=Inf+"\nElements:\n"
        for a in Ele:
            info=a.split("-")
            Inf=Inf+"\n\t"+info[0]+"\n\t\tPreu: "+info[1]+"\n\t\tFungible: "+info[2]+"\n\t\tQuantitat: "+info[3]+"\n"
    
    return Inf

#Comanda per guardar partida
def Guardar(nom):
    
    #Es crea o es sobreescriu, si ja esta creat, el fitxer seleccionat
    fitxer=open("Partidas/"+nom+".txt","w")

    #Es guarda l'informació de la partida en el fitxer seleccionat, si ja existeix es sobreescriu
    part=Joc.Guardar()
    fitxer.write(part)
    fitxer.close()
    
    #Si el fitxer no existia abans es guarda el seu nom en el arxiu que emmagatzema les partides guardades
    fitxerl=open("Partidas/SelecPart.txt","r")
    PartidasG=fitxerl.read()
    PartidasG=PartidasG.split("\n")
    if nom not in PartidasG:
        fitxerw=open("Partidas/SelecPart.txt","a")
        fitxerw.write("\n"+nom)
        fitxerw.close()
#Comando para cargar partida
def Cargar(ncarga):

    #Es comprova que hi ha partides guardades
    fitxer=open("Partidas/SelecPart.txt","r")
    part=fitxer.read().split("\n")
    fitxer.close()
    if len(part)>0:
            
        #Si la partida existeix comença a carregar la informació
        if ncarga in part and ncarga !="Partidas guardadas:":
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
                    
                #Es carreguen els elements de la partida 
                Ele=Temp[0].split("--*--")
                for a in Ele:
                    info=a.split("-")
                    Joc.CarregarPartida(info[0],info[1],info[2],info[3])
                    
            #Si en la partida a carregar no existeixen usuaris es carreguen només els elements de la partida
            else:
                Ele=dats.split("--*--")
                for a in Ele:
                    info=a.split("-")
                    Joc.CarregarPartida(info[0],info[1],info[2],info[3])
            
        #Si la partida no existeix s'activa un warning que indica que la partida no existeix
        else:
            messagebox.showwarning("No es pot carregar la partida","No existeix la partida introduida")
    
    #Si no hi ha partides guardades s'activa un guarning indicant que no hi han partides guardades
    else:
        messagebox.showwarning("No es pot carregar la partida","No existeix ninguna partida guardada")

#Defineix els gadgets de la ventana i els mostra
def WindNewplayer():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaNP=Toplevel()
    ventanaNP.title("Afegir jugador")

    #Inicialització dels textos
    Jug=Label(ventanaNP,text="Nou jugador")
    Nom=Label(ventanaNP,text="Nom")
    Força=Label(ventanaNP,text="Força")
    Magia=Label(ventanaNP,text="Magia")
    Velocitat=Label(ventanaNP,text="Velocitat")
    
    #Inicialització de les entrades
    entryN=Entry(ventanaNP, width=30)
    entryF=Entry(ventanaNP, width=30)
    entryM=Entry(ventanaNP, width=30)
    entryV=Entry(ventanaNP, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaNP,text="Afegir",bd=2, relief=GROOVE, command=lambda:NPlayer(entryN.get(),entryF.get(),entryM.get(),entryV.get()))

    #S'estableix la disposició dels gadgets en la ventana
    Jug.grid(row=0,column=0,columnspan=2,padx=10)
    Nom.grid(row=1,column=0,padx=10,pady=5)
    Força.grid(row=2,column=0,padx=10,pady=5)
    Magia.grid(row=3,column=0,padx=10,pady=5)
    Velocitat.grid(row=4,column=0,padx=10,pady=5)

    entryN.grid(row=1,column=1,padx=10,pady=5)
    entryF.grid(row=2,column=1,padx=10,pady=5)
    entryM.grid(row=3,column=1,padx=10,pady=5)
    entryV.grid(row=4,column=1,padx=10,pady=5)

    Confirm.grid(row=5,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindDelplayer():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaDP=Toplevel()
    ventanaDP.title("Eliminar jugador")

    #Inicialització dels textos
    Jug=Label(ventanaDP,text="Eliminar jugador")
    Nom=Label(ventanaDP,text="Jugador")
    
    #Inicialització de les entrades
    entryN=Entry(ventanaDP, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaDP,text="Borrar",bd=2, relief=GROOVE, command=lambda:DPlayer(entryN.get()))

    #S'estableix la disposició dels gadgets en la ventana
    Jug.grid(row=0,column=0,columnspan=2,padx=10)
    Nom.grid(row=1,column=0,padx=10,pady=5)
    entryN.grid(row=1,column=1,padx=10,pady=5)
    Confirm.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindDamage():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaDD=Toplevel()
    ventanaDD.title("Restar salut")  

    #Inicialització dels textos
    Jug=Label(ventanaDD,text="Restar salut")
    Nom=Label(ventanaDD,text="Jugador")
    Dany=Label(ventanaDD,text="Dany")

    #Inicialització de les entrades    
    entryN=Entry(ventanaDD, width=30)
    entryD=Entry(ventanaDD, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaDD,text="Afegir dany",bd=2, relief=GROOVE, command=lambda:DDPlayer(entryN.get(),entryD.get()))
    
    #S'estableix la disposició dels gadgets en la ventana
    Jug.grid(row=0,column=0,columnspan=2,padx=10)
    Nom.grid(row=1,column=0,padx=10,pady=5)
    Dany.grid(row=2,column=0,padx=10,pady=5)
    entryN.grid(row=1,column=1,padx=10,pady=5)
    entryD.grid(row=2,column=1,padx=10,pady=5)
    Confirm.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindBuy():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaB=Toplevel()
    ventanaB.title("Comprar element")

    #Inicialització dels textos
    Jug=Label(ventanaB, text="Comprar element")
    Nom=Label(ventanaB, text="Jugador client")
    Element=Label(ventanaB, text="Element a comprar")

    #Inicialització de les entrades
    entryJ=Entry(ventanaB, width=30)
    entryE=Entry(ventanaB, width=30)

    #Inicialització del botó
    Confirm=Button(ventanaB,text="Comprar",bd=2, relief=GROOVE, command=lambda:CPlayer(entryJ.get(),entryE.get()))

    #S'estableix la disposició dels gadgets en la ventana
    Jug.grid(row=0,column=0,columnspan=2,padx=10)
    Nom.grid(row=1,column=0,padx=10,pady=5)
    Element.grid(row=2,column=0,padx=10,pady=5)
    entryJ.grid(row=1,column=1,padx=10,pady=5)
    entryE.grid(row=2,column=1,padx=10,pady=5)
    Confirm.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindUse():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaU=Toplevel()
    ventanaU.title("Usar element")
    
    #Inicialització dels textos
    Jug=Label(ventanaU, text="Usar l'element")
    Name=Label(ventanaU, text="Jugador seleccionat")
    Item=Label(ventanaU, text="Item seleccionat")

    #Inicialització de les entrades
    entryJ=Entry(ventanaU, width=30)
    entryI=Entry(ventanaU, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaU,text="Usar",bd=2, relief=GROOVE, command=lambda:UPlayer(entryJ.get(),entryI.get()))

    #S'estableix la disposició dels gadgets a la ventana
    Jug.grid(row=0,column=0,columnspan=2,padx=10)
    Name.grid(row=1,column=0,padx=10,pady=5)
    Item.grid(row=2,column=0,padx=10,pady=5)
    entryJ.grid(row=1,column=1,padx=10,pady=5)
    entryI.grid(row=2,column=1,padx=10,pady=5)
    Confirm.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindShow():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaSH=Toplevel()
    ventanaSH.title("Mostrar partida")

    #Es recull l'informació de la partida
    Inform=InfoPart()

    #Inicialització del frame
    frame1= LabelFrame(ventanaSH, text="Informació de la partida", padx=20, pady=20)
    
    #Inicialització del scrollbar
    Yscroll=Scrollbar(frame1)

    #Inicialització dels textos
    Info=Label(frame1,text="Estadistiques")
    Data=Text(frame1,yscrollcommand=Yscroll.set)

    
    Data.insert(END,Inform)

    Yscroll.config(command=Data.yview)
    
    #S'estableix la disposició dels gadgets en la ventana
    frame1.grid(row=0,column=0)
    Yscroll.grid(row=0,column=1,rowspan=2,sticky=N+S)
    Info.grid(row=0,column=0,padx=10)
    Data.grid(row=1,column=0,padx=10,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindSave():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaS=Toplevel()
    ventanaS.title("Guardar partida")

    #Inicialització dels textos
    Guard=Label(ventanaS, text="Guardar partida")
    Part=Label(ventanaS, text="Selecciona la partida")

    #Inicialització de les entrades
    entryP=Entry(ventanaS, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaS, text="Guardar",bd=2,relief=GROOVE, command=lambda:Guardar(entryP.get()))

    #S'estableix la disposició dels gadgets a la ventana
    Guard.grid(row=0,column=0,columnspan=2,padx=10)
    Part.grid(row=1,column=0,padx=10,pady=5)
    entryP.grid(row=1,column=1,padx=10,pady=5)
    Confirm.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#Defineix els gadgets de la ventana i els mostra
def WindLoad():

    #S'executa la ventana i s'inicialitzen els gadgets
    ventanaLC=Toplevel()
    ventanaLC.title("Cargar partida")

    #Inicialització dels textos
    Guard=Label(ventanaLC, text="Cargar partida")
    Part=Label(ventanaLC, text="Selecciona la partida")

    #Inicialització de les entrades
    entryP=Entry(ventanaLC, width=30)

    #Inicialització del butó
    Confirm=Button(ventanaLC, text="Cargar",bd=2,relief=GROOVE, command=lambda:Cargar(entryP.get()))

    #S'estableix la disposició dels gadgets a la ventana
    Guard.grid(row=0,column=0,columnspan=2,padx=10)
    Part.grid(row=1,column=0,padx=10,pady=5)
    entryP.grid(row=1,column=1,padx=10,pady=5)
    Confirm.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#S'importen els fitxers .py de les classes utilitzades i les llibreries
from Part import Partida
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#S'estableix previament un fitxer .txt on s'almacena l'informació del elements
FitxerElements="Elements.txt"

#Extracció de l'informació del fitxer
fitxer=open(FitxerElements,"r")
elem=fitxer.readlines()
fitxer.close()


#S'inicia la partida i s'estableixen les condicions inicials. El programa també comprova si el fitxer Elements.txt te algú error en els valor
Joc=Partida()
ElemError=False
try:
    for a in elem:
        if a[len(a)-1]=="\n":
            a=a[0:len(a)-1]
        info=a.split("-")
        Joc.CarregarPartida(info[0],info[1],info[2],info[3])
except:
    ElemError=True

#Si es detecta un error al carregar la partida surtira un popup de warning i no s'iniciarà el programa
if ElemError:
    messagebox.showwarning("Error de inicio","Se ha detectado que en el fichero Elements.txt la informacion no esta debidamente escrita")
else:

    #S'executa la ventana i s'inicialitzen els gadgets
    root = Tk()
    root.title("Pratica Programación II Brandon Araníbar")
    
    #Inicialització de un contenidor (frame)
    frame= LabelFrame(root, text="Joc", padx=20, pady=20)
    
    #Inicialització de un text
    Enun=Label(frame,text="Seleccioni una opcion: ")
    
    #Inicialització dels butons
    Opcio1=Button(frame,text="Afegir jugador", width=15, bd=2, bg="#9BFE85", relief=GROOVE, command=lambda:WindNewplayer())
    Opcio2=Button(frame,text="Eliminar un jugador", width=15, bd=2,fg="#FFFFFF", bg="#000000", relief=GROOVE, command=lambda:WindDelplayer())
    Opcio3=Button(frame,text="Decrementar salut", width=15, bd=2, bg="#FE9285", relief=GROOVE, command=lambda:WindDamage())
    Opcio4=Button(frame,text="Comprar element", width=15, bd=2, bg="#FEFE85", relief=GROOVE, command=lambda:WindBuy())
    Opcio5=Button(frame,text="Usar element", width=15, bd=2, bg="#8586FE", relief=GROOVE, command=lambda:WindUse())
    Opcio6=Button(frame,text="Mostrar la partida", width=15, bd=2, bg="#FFFFFF", relief=GROOVE, command=lambda:WindShow())
    Opcio7=Button(frame,text="Guardar partida",width=15,bd=2,bg="#848484", relief=GROOVE, command=lambda:WindSave())
    Opcio8=Button(frame,text="Cargar partida",width=15,bd=2,bg="#C8C8C8", relief=GROOVE, command=lambda:WindLoad())

    #S'estableix la disposició dels gadgets a la ventana
    Enun.grid(row=0, column=0, columnspan=2, padx=10, pady=10)    
    
    frame.grid(row=0, column=0, padx=10, pady=10)
    
    Opcio1.grid(row=1, column=0, padx=5, pady=5)
    Opcio2.grid(row=2, column=0, padx=5, pady=5)
    Opcio3.grid(row=3, column=0, padx=5, pady=5)
    Opcio4.grid(row=1, column=1, padx=5, pady=5)
    Opcio5.grid(row=2, column=1, padx=5, pady=5)
    Opcio6.grid(row=3, column=1, padx=5, pady=5)
    Opcio7.grid(row=4, column=0, padx=5, pady=5)
    Opcio8.grid(row=4, column=1, padx=5, pady=5)
    root.mainloop()