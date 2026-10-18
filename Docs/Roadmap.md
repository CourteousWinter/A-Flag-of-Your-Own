# Roadmap iniziale

Versione 0.1, 18 ottobre 2026. Questo documento traduce il concept disponibile in un primo percorso di sviluppo. La descrizione dettagliata del gioco deve ancora essere raccolta: le fasi dopo l'MVP sono direzioni da affinare, con contenuti e sistemi da confermare.

## Cosa abbiamo capito

Il giocatore costruisce una vita in mare: parte da mozzo o marinaio, lavora e vive a bordo, guadagna denaro e reputazione, diventa capitano e può arrivare a possedere una flotta e una villa su un'isola dalla quale dirigere le spedizioni. La quotidianità, la ciurma, i rapporti e i luoghi in cui vivere collegano questa progressione.

La crescita deve rendere visibile il passaggio dal servizio agli altri all'indipendenza: ogni avanzamento introduce decisioni e responsabilità. Tempi, requisiti e regole di sblocco restano da progettare.

**Decisione confermata dall'utente il 18 ottobre 2026: visuale in terza persona per il primo prototipo.** Sensibilità, distanze della camera, animazioni e controlli specifici saranno verificati nel prototipo.

Sono ancora aperti ambientazione e grado di fantasia, ruolo del combattimento e della navigazione, eventuali carriere alternative, ambizioni multiplayer e contenuto del primo lavoro da mozzo. Non considerare questi elementi requisiti approvati.

## M0 - Primo ciclo da mozzo (MVP)

[Milestone GitHub](https://github.com/CourteousWinter/A-Flag-of-Your-Own/milestone/1)

Risultato da provare: su una sola nave ferma, il giocatore si muove in terza persona, accetta un incarico, lo completa, riceve paga e reputazione e ritrova il progresso dopo il riavvio. Un eseguibile Windows permette di provare il ciclo fuori dall'editor.

Questa è la prima ipotesi di esperienza giocabile, da validare con il design dettagliato e i playtest. Le forme del blockout e gli eventuali valori economici sono provvisori. Navigazione, combattimento, flotta, villa, economia estesa e simulazione sociale completa vengono raffinati nelle fasi successive.

| Issue | Risultato | OA iniziali | Confidenza | OH | Dipendenze |
| --- | --- | --- | --- | --- | --- |
| [#4](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/4) | Roadmap e decisioni esplicite | 1 | Alta | 0 | Nessuna |
| [#5](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/5) | Verifica ripetibile in Unreal | 2 | Media | 0 | Nessuna tecnica |
| [#6](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/6) | Movimento e camera in terza persona | 4 | Bassa | 0.25 | #5; affinamento controlli |
| [#7](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/7) | Interazione con un oggetto | 2 | Media | 0.1 | #6 |
| [#8](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/8) | Primo incarico completo | 4 | Bassa | 0.25 | #7; scelta del lavoro |
| [#9](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/9) | Paga, reputazione e feedback minimo | 2 | Media | 0.15 | #8 |
| [#10](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/10) | Salvataggio e caricamento | 4 | Bassa | 0.1 | #8, #9 |
| [#11](https://github.com/CourteousWinter/A-Flag-of-Your-Own/issues/11) | Packaging e playtest Windows | 2 | Bassa | 0.5 | #6-#10 |

Stima iniziale del backlog: **21 OA e 1.35 OH**, delle quali 1 OA riguarda la pianificazione. Ogni issue contiene ripartizione e intervallo plausibile. Sono ipotesi, senza misure di velocità precedenti: il totale non è una scadenza e va aggiornato al raffinamento. Le attese non supervisionate e le correzioni scoperte durante i playtest vanno registrate separatamente. [Metodo di stima](Planning.md).

Le issue future partono in triage; diventano `ready` con specifiche, responsabilità, dipendenze risolte e verifica definita. Si lavora su una issue alla volta per responsabile. Chiudere un task tecnico non equivale a validare il divertimento della milestone.

### Uscita dall'MVP

- Il ciclo completo è riproducibile in una build Windows, con nuovo profilo e riavvio.
- Le ricompense non si duplicano ripetendo l'interazione o ricaricando lo stato.
- Il salvataggio assente o illeggibile ha un comportamento gestito e documentato.
- Il playtest umano chiarisce se obiettivo, azione e ricompensa sono comprensibili e se il lavoro è interessante.
- Ogni difetto bloccante è risolto; le modifiche di design emerse sono registrate prima di ampliare il gioco.

## Incrementi verso il gioco completo

Le fasi descrivono risultati giocabili da esplorare dopo M0; ordine e scope saranno rivisti con la descrizione completa e le evidenze dei test. Le stime di implementazione vengono assegnate alle issue piccole quando il relativo scope è abbastanza chiaro.

| Fase proposta | Incremento giocabile | Domanda da validare prima di espandere |
| --- | --- | --- |
| M1 - Vita a bordo | Più attività significative e primi rapporti con la ciurma collegati al ciclo quotidiano | Vivere sulla nave resta interessante oltre il primo incarico? |
| M2 - Viaggi | Un viaggio limitato che collega lavoro, navigazione e ricompensa | Quale ruolo hanno controllo della nave, esplorazione e scelte di rotta? |
| M3 - Capitano | Gestire una nave propria, ciurma, provviste e decisioni di viaggio | Il comando introduce scelte interessanti e sostenibili da realizzare? |
| M4 - Flotta | Più navi e capitani con spedizioni coordinate | La delega amplia le decisioni del giocatore senza moltiplicare inutilmente il lavoro ripetitivo? |
| M5 - Vita sull'isola | Residenza e gestione dalla villa collegate alle attività in mare | Casa e isola rafforzano il senso di crescita e appartenenza? |
| M6 - Gioco completo | Sistemi collegati, progressione verificata, contenuti e qualità di release | L'esperienza mantiene la promessa iniziale dall'inizio alla gestione della flotta? |

Per ogni fase: specificare un piccolo risultato giocabile, risolvere le incertezze con uno spike da 1-2 OA se necessario, implementare, verificare in build, raccogliere feedback e aggiornare il backlog. Ampliare i contenuti dopo aver verificato il sistema che li sostiene. Performance, leggibilità, salvataggi e qualità del controllo vanno verificati lungo il percorso, secondo il tipo di cambiamento.

## Confini da definire con la descrizione completa

Servono soprattutto il ciclo di una sessione tipica, le azioni del mozzo, il ruolo di relazioni e bisogni, il funzionamento dei viaggi e della navigazione, l'eventuale combattimento, il passaggio al comando, la delega alla flotta e le attività sulla propria isola. Verranno aggiornati visione, milestone e issue interessate; eventuali cambiamenti non rendono definitive le ipotesi di questo documento.
