import os

def checkOrCreateFile(path):

 # Check if the file already exists
    if not os.path.exists(path):
        # If the file doesn't exist, create it
        with open(path, 'x') as f:
            pass
        print(f"File '{path}' created successfully.")
    else:
        print(f"File '{path}' already exists.")

def replaceTildes(string):

    output_string = ''

    if(type(string) == list):
        for s in string:
            output_string += s.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') \
                .replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U') \
                .replace('ñ', 'n').replace('Ñ', 'N').replace(' ', '')
    else:
        output_string = string.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') \
                .replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U') \
                .replace('ñ', 'n').replace('Ñ', 'N').replace(' ', '')
    
    
    return output_string