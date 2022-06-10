import PyPDF2
import os

caminho_dos_pdf = 'pdf'


novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdf):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdf}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


with open(f'{caminho_dos_pdf}/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    reader = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = reader.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = reader.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/pdf{num_pagina + 1}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
