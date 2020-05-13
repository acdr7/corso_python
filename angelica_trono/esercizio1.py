print("Calcolo i primi minori di N, e li conto")
from math import log
N=int(input("Digita N=:"))
n_primi=0
#controllo se un numero minore di N è primo facendo variare l'indice i 
for i in range(2,N):
	non_divisori=0
	#controllo i numeri minori del mio candidato primo facendo variare j
	for j in range(2,i):
		if (i%j)!=0:
			non_divisori+=1
	#nessuno di questi lo deve dividere, il numero dei non divisori deve essere i-2 
	if i-2 == non_divisori:
			print(i,"e' primo")
			n_primi+=1
print("Il numero dei primi minori di ",N," sono ",n_primi,"   N/log(N)=",N/log(N))

