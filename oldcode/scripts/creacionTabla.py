import pandas as pd
import filtroDB
import util
from bs4 import BeautifulSoup

#MODOS: Numerico y Veredas
def crearTabla(modo, ciudadInput, veredaInput, numero):

    ciudad = util.replaceTildes(ciudadInput)
    vereda = util.replaceTildes(veredaInput)

    dataframe = ''

    if(modo == 'Numerico'):
        nombreTabla = ciudad+str(numero)
        dataframe = filtroDB.filtroPorCiudadNumero(ciudad=ciudadInput, numero=numero, ciudadFileName=ciudad)
    elif(modo == 'Veredas'):
        nombreTabla = ''
        if(type(vereda) == list):
            for ver in vereda:
                nombreTabla += ver
        else:
            nombreTabla = ciudad+vereda
        dataframe = filtroDB.filtroPorCiudadVereda(ciudad=ciudadInput, vereda=veredaInput, ciudadFileName=ciudad, veredaFilename= vereda)
    else:
        print('Por favor especificar el modo de uso para la creación de tablas: Numerico o Veredas')
        return
    
    #crear un HTML desde un Datframe de python
    archivoHTML=dataframe.to_html()
    
    #Establecemos la ruta donde vamos a guardar la tabla
    rutaArchivo=f"tables/{nombreTabla}.html"
    util.checkOrCreateFile(rutaArchivo)

    
    #Generamos una estructura HTML
    encabezadoHTML=f''' 
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>tablas</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
            <img src="../graphics/{nombreTabla}.png">
    '''
    
    #Adaptar los estilos de la tabla
    sopa=BeautifulSoup(archivoHTML,'html.parser')
    
    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML=str(sopa)
    

    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    
    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")



#Creación de tabla por filtro de número de árboles y ciudad
#crearTabla('Numerico', 'Medellín', 'NA', 200)

#Creación de tabla por filtro de veredas
crearTabla('Veredas', 'Medellín', 'El Yolombo', 0)
