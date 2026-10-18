# Protocollo di verifica e playtest

Baseline 0.2, 18 ottobre 2026. Non sono ancora disponibili risultati di gioco: ogni verifica qui descritta è pianificata.

## Evidenze tecniche

Ogni report registra commit, versione engine/build, hardware, preset, numero di processi e PC, rete, passi, atteso, osservato e log pertinenti. Conservare report sintetici in `Docs/Playtests/`; build, log voluminosi e dati personali restano fuori da Git. Nessuna credenziale o indirizzo personale nei report pubblici.

| Percorso | Verifica minima |
| --- | --- |
| Sessione | Host + uno/tre client; quinto rifiutato; errore di ingresso/versione; ingresso tardivo |
| Rete | Almeno due PC; percorso esterno concordato; 80 ms RTT e 1% perdita simulata; uscita/rientro; perdita host |
| Nave | Calma e mare mosso; vento laterale/favorevole/contrario; carico spostato; scale e postazioni durante rollio |
| Mansioni | Ogni minigioco con uno/due utenti; interruzione; stessa postazione contesa; disconnessione con oggetto |
| Progressi | Profili distinti; nuovo imbarco; salvataggio/caricamento; dati assenti/corrotti; premi ripetuti |
| Prestazioni | Scena ripetibile, mediana/picchi di frame time e memoria/rete; confronto al budget fissato prima del test |
| Pacchetto | Avvio e percorso completo fuori dall'editor su dati puliti; dipendenze/licenze e istruzioni |

Le verifiche in Play accelerano l'iterazione. I gate richiedono anche build e macchine reali. `Repository checks` non verifica Blueprint, fisica, packaging o divertimento. I difetti osservati diventano issue specifiche; P0/P1 e nuove dipendenze bloccano il gate pertinente finché verificati.

## Playtest della demo

Budget iniziale **6 OH totali**, comprensive di circa 3 ore-partecipante (sei persone per 30 minuti), 1 OH di osservazione, 1 OH di preparazione e 1 OH di raccolta/sintesi. Il lavoro dell'agente per preparare e analizzare il test è separato: 2 OA nella relativa issue. Reclutamento e indisponibilità sono attese esterne. Un test ripetuto richiede nuovo budget; sei OH non garantiscono una quantità indefinita di sessioni.

1. Reclutare due gruppi distinti: due persone, poi tre o quattro. Raccogliere consenso per osservazioni; registrazioni solo se autorizzate. Usare identificativi anonimi e non pubblicare dati personali.
2. Fissare build, obiettivi, soglie e domande prima dell'inizio. Fare la verifica tecnica prima di chiedere giudizi sul gioco.
3. Lasciare scegliere mozzo/cuoco. Fornire soltanto le istruzioni presenti nella demo; annotare quando il facilitatore deve intervenire.
4. Osservare il viaggio e raccogliere richieste di aiuto, errori, incidenti di camera, episodi di coordinamento, ripetizioni e attese oltre due minuti dovute all'assenza di lavoro o a ruoli bloccati.
5. Chiedere individualmente: obiettivo compreso? contributo utile? piacere della collaborazione da 1 a 5? mare leggibile e controlli confortevoli? altro viaggio sì/no e perché? cosa togliere o cambiare?
6. Confrontare osservazioni e risposte con i criteri di [Demo](Demo.md). Distinguere problemi tecnici, incomprensione e poco interesse. Il responsabile registra GO/ITERATE/REWORK con le evidenze.

Segnali contrari: un ruolo passa il viaggio inattivo; il lavoro sembra manutenzione senza scelte; il mare impedisce di agire; i partecipanti aspettano che qualcun altro finisca; nessuno desidera un altro imbarco. Non mascherare questi segnali con la sola assenza di crash.

## Gate delle fasi successive

Ogni fase ha un report, una sessione umana e una decisione esplicita. Carriera: verificare scelta a ogni imbarco e amici con XP diversi. Comando: utilità dei minigiochi e delega a una ciurma limitata. Flotta: decisioni e passaggio fra nave vicina e spedizione delegata senza duplicazioni. Villa: crescita visibile e collegamento concreto alla vita in mare.

La beta finale prevede **16 OH iniziali** per partecipanti, preparazione e osservazione dell'arco completo; durata e reclutamento vanno raffinati dopo aver deciso il ritmo della carriera. Test accelerati con profili predisposti verificano collegamenti e salvataggi, ma non dimostrano che il ritmo naturale dal mozzo alla villa sia divertente. Se il ritmo richiede più osservazione, aggiungere sessioni e aggiornare OH prima del gate release.

## Chiusura

Un report riporta anche controlli non eseguiti, OA/OH misurate oppure «non misurate», difetti aperti e prossimo passo. Non chiudere una issue con accettazione umana pendente. Un gate fallito rimane aperto; le correzioni sono nuove issue atomiche con verifica e dipendenze. Eventuali eccezioni ai criteri sono decisioni di prodotto visibili, non successi tecnici presunti.
