-----------------------------------Lezione 1 esercizi assegnati--------------------------------

---Esercizio 1 --

----TRACCIA----

Test del Teorema dei numeri primi
Scade il 28 aprile 2020 23:59
Istruzioni
Verificare la distribuzione dei numeri primi in Python.
Scrivere un programma Python the dato un intero N, calcola e stampa il numero di primi minori di N ed accanto ad esso il valore di log(N) /N. 

vedere Wikipedia (Teorema dei Numeri Primi) 
----------------

--COMMENTO PROFESSORE--
 nel ciclo interno, lei conta i non divisori. ma è necessario per sapere se n è primo? 
morale: non fate più lavoro delle specifiche.

p.s. l'esercizio viene meglio se invece di pensarlo per un singolo N, lo considera come calcolare i valori delle funzioni:
p(n) = numero dei primi <= n e
n/log n, per ogni n < N.
N è grande. e quando intendo grande intendo roba stile 10^9 o anche di più.
Stampare tutti i valori può essere inutile, basterebbe stampare a questo punto ogni 10000, o 10000. 
l'idea è poi plottare queste due curve.

p.s.s. deve arrivare proprio fino ad 'i' nel ciclo interno?
----------------

----Esercizio 2-----

----TRACCIA----

Simulazione dei Due Corpi
programming
Scade il 28 aprile 2020 23:59
Istruzioni
Per il background fisico, vedi su:  https://it.wikipedia.org/wiki/Problema_dei_due_corpi

Si tratta di simulare la traiettoria (orbita) di un pianeta attorno ad un sole. Semplificare al massimo il modello, in particolare 

uno dei corpi (il sole) è fermo nell'origine, quindi le coordinate dell'altro corpo sono 'relative' ad esso, e la sua posizione coincide

con le loro distanze. Per semplificare ulteriormente, si consideri m1+m2 = 1 e m2*G = 1 quindi la legge del moto si riduce a

r'' = - 1 / r^2 * r

dove r è il vettore posizione del pianeta, si considerino quindi le condizioni iniziali :  r = [1,0,0] e r' = v = [ 0, 0.5, 0].

(si lavora in 3d ma in effetti il moto è ristretto al piano). Scrivere un programma Python che riceve in input il valore

dt = (esempio: 0.01) e stampa le coordinate del pianeta ( r ) per tutti i t in [0,10] a passi di dt.

----Esercizio 3-----

----TRACCIA---

eorema di Bolzano, conseguenze costruttive.
Scade il 28 aprile 2020 23:59
Istruzioni
Come avete studiato ad Analisi 1, il teorema di Bolzano, https://it.wikipedia.org/wiki/Teorema_di_Bolzano

è costruttivo, infatti si definisce una successione di valori reali che converge allo zero della funzione.

Scrivere un programma python che cerca gli zeri dell'equazione non lineare e^x-4sin(x)cos(x) == 0.

Il programma chiede due numeri che definiscono l'intervallo di partenza [a,b], verifica le condizioni di

applicazione del teorema e cerca uno degli zeri. Ragionare sulle condizioni di terminazione.


--------------------------------------Lezione 2 esercizi assegnati---------------------------------
----Esercizio 1-----

----TRACCIA---

Fattorizzazione
Scrivere una funzione che dato un intero N, restituisce una lista di coppie (pi, ai) dove pi è primo e divide N e ai è il suo esorinenre.
esponente.


--------------------------------------Lezione 3 esercizi assegnati---------------------------------

----Esercizio 1-----

----TRACCIA---

Problema n-corpi
Scaduto ieri alle 23:59
Istruzioni
Se riuscite provate a estendere il problema trattato per i due corpi in due direzioni:

 

