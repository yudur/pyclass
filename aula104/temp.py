import string
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

gmail = input('digite seu gmail: ')
senha = input('digite sua senha: ')
gmail1 = input('digite o gmail do cliente: ')
nome = input('qual o nome da pessoa: ')

with open('templete.html', 'r') as html:
    templete = string.Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = templete.substitute(nome=nome, data=data)

msg = MIMEMultipart()
msg['from'] = 'Yudi Mendes Duarte'
msg['to'] = gmail1  # clientes
msg['subject'] = 'ATENÇÃO: isto é apenas um teste'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('tst.jpg', 'rb') as image:
    image = MIMEImage(image.read())
    msg.attach(image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(gmail, senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail não foi enviado...')
        print(f'Error: {e}')
