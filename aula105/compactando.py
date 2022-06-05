from zipfile import ZipFile
import os

# ZIP - Compactando / Descompactando arquivos

# criando arquivo zip
caminho = r'\Users\user\os tst\99'
with ZipFile('Arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# lendo arquivo zip
with ZipFile('Arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# descompactando arquivo zip
with ZipFile('Arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
