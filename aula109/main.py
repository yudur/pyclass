"""
Subprocess - Executando programas e comandos externos

windows - ping 127.0.0.1
linux - ping 127.0.0.1 -c 4
"""
import subprocess

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('Resposta', 'Danone')

print(saida)
