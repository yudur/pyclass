"""
OS + SHUTIL - Mover, copiar e apagar arquivos
"""
import os
import shutil

caminho_original = r'\Users\user\Downloads'
caminho_novo = r'\Users\user\os tst'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    pass

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        if 'geracnpj.zip' == file or 'sobrecarga.py' == file:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)

            shutil.copy(old_file_path, new_file_path)
            print(f'arquivo {file} copiado com sucesso')

print()

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        new_file_path = os.path.join(caminho_novo, file)

        if '.zip' in file:
            os.remove(new_file_path)
            print('arquivo apagado.')
