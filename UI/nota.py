"""FlightDelays —> grafo non orientato e pesato in cui nodi tutti gli aeroporti con nMIn di compagnie aeree e archi con tutti gli aeroporti per cui c’è un volo, con peso numero di voli tra aeroporti (indifferentemente da A->B o B->A)
Baseball —> grafo non orientato e pesato, con nodi le squadre di un anno e archi il totale dei salari di entrambe in quell’anno
iTunes —> grafo non orientato e non pesato, album collegati se una loro canzone esiste in una stessa playlist, componente connessa dimensione/durata complessiva album
Lab13 --> grafo orientato e pesato, piloti collegati se nell’anno hanno finito una gara entrambi e peso numero di volte arrivato prima - numero di volte arrivato dopo
10-07-25 (A) —> grafo diretto e pesato in cui i nodi sono i prodotti di una categoria e gli archi sono i prodotti venduti in un range di date con peso uguale alla somma delle volte che sono stati venduti (non le quantità). Inoltre stampare i migliori 5 score come archi uscenti - archi entranti
1
10-07-25 (B) —> uguale ma peso uguale al numero di pezzi venduti (campo quantità)
26-06-25 (A) —> grafo con nodi tutti i circuiti e archi se circuiti con una gara nel range di anni. Componente connessa, e soprattutto map negli attributi di un oggetto, evitando la query per gli archi
26-06-25 (A) —>
13-01-25 —> grafo semplice e pesato in cui i nodi sono le classificazioni (localization e geneid) con archi se presente interazione tra nodi e peso somma di colonna di tabella. Archi ordinati e componente connessa >1 e ordinata in ordine decrescente """