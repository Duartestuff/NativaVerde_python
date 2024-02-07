import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def filtroPorCiudadNumero(ciudad, numero, ciudadFileName):
    
    df = pd.read_csv('database/Siembras.csv')
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
    finalDf = df.loc[(df['Ciudad'] == ciudad) & (df['Arboles'] > numero)].sort_values(by='Fecha')
    


    plt.plot(finalDf['Fecha'], finalDf['Arboles'], color='blue')
    plt.scatter(finalDf['Fecha'], finalDf['Arboles'], color='blue', marker='o')


    # Set the tick frequency and date format for the x-axis
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # Set ticks to display once per year
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format the date labels
    plt.xlabel('Fechas')
    plt.ylabel('Árboles plantados')
    plt.title(f'Más de {numero} Árboles plantados en {ciudad}')

    plt.savefig(f'graphics/{ciudadFileName}{numero}.png')

    return finalDf

def filtroPorCiudadVereda(ciudad, vereda, ciudadFileName, veredaFilename):

    df = pd.read_csv('database/Siembras.csv')
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)
    
    veredas = ''
    finalDf = ''
    
    if(type(vereda) == list):
        
        for ver in vereda:
            veredas += ver

        finalDf = df.loc[
            (df['Ciudad'] == ciudad) & (df['Vereda'].isin(vereda))
        ].sort_values(by='Fecha')
    
    else:
        veredas = vereda
        finalDf = df.loc[
        (df['Ciudad'] == ciudad) & (df['Vereda'] == vereda)
        ].sort_values(by='Fecha')

    plt.plot(finalDf['Fecha'], finalDf['Arboles'], color='blue')
    plt.scatter(finalDf['Fecha'], finalDf['Arboles'], color='blue', marker='o')


    # Set the tick frequency and date format for the x-axis
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # Set ticks to display once per year
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format the date labels
    plt.xlabel('Fechas')
    plt.ylabel('Árboles plantados')
    plt.title(f'Árboles plantados en {ciudad} y {veredas}')

    plt.savefig(f'graphics/{ciudadFileName}{veredaFilename}.png')

    return finalDf

    
    

