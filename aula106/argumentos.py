"""
Sys.argv - Executando arquivos com argumentos no sistema
"""
import sys
import os

args = sys.argv
if len(args) <= 1:
    print('faltando argumentos:')
    print('-a para lista todos os arquivos nessa pasta', sep='\t')
    print('-d para lista todos os diretórios nessa pasta', sep='\t')
    sys.exit()

so_arquivos = False
so_dicts = False

if '-a' in args:
    so_arquivos = True

if '-d' in args:
    so_dicts = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_dicts:
        if os.path.isdir(arquivo):
            print(arquivo)
