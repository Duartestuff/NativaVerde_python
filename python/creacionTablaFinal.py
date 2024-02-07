import pandas as pd
import grafica as gr
import util
from bs4 import BeautifulSoup

def crearTablaGrafico(ciudad):

    filtro_graficas = ['Fecha', 'Arboles']
    orden_columnas_data = ['Vereda', 'Arboles', 'Hectareas', 'Fecha', 'Nombre comun', 'evento']
    ciudad_filename = util.replaceTildes(ciudad)

    data = pd.read_excel('../database/corrected_file.xlsx')
    data_filtro = {}

    if(ciudad == 'Colombia'): data_filtro = data
    else: data_filtro = data.loc[(data['Ciudad'] == ciudad)]    

    data_grafica = data_filtro[filtro_graficas]

    gr.crearGrafica(data_grafica, ciudad, ciudad_filename)

    #crear un HTML desde un Datframe de python
    archivoHTML=data_filtro[orden_columnas_data].to_html()

    #Establecemos la ruta donde vamos a guardar la tabla
    rutaArchivo=f"../{ciudad_filename}.html"
    util.checkOrCreateFile(rutaArchivo)


    #Generamos una estructura HTML
    encabezadoHTML=f''' 
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>{ciudad_filename}</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
            <img src="graphics/{ciudad_filename}.png">
    '''

    #Adaptar los estilos de la tabla
    sopa=BeautifulSoup(archivoHTML,'html.parser')

    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML=str(sopa)
    

    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    
    
    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezadoHTML}\n{archivoHTML}\n</body>\n</html>")