# Demo cooperativa: il primo imbarco

Baseline 0.2, 18 ottobre 2026. Obiettivo: ottenere una prova realmente giocabile che permetta di decidere se cooperare, lavorare e viaggiare su questa nave è comprensibile e interessante. Questo documento specifica lavoro futuro; oggi il progetto contiene ancora il solo blockout iniziale.

## Perimetro minimo

La piattaforma di verifica proposta è Windows, con una sessione privata da due a quattro giocatori in terza persona. Una nave low poly percorribile comprende ponte, cucina e stiva. La rotta collega un porto e un punto di consegna/rientro; non richiede un mondo aperto. Un capitano NPC conduce la rotta: serve a rendere provabili i ruoli iniziali senza concedere subito il ruolo di capitano ai nuovi personaggi.

Ipotesi di sessione: 20–30 minuti, pochi aiutanti NPC e valori modificabili. Si imbarcano personaggi nuovi come mozzi o cuochi; anche ruoli uguali devono trovare lavoro utile. Il totale NPC della demo resta molto inferiore al limite finale di venti.

| Momento | Azione giocabile | Cosa vogliamo imparare |
| --- | --- | --- |
| Imbarco | Scegliere mozzo/cuoco, capire incarico e postazione | Si comprende come iniziare senza spiegazione costante? |
| Preparazione | Pulire, preparare un pasto, ordinare e fissare poche casse | I gesti sono diversi, leggibili e permettono aiuto? |
| Traversata | Continuare i lavori mentre nave, onde e vento cambiano | La nave è un luogo vivo o ostacola soltanto i controlli? |
| Evento moderato | Variazione controllata del mare/vento e lavoro da redistribuire | Nasce comunicazione utile senza attese o caos arbitrario? |
| Rientro | Concludere il viaggio, vedere ricompense e XP personali | Il risultato è comprensibile e invita a un nuovo imbarco? |
| Nuova sessione | Ricaricare il profilo e scegliere nuovamente un ruolo iniziale | L'esperienza persiste senza duplicazioni o perdita di identità? |

La demo mostra la direzione della carriera, ma non implementa ancora tutti gli sblocchi. La manovra delle vele per i giocatori viene estesa in M2; nella demo il capitano NPC può gestirla. Il modello fisico deve comunque reagire alle vele, al vento apparente, al timone e alla distribuzione del carico.

## Ordine di consegna

M0 verifica sessione, personaggi, nave, mare, vento, ponte mobile e interazioni autorevoli. M1 integra i tre minigiochi, il viaggio, il profilo e i salvataggi, produce il pacchetto e conduce il playtest. Il gate M0 abilita la costruzione della demo; il gate M1 abilita l'espansione del gioco. [Issue e dipendenze](Backlog.md).

## Accettazione tecnica

- Il percorso completo funziona nell'eseguibile Windows fuori dall'editor, con versione e commit identificabili, dati puliti e successivo riavvio.
- Due e quattro processi di gioco, su almeno due PC reali, completano il percorso; la connessione esterna segue il percorso scelto nello spike architetturale. Quattro finestre sullo stesso PC non esauriscono la verifica.
- Un test ripetibile con 80 ms RTT e 1% di perdita simulata non produce blocchi, oggetti/ricompense duplicati o perdita di progressi. Sono condizioni iniziali di prova, non garanzia per ogni rete.
- Ingresso tardivo, conflitto sulla postazione, abbandono, riconnessione e perdita dell'host hanno comportamenti espliciti. La migrazione automatica dell'host non è implicita.
- Personaggi e oggetti restano coerenti sulla nave in movimento; acqua e interni, onde visibili e query fisiche rispettano le tolleranze definite dallo spike mare.
- Frame time, picchi, memoria e rete sono registrati sulle macchine concordate. Target iniziale proposto: 60 fps a 1080p; hardware, preset e soglie di accettazione vanno fissati prima dei benchmark. Un risultato sotto target richiede una decisione documentata, non un cambiamento silenzioso della soglia.
- Nessun difetto P0/P1 rimane aperto sul percorso. Difetti scoperti hanno issue proprie, stima e dipendenza bloccante dal gate.

## Accettazione dell'esperienza

Due gruppi distinti, uno da due e uno da tre/quattro persone, provano la build secondo [PlaytestPlan](PlaytestPlan.md). Si osservano comprensione, utilità di entrambi i ruoli, coordinamento, tempi morti, comfort e ripetitività. I segnali iniziali proposti sono: completamento senza guida continua, nessun ruolo sistematicamente inattivo, almeno due terzi dei partecipanti disponibili a un altro viaggio e mediana di piacere della collaborazione almeno 4/5.

Queste soglie sono ipotesi da fissare prima del test; con un campione piccolo indicano problemi e direzioni, non validazione statistica del mercato. Il giudizio dei giocatori non può essere sostituito da test automatici o dall'agente.

## Decisione dopo il playtest

**GO:** criteri tecnici soddisfatti, segnali umani sufficienti e responsabile concorde: raffinare la carriera. **ITERATE:** il nucleo è leggibile ma presenta problemi circoscritti: stimare correzioni, collegarle al gate e riprovare. **REWORK:** il ciclo non sostiene collaborazione o desiderio di continuare: rivedere il design prima di ampliare contenuti.

La decisione riporta build, evidenze, scostamenti e motivazioni. Il gate resta aperto durante le correzioni; chiudere una sessione di test non equivale ad approvare la demo.
