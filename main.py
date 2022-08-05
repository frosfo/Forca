import re
import os
from urllib.request import Request, urlopen

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

req = Request('https://www.palabrasaleatorias.com/palavras-aleatorias.php', headers={'User-Agent': 'Mozilla/5.0'})
palavras = urlopen(req).read()[14133:]
pa = re.search(re.compile(  rb'([A-Za-z-]+)</div>\r\n<br />\r\nPesquisa significado em:'), palavras).group(1).decode().upper()

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
