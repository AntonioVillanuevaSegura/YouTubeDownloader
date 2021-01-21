"""  
    YouTube downloader Antonio Villanueva Segura
    usando la libreria pytube
    https://github.com/pytube/pytube?fbclid=IwAR1T-KnFOsFrYdbBRZ3U7zUGwcuT-ESZO2TGIL1RLPIKuxY0BZ1JbFol6s0
    sudo apt install python3.7-tk
"""
#!/usr/bin/python
# -*- coding: latin-1 -*-
from pytube import YouTube
from pytube import Playlist
from tkinter import *

def descarga(http):
    #Detecta si es una lista o un video simple
    if ("list" in http):
        listaVideos = Playlist (http) 
        
        for video in listaVideos.videos:
            video.streams.first().download()
                     
    else:#Video simple           
        YouTube(http).streams.first().download()

#Click boton de descarga   
def click(http):
    descarga(http)
    
#Pantalla grafica tkinter  ,Clase que contiene los widgets tkinter
class Graficos: 
    def __init__(self, ventana):
        
        #Instancio el nivel superior widget
        self.ventana=ventana
            
        # Texto
        etiqueta1 = Label (self.ventana, text = "COPIA EL VIDEO QUE QUIERES DESCARGAR")
        etiqueta1.pack()
        
        # Entrada de texto
        entrada1 = Entry (self.ventana,width=100)
        entrada1.pack()    
        
        seleccion1 = Checkbutton (self.ventana ,text = "seleccion 1")
        seleccion1.pack()    
                

        # Boton de descarga
        bouton1 = Button (self.ventana, text = "DESCARGA",fg = "red",command= lambda: click(entrada1.get()) ,
            bd = 2, bg = "light green", relief = "groove")
        bouton1.pack()    
                
#Main        
def main():
    
    max_x=800
    max_y=100
    tam=str(max_x)+"x"+str(max_y)
    
    # Creo una ventana de la clase Tk
    ventana = Tk()
    
    #Titulo
    ventana.title("YouTube Downloader por A.Villanueva ")

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
