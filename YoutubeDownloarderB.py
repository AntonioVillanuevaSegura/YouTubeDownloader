
"""  
    YouTube downloader Antonio Villanueva Segura
    usando la libreria pytube https://pypi.org/project/pytube/
    documentacion https://python-pytube.readthedocs.io/en/latest/
    https://github.com/pytube/pytube?fbclid=IwAR1T-KnFOsFrYdbBRZ3U7zUGwcuT-ESZO2TGIL1RLPIKuxY0BZ1JbFol6s0
    sudo apt install python3.7-tk
    23012021  incluye checkButton para listas 
    https://nuitka.net/doc/user-manual.html#use-case-1-program-compilation-with-all-modules-embedded    
    python -m nuitka --onefile program.py   
"""
#!/usr/bin/python
# -*- coding: latin-1 -*-
from pytube import YouTube
from pytube import Playlist
from tkinter import *

#Informacion del video descargando
def informacionVideo(video):
    #print( "Titulo",video.title)
    #video.thumbnail_url #imagen
    return video.title
    
def descarga(http,modoLista,informacion,ventana):
    #Detecta si es una lista o un video simple
    if ( ("list" in http) and (modoLista)):
        listaVideos = Playlist (http) 
        
        for video in listaVideos.videos:
            informacion.set (informacionVideo(video))
            ventana.update()            
            video.streams.first().download()
                     
    else:#Video simple  
        video=YouTube(http)
        #Muestra informacion del video descargando
        informacion.set (informacionVideo(video))
        ventana.update()
        video.streams.first().download()

#Click boton de descarga   
def click(http,modoLista,informacion,ventana):   

    if ("https://www.youtube." in http):#filtra el texto seleccionado       
        descarga(http,modoLista,informacion,ventana)
    informacion.set("")#Reset informacion del video en descarga
    ventana.update()    
    
#Pantalla grafica tkinter  ,Clase que contiene los widgets tkinter
class Graficos: 
    def __init__(self, ventana):
        #Variable para ver si esta activado el modo Lista
        modoLista= IntVar()
        informacion = StringVar()
        informacion.set("")
        
        #Instancio el nivel superior widget
        self.ventana=ventana
            
        # Texto
        etiqueta1 = Label (self.ventana, fg="red",text = "COPIA EL VIDEO QUE QUIERES DESCARGAR")
        etiqueta1.pack()
        
        # Entrada de texto
        entrada1 = Entry (self.ventana,width=100)
        entrada1.pack()   
        #entrada1.bind("<1>", handle_click) #funcion evento..
        
        #CheckButton confirmacion de descarga de listas , por si un video simple esta en una lista
        seleccion1 = Checkbutton (self.ventana ,text = "Modo Lista",variable = modoLista)
        seleccion1.pack()    
                
        # Boton de descarga
        bouton1 = Button (self.ventana, text = "DESCARGA",fg = "red",command= lambda: click(entrada1.get(),modoLista.get(),informacion ,ventana) ,
            bd = 2, bg = "light green", relief = "groove")
        bouton1.pack()  
        
        etiqueta2 = Label(self.ventana, textvariable = informacion )
        etiqueta2.pack()        
        
#Main        
def main():
    #Tamano de la ventana
    max_x=800
    max_y=100
    tam=str(max_x)+"x"+str(max_y)
    
    # Creo una ventana de la clase Tk
    ventana = Tk()
    
    #Titulo
    ventana.title("YouTube Downloader por Antonio Villanueva ")

    #Dimensiones de la ventana principal
    ventana.geometry(tam)
    
    #Limites de la pantalla
    ventana.maxsize(max_x,max_y)
    ventana.minsize(max_x,max_y)
 
    #Llamada a la venta
    graficos = Graficos(ventana) 
    
    # Muestra la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