Sempre per due corpi, usate degli integratori più accurati, LeapFrog (secondo ordine) o rudge-kutta, verificate che per lo stesso valore di dt, avete migloramenti significativi nella convergenza, (potete farlo ad esempio controllando la variazione tra l'energia totale del sistema all'inizio e alla fine, e misurando l'errore assoluto e relativo rispetto a queste quantità). 
Riscrivere il modello per n-corpi (passare da due a tre non è più facile che passare a 100).
Provate il passo 2 usando la progettazione ad oggetti.

----Esercizio 2-----

----TRACCIA---

Studio delle Orbite dei Numeri di Fibonacci in Zn
Scaduto ieri alle 23:59
Istruzioni
Carissimi, un interessante quesito posto tra una chiacchiera e un altra dal prof. Chirivì:

 

Fissato un intero n positivo, si studi come la successione di Fibonacci viene ridotta modulo n.

In particolare si vuole studiare qual'è il periodo (lunghezza prima di una ripetizione) di F_k mod n in funzione di n.

 

Se n è primo c'è un modo per calcolare questo periodo, poichè divide n^2-1, in generale è possibile ricavare

la lunghezza del periodo, guardando i primi che dividono n, ma non è proprio banale.

 

Ecco, questo è un tipico esempio di 'esplorazione' su un problema di teoria dei numeri.

Ne approfitto per segnalarvi, che le successioni modulo un intero sono ESTREMAMENTE importanti.

Molti di voi sanno che è possibile in tutti i linguaggi di programmazione generare numeri pseudo-casuali,

ma pochi sanno come viene davvero fatto, ebbene questo è di solito il modo più comune:

 

https://wiki2.org/en/Linear_congruential_generator

 

Esercizio, usate jupyter per creare un notebook, dove scrivete (in Markdown) la descrizione sopra, e provate

a esplorare cosa accade, notate che dovreste distinguere i casi n primo dagli altri, e ovviamente per avere

senso n dovrebbe essere abbastanza grande da non dover far ricadere il problema su cose banali.

 

Come si genera quindi un intero primo molto grande?

----Esercizio 3-----

----TRACCIA---

---------a-----------
Problemi di vicinanza
Scade oggi alle 23:59
Istruzioni
Le problematiche di distanziamento, sono interessanti anche algoritmicamente.

 

Data una distribuione di N punti in R^2, vogliamo trovare la coppia di punti più vicina. Il problema è banale tutto sommato, quindi mi aspetto che TUTTI davvero riescano a risolverlo piuttosto velocemente.
Calcolate quanti confronti tra coppie di punti vengono eseguite dal vostro programma in funzione di N, questa misura (che domina tutto il resto) è una classica misura di Complessità Computazionale (potete ignorare termini di ordine piccolo e esprimere il tutto in termini di una funzione di N, tipo NLogN, N, N^2, N^3 etc).
Esiste secondo voi un algoritmo che può risolvere il problema con meno confronti ? e se si, come ? e se no come si potrebbe dimostrare che NON esiste?


---------b-----------

Un altro problema fondamentale usatissimo come primitiva in campi amplissimi come l'intelligenza artificiale, l'ottimizzazione etc etc etc. è il seguente:

 

Dato una spazio metrico (R^n, d),  con n fissato (anche molto grande), e d la solita distanza (euclidea va bene, ma potrebbe anche non esserlo), 

e  la solita distribuzione P di N punti in R^n , dato un punto p \in R^n, ed un valore r, trovare tutti i punti di P che sono a distanza al più r da p 

(i punti dentro la palla di raggio r in R^n). Anche questo problema si risolve banalmente con una ricerca che verifica la distanza per ogni punto di P da p,

ovvio e mortalmente lento (N dovete pensarlo > 10^6). Provate a capire se è possibile fare meglio, a partire dal caso più semplice n = 1 (sulla retta),

per poi passare al piano e su di dimensione (salendo, vi imbatterete in un fenomeno chiamato: Curse of the Dimensionality)

 

Implementate la soluzione banale e provate ad usarla per N molto grande, verificate come l'algoritmo lineare diventa poco usabile (dipende dai vostri pc, ma anche dal fatto che è inerentemente lento).
provate a pensare nel caso n = 1, come si potrebbe velocizzare la ricerca..(vi dico già..è semplice).
da n = 2 diventa molto più complesso ma fattibile.
da n > 3 le soluzioni sopra funzionano, ma perdono rapidamente di efficacia col crescere di n.
 
---------------------



