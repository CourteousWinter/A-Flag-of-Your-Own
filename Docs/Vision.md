# Visione del gioco

Baseline 0.2, 18 ottobre 2026. Questa specifica raccoglie le decisioni emerse in chat; distingue requisiti, ipotesi da provare e scelte ancora aperte. La pianificazione non autorizza l'avvio dello sviluppo.

## Esperienza promessa

Costruire una vita in mare insieme agli amici: lavorare a bordo, imparare un mestiere, assumere responsabilità, diventare capitano, possedere navi e una flotta, fino a dirigere le spedizioni dalla propria villa su un'isola. La quotidianità sulla nave deve sostenere questa crescita.

Il ciclo è: scegliere un nuovo imbarco e un ruolo consentito → preparare nave e provviste → collaborare durante il viaggio → ricevere esperienza e ricompense → scegliere il prossimo imbarco o investimento. La crescita introduce nuove decisioni; la delega deve evitare che il comando moltiplichi la manutenzione ripetitiva.

## Decisioni confermate

- Gioco cooperativo con un massimo di **quattro giocatori**. La prova iniziale usa la terza persona.
- Grafica **low poly**, con mare e vento credibili: onde, galleggiamento, carico e vele devono avere conseguenze osservabili. Sea of Thieves e Black Flag sono riferimenti di esperienza, non una promessa di superarli tecnicamente.
- Le attività operative sono minigiochi: comprendere un gesto, eseguirlo, vedere il risultato e poter collaborare. Pulizia della nave, cucina e ordine della stiva sono requisiti espliciti.
- Al massimo **20 NPC sulla nave più grande**, oltre ai giocatori. Non è il numero obbligatorio di ogni equipaggio.
- Cinque ruoli: **mozzo, cuoco, marinaio, capomastro, capitano**. Un nuovo personaggio può partire come mozzo o cuoco.
- L'esperienza appartiene al personaggio e si accumula nel tempo. **A ogni nuovo imbarco si sceglie il ruolo**, fra quelli consentiti dall'esperienza; sbloccare un ruolo non obbliga a utilizzarlo.
- L'arco di crescita arriva al comando, alla flotta e alla villa sull'isola. Contenuti e quantità entro questo arco richiedono un budget finito approvato.

## Ipotesi della demo da validare

Una sola nave, un porto e una traversata breve, due-quattro giocatori, tre lavori collegati al viaggio, un capitano NPC e pochi aiutanti. Durata obiettivo 20–30 minuti. I principianti devono poter giocare insieme anche scegliendo lo stesso ruolo. Ricette, valori di esperienza, economia e frequenza dei lavori sono provvisori.

La demo comprende navigazione fisica e cooperazione su una nave in movimento: una nave ferma con un incarico non basta più a verificare questa promessa. [Demo e criteri di uscita](Demo.md).

## Decisioni ancora aperte

| Decisione | Quando risolverla |
| --- | --- |
| Epoca, area geografica, rig, nomi e numero definitivo delle navi | Scheda della nave demo, poi catalogo prima di produrre altre navi |
| Identità, connessione privata, eventuali servizi online e confine Blueprint/C++ | Spike architetturale prima della cooperativa |
| Modello delle onde e budget per fisica, grafica e rete | Spike mare prima della simulazione |
| Soglie dei ruoli, prove di competenza e tempi di crescita | Prima della carriera estesa |
| Proprietà di denaro, navi, flotta e villa; diritti degli ospiti e portabilità fra host | Decisione di proprietà prima degli acquisti persistenti |
| Numero di navi della flotta, navi fisiche simultanee e progresso offline | Specifica della flotta prima della delega |
| Dimensione dell'isola, livelli della villa, contenuti e durata della 1.0 | Budget delle rispettive fasi e verifica finale del perimetro |

Il profilo personale persistente è confermato; la proprietà condivisa del mondo non lo è. Ogni decisione di prodotto ha una issue e richiede un esito registrato prima di rendere pronte le implementazioni dipendenti.

Combattimento, PvP, MMO, singolo, mondo aperto senza limiti, costruzione libera, simulazione sociale estesa, console, store, server dedicati e migrazione dell'host non sono requisiti approvati. Una proposta futura richiede una decisione e un aggiornamento di scope, stime e dipendenze.

## Mare e vela

Simulazione ben fatta significa relazione coerente fra superficie visibile, forze sullo scafo, vento apparente e manovre, con controllo comprensibile e rete stabile. Low poly non riduce automaticamente il costo della fisica. Non si assume una simulazione volumetrica dell'intero oceano: la scelta fra onde analitiche, FFT ed effetti locali passa da uno spike con evidenze, licenze e profiling.

Le navi sono ispirate a fonti storiche, ma il limite di 20 NPC è una scelta di gioco. Non si presenta una ciurma ridotta come ricostruzione numericamente autentica. [Ricerca e riferimenti](Research/Ships.md).

## Cosa significa gioco finito

Una build Windows del perimetro approvato collega primo imbarco, tutti i ruoli, comando, proprietà, flotta e villa; mantiene progressi e oggetti coerenti in cooperativa, rispetta i budget concordati e supera verifiche tecniche e playtest umani. Un gate fallito riapre l'iterazione e genera correzioni stimate. La 1.0 non è completata soltanto perché tutte le feature hanno codice.

[Roadmap](Roadmap.md) · [Backlog completo](Backlog.md) · [Protocollo di playtest](PlaytestPlan.md)
