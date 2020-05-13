
#devo mettere un contatore per determinare il periodo
#posso contare dopo quanto compare 0 1 1

#poi devo fare una funzione periodo - modulo
#la plotto per vedere cosa esce

#per i primi il periodo divide sempre n^2-1 , da rivedere

#--------------------------------------------
#Se voglio scegliere in input l'n faccio questo
#nterms = int(input("How many terms? "))
#-------------------------------------------

nterms=int(40);
# first two terms
n1, n2 = 0, 1
count = 0
# -------------------------------------------------Restistuisce Succ_fibonacci modulo n
mod_n = int(input("Modulo n = ? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1%k)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1%mod_n)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
	   
