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

"""PUNTO 1 (variante di allenamento)
1. L’utente seleziona da due menù a tendina un anno di inizio e un anno di fine. I menù devono essere popolati interrogando il database per ottenere gli anni in cui è stato disputato almeno un Gran Premio.
2. Premendo sul tasto Crea grafo, l’applicazione dovrà costruire un grafo semplice e pesato, così costituito: a) Nodi: tutti i piloti che hanno preso parte ad almeno una gara nel range di anni selezionato (estremi inclusi). Per ogni nodo, si memorizzi:
    * le proprietà del pilota (colonne della tabella drivers),
    * i risultati delle gare disputate dal pilota nel periodo selezionato (tabella results, campi come raceId, position, points).
3. b) Archi: due piloti sono collegati da un arco se hanno disputato almeno una gara nello stesso Gran Premio nel range di anni selezionato.
    * Il peso dell’arco è pari al numero totale di volte in cui entrambi i piloti hanno ottenuto punti nello stesso GP (ovvero entrambi hanno points > 0 nella stessa gara).
    * Se non hanno mai preso punti insieme, nessun arco viene creato.
4. Una volta costruito il grafo, l’applicazione deve visualizzare:
    * numero di nodi,
    * numero di archi,
    * la coppia di piloti con arco di peso massimo, indicando in quante gare hanno conquistato punti insieme.


Traccia 1 (2 dropdown: Anno, Costruttore) — PUNTO 1
1. L’utente seleziona:
    * Anno (dropdown popolato con gli anni presenti in races.year);
    * Costruttore (dropdown da constructors).
2. Crea grafo → costruisci un grafo diretto e pesato:
    * Nodi: tutti i piloti che hanno disputato almeno una gara nell’anno selezionato per il costruttore scelto.
    * Archi: tra due piloti A e B c’è un arco se hanno corso insieme almeno una gara in quell’anno per lo stesso costruttore (cioè risultano entrambi nei results della stessa raceId con quel constructorId).
        * Verso: dall’alfiere con meno punti stagionali (somma results.points nell’anno per quel costruttore) verso quello con più punti.
        * Parità di punti stagionali → inserisci entrambi gli archi.
    * Peso dell’arco: numero di gare dell’anno in cui i due sono stati compagni di squadra (co-presenze).
    * Se un pilota ha corso solo gare senza compagno → il nodo resta isolato.
3. Dopo la costruzione mostra #nodi e #archi. Bottone Top Driver: stampa i 3 piloti con valore massimo di (somma pesi archi entranti) − (somma pesi archi uscenti) ."""