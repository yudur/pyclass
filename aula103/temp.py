"""
String - Template
"""

from string import Template
from datetime import datetime

data = datetime.now()
dataf = data.strftime('%d/%m/%Y')

with open("template.html", 'r') as html:
    templete = Template(html.read())
    corpo_msg = templete.safe_substitute(nome='Yudi Duarte', data=dataf)

print(corpo_msg)
