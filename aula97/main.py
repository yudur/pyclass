"""
OS - Percorrendo arquivos e pastas
"""
import os

conta = 0
caminho_procura = input('digite um caminho: ')
termo_procura = input('digite um termo: ')


def formata_tamanho(valor):
    base = 1000
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if kilo > valor:
        return f'{round(valor, 2)}B'
    elif mega > valor:
        return f'{round((valor / kilo), 2)}KB'
    elif giga > valor:
        return f'{round((valor / mega), 2)}MB'
    elif tera > valor:
        return f'{round((valor / giga), 2)}GB'
    elif peta > valor:
        return f'{round((valor / tera), 2)}TB'
    else:
        return f'{round((valor / peta), 2)}PT'


for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print(f'encontrei o arquivo: {arquivo}')
                print(f'caminho: C:{caminho_completo}')
                print(f'nome: {nome_arquivo}')
                print(f'extensão: {ext_arquivo}')
                print(f'tamanho em bytes: {tamanho}')
                print(f'tamanho formatado: {formata_tamanho(tamanho)}')

            except PermissionError:
                print('error de permissão')
            except FileNotFoundError:
                print('arquivo não encontrado')
            except Exception:
                print('algo deu errado :(')

print()
print(f'{conta} arquivo(s) encontrado(s)')
