import requests
import csv
import datetime
import os

try:
    URL = 'https://jsonbox.io/box_9da5210c1a35783aa3a7'

    try:
        response = requests.get(URL)
        json = response.json()
    except:
        raise Exception("Não foi possível obter os dados")
    
    FILE_FOLDER = 'temp/'
    
    if os.path.isdir(FILE_FOLDER) == False:
        os.mkdir(FILE_FOLDER)
    
    file_name =  datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    file_path = FILE_FOLDER + file_name + '.csv'

    try:
        with open(file_path, 'w') as outf:
            dw = csv.DictWriter(outf, json[0].keys())
            dw.writeheader()
            for row in json:
                dw.writerow(row)
    except :
        raise Exception("Não foi possível criar o arquivo")

    print('Arquivo criado')
except Exception as exception:
    print(exception)