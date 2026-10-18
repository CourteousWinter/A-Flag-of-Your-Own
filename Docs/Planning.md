# Pianificazione in ore-agente

## Unità di misura

**1 OA = 1 ora di lavoro attivo di un agente di riferimento sul progetto**, con accesso al repository e agli strumenti previsti. La stima comprende lettura del contesto, implementazione, test pertinenti, documentazione, correzioni di review e integrazione. Per rendere confrontabili le stime, annotare nella issue il tipo di agente/modello e gli strumenti quando differiscono dal flusso abituale.

OA misura impegno, non punti astratti, costo in token o scadenza. Due agenti per due ore ciascuno consumano **4 OA**. Una issue da 4 OA eseguita da un solo agente richiede circa quattro ore attive se la stima è corretta. Due agenti non dimezzano automaticamente la durata: dipendenze, asset condivisi e integrazione limitano il parallelismo. Sommare anche l'eventuale coordinamento attivo, senza contare due volte la stessa sessione.

Escludere attese esterne e build non supervisionate dal lavoro attivo; riportarle come durata separata se rilevanti. Stimare **OH (ore umane)** separatamente per decisioni di design, revisione visiva e playtest manuale. Un'attività non eseguibile dagli strumenti disponibili deve dichiarare questa dipendenza, senza fingere che l'agente possa completarla autonomamente.

## Taglie delle issue

| Stima | Uso tipico |
| --- | --- |
| 0.5 OA | Correzione circoscritta o configurazione già compresa |
| 1 OA | Piccolo cambiamento con verifica locale |
| 2 OA | Comportamento singolo con test o prova in editor |
| 4 OA | Feature piccola completa, con integrazione |
| 8 OA | Limite massimo di una issue eseguibile; dividerla se possibile |

Questi esempi sono criteri di dimensionamento, non promesse sulla velocità di un modello. Le stime iniziali sono ipotesi da calibrare. Arrotondare per eccesso alla taglia supportata, includendo il lavoro necessario a consegnare. Oltre 8 OA, creare un contenitore e sotto-issue ciascuna <= 8 OA; sommare solo le foglie per non raddoppiare il totale.

Se la fattibilità è ignota, aprire uno **spike da 1 o 2 OA** con una domanda precisa, limite di tempo e risultato atteso (decisione, prova, rischi e nuova stima). Alla scadenza registrare quanto appreso; non trasformarlo silenziosamente in una feature aperta.

## Prima di iniziare

Ogni issue `ready` contiene:

- risultato osservabile e confini esclusi;
- criteri di accettazione e metodo di verifica;
- stima totale OA, breve ripartizione, intervallo plausibile e confidenza alta/media/bassa;
- OH previste, anche 0; eventuali tempi di attesa esterni;
- responsabile, dipendenze e asset da riservare;
- una sola etichetta `effort:0.5`, `effort:1`, `effort:2`, `effort:4` o `effort:8`.

`effort:unestimated` indica triage; `effort:split` segnala scope troppo grande. Il workflow sincronizza queste etichette dalla voce **Stima (OA)** dei moduli. L'automazione non decide se una stima è realistica né imposta automaticamente `ready`.

Esempio: 4 OA = 0.5 lettura + 2 implementazione + 1 verifiche + 0.5 integrazione; intervallo 3-6 OA, confidenza media; 0.25 OH per playtest visivo; dipendenza da camera già scelta.

## Durante e dopo il lavoro

Se emergono dipendenze o si consuma la stima senza arrivare all'accettazione, registrare lavoro svolto, **OA residue** e motivo. La nuova previsione totale è `OA già consumate + OA residue`; non sovrascrivere la stima iniziale, che serve al confronto. Dividere lo scope prima di proseguire oltre 8 OA residue.

Alla chiusura annotare OA effettive (somma del tempo attivo di tutti gli agenti), OH effettive, verifica e PR. Se il tempo non è stato misurato, scrivere **non misurato**; se ricostruito, indicarlo come approssimazione e spiegare il metodo. La durata di una chat o il numero di commit non è una misura affidabile di lavoro attivo.

Dopo almeno cinque issue simili completate confrontare stima iniziale ed effettivo: `fattore = somma OA effettive / somma OA stimate`. Usarlo sulle nuove stime della stessa area e aggiornare la capacità settimanale osservata. Una capacità di 10 OA/settimana e un backlog di 30 OA suggeriscono circa tre settimane attive, prima di attese e verifiche umane. Non assumere capacità disponibili senza misurarle.

## Baseline e raffinamento progressivo

La baseline 0.2 segue la [Vision](Vision.md) aggiornata: cooperativa fino a quattro persone, mare e vento simulati, minigiochi, carriera a ogni imbarco, flotta e villa. La prima prova di prodotto è la [demo](Demo.md), preceduta dal gate tecnico della nave in rete. [Roadmap](Roadmap.md), [indice delle issue](Backlog.md) e [manifest JSON](Backlog.json) descrivono il percorso completo fino alla release.

Le issue sono foglie stimate, raccolte in sette epic. Gli epic riportano somme e checklist; non hanno un'altra stima da sommare. La issue di pianificazione #14 (4 OA stimate), il lavoro storico chiuso e le attese sono esclusi dai totali futuri. Nessuna OA effettiva viene dedotta dalla durata della chat.

L'intervallo di ciascuna foglia iniziale è una sensibilità esplicita da metà al doppio della stima, non un intervallo statistico. La somma degli estremi non è una previsione probabilistica della release. Le fasi lontane hanno confidenza bassa e richiedono raffinamento dopo i gate precedenti; anche le issue da 8 OA richiedono riesame. Prima di `ready`, sostituire gli intervalli generici con evidenze, verificare toolchain, licenze, budget dei contenuti e responsabilità. Se la previsione aggiornata supera 8 OA, dividere la foglia, mantenere la storia e ricalcolare il totale senza contare due volte il contenitore.

OA e OH sono lavoro attivo distinto. OH comprende anche il tempo dei partecipanti ai test, non solo del facilitatore; la disponibilità di persone e di almeno due PC è una dipendenza esterna. I budget OH delle fasi lontane sono iniziali: vanno raffinati con numero di partecipanti, durata e ritmo naturale della progressione.

Non è stanziato un numero inventato di ore per difetti ancora sconosciuti. Ogni difetto o iterazione di design scoperto diventa una issue atomica stimata e una dipendenza del gate; la previsione complessiva cambia. Senza benchmark di produttività, catalogo approvato e risultati degli spike, il totale del backlog non è un preventivo chiuso né una data di consegna.

Tutte le issue di sviluppo rimangono pianificate: la richiesta attuale autorizza soltanto tracciamento e documentazione. `blocked` segnala prerequisiti aperti; `triage` segnala anche scope o decisioni da raffinare. Rimuovere un blocco non autorizza automaticamente l'avvio di un task.

## Storia delle stime

La baseline 0.1 prevedeva un ciclo su nave ferma: 21 OA e 1.35 OH, inclusa la pianificazione iniziale. Non copriva il gioco attuale. Le issue #6–#11 vengono aggiornate conservandone stima originale e motivo della revisione; #4 e #5 restano storico chiuso. La baseline 0.2 non sovrascrive consuntivi e non considera svolto lavoro di gameplay.
