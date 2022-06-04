"""
OS, SYS, FNMATCH - Convertendo vídeos com Python + FFMPEG
https://ffmpeg.org/documentation.html
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    command_ffmpeg = 'ffmpeg'
else:
    command_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bit_rat = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:15'

caminho_de_origem = r'\Users\user\Downloads'
caminho_destinado = r'\Users\user\os tst\99'

for root, dirs, files in os.walk(caminho_de_origem):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue

        caminho_completo = os.path.join(root, file)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.mp4'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s mp3 -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(file)

        arquivo_saida = rf'{caminho_destinado}\{file}_novo{extensao_arquivo}'

        command = f'{command_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} ' \
                  f'{codec_audio} {bit_rat} {debug} {map_legenda} "{arquivo_saida}"'

        os.system(command)
