with open('poesia.txt', 'r') as r:
    print(r.read())

with open('poesia.txt', 'a+') as a:
    a.write('\noutra linha')
