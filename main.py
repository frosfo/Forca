import os
import requests
from bs4 import BeautifulSoup

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

req = requests.get('https://www.palabrasaleatorias.com/palavras-aleatorias.php')
sopa = BeautifulSoup(req.content,"html.parser")
pa = sopa.find(attrs={"style":"font-size:3em; color:#6200C5;"}).get_text().strip().upper()
pu = list("_"*len(pa))
on = True
vi = 5
count = 0
er = ' '
len = len(pa)
while vi > 0 and count < len:
	cls()
	acerto = False
	print(pu)
	print(vi,"vidas. Erros:",er)
	c = input("letra: ").upper()
	x = 0
	while x < len:
		if(pa[x] == c):
			if (c != pu[x]):
				pu[x] = pa[x]
				count += 1
			acerto = True
		x += 1
	if(acerto == False):
		vi -= 1
		er = er+c+' '
if vi == 0:
	print('PERDEU')
	print('a palavra era:  ', pa)
else:
	cls()
	print(pu)
	print('GANHOU!')
input()