from math import exp
from math import sin
from math import cos
from math import log

#--------------------------------------------------------------------------- funzione
def f(x): return exp(x)-4*sin(x)*cos(x) 
#--------------------------------------------------------------------------- input

a=float(input("inserire a:"))
b=float(input("inserire b:"))
#--------------------------------------------------------------------------- tolleranza
tol=float(1e-6)


#-----------------------------------------------------------------------------Verifico le condizioni del Teorema di Bolzano
fa=f(a)
fb=f(b)
if fa * fb < 0: print(" Valgono le condizioni del teorema di Bolzano")
else: print(" Non valgono le condizioni del teorema di Bolzano")

#---------------------------------------------------------------------------- 1^ criterio di convergenza sul numero dei passi: 
#---------------------------------------------------------------------------- n_passi > log_2((abs(b-a))/tol) 
#-----------------------------------------------------------------------------per teoria studiata in Analisi Numerica

n_passi_consigliati=log((abs(b-a))/tol,2) 
print("Il numero dei passi consigliati affinchè converga è minimo [log((abs(b-a))/tol,2)]+1 cioè" ,int(n_passi_consigliati)+1)


#----------------------------------------------------------------------------Uso l'algoritmo di Bisezione
m=(a+b)/2
fm=f(m)

for i in range(int(n_passi_consigliati)+1): 
    if(fm == 0):
        print("Successo!") 
        break
    elif(fa*fm > 0):
        a=m      ; fa=f(a)
        m=(a+b)/2; fm=f(m)
		
    elif(fb*fm > 0):
        b=m      ; fb=f(b)
        m=(a+b)/2; fm=f(m) 
    else:
        print("Errore...")
        break
print("alla fine del ciclo ottengo fa=%10.6f fm=%10.6f fb=%10.6f" %(fa,fm,fb))
#-----------------------------------------------------------------------------Controllo anche se è vero il 2^ criterio sulla convergenza:
#-----------------------------------------------------------------------------stop=abs(b-a)<tol
stop=abs(b-a)<tol
print("Infatti il criterio di convergenza [abs(b-a)< tol] è" ,stop)

#Professore ho avuto problemi con il while per le condizioni di convergenza quindi ho fatto così, e nel caso non valgono le ipotesi del teorema cicla comunque
