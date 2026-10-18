# Navi, mare e vento: riferimenti di progetto

Ricerca per la baseline del 18 ottobre 2026. Le fonti orientano la progettazione; non fissano ancora epoca, area geografica o un catalogo definitivo. Non vengono importate immagini, modelli o asset esterni con questa pianificazione.

## Navi e attrezzature

Il nome di una nave può descrivere l'armo, la funzione o una classificazione storica diversa secondo periodo e paese. Non derivare dimensioni ed equipaggio soltanto dal nome.

| Riferimento | Cosa possiamo ricavarne | Uso proposto |
| --- | --- | --- |
| [Glossario NOAA degli armi](https://repository.library.noaa.gov/view/noaa/38223/noaa_38223_DS1.pdf) e [riferimento NOAA](https://repository.library.noaa.gov/view/noaa/36050/noaa_36050_DS1.pdf) | Distinzione generale fra sloop, schooner, brig e armi misti; terminologia da ricontrollare per l'epoca scelta | Confrontare manovre, alberi e silhouette prima del catalogo |
| [Modello brigantino/sloop, circa 1740, Royal Museums Greenwich](https://www.rmg.co.uk/collections/objects/rmgc-object-66190) e [sloop, circa 1710](https://www.rmg.co.uk/collections/objects/rmgc-object-66359) | Esempi concreti e variabilità dei termini storici | Scheda di una nave demo leggibile, senza fissare implicitamente una ricostruzione |
| [Modello di nave da 60 cannoni, Rijksmuseum](https://www.rijksmuseum.nl/nl/collectie/object/Model-van-een-linieschip-van-60-stukken--acecc2f3db71b1527fbf7aab244a58aa) | Organizzazione dei ponti e attrezzature su una nave maggiore | Riferimenti spaziali per postazioni e vita di bordo; non requisito di cannoni giocabili |
| [Fluyt, Het Scheepvaartmuseum](https://www.hetscheepvaartmuseum.nl/collectie/artikelen/701/het-fluitschip-vrachtschip-van-de-17e-eeuw) | Una famiglia mercantile orientata al carico | Confrontare funzione e stivaggio con navi più manovriere |
| [La Concorde / Queen Anne's Revenge, archivio ufficiale](https://www.qaronline.org/history/ships-journey) e [ricerca storica](https://www.qaronline.org/media/35/open) | Documentazione di un caso reale e incertezze di ricostruzione; equipaggi storici potevano superare molto venti persone | Separare ispirazione, dato documentato e semplificazione di gioco |
| [Lavori di bordo, USS Constitution Museum](https://ussconstitutionmuseum.org/2016/03/31/small-jobs-big-purpose/) | Esempi di manutenzione e specializzazioni in un contesto successivo | Ispirazione dei gesti, da verificare prima di trasporli in un'altra epoca |

Proposta da decidere: una nave demo compatta, poi una media e una maggiore. Non è ancora il catalogo approvato della release. Per ogni nave serviranno scheda di armo, dimensioni giocabili, percorso dell'equipaggio, massa/carico, manovre e budget artistico. Venti NPC sulla nave maggiore è un limite deliberato di design; le mansioni storicamente distribuite fra molti marinai saranno sintetizzate.

## Simulazione sostenibile

[La presentazione tecnica di Rare a SIGGRAPH](https://history.siggraph.org/wp-content/uploads/2022/09/2018-Talks-Ang_The-Technical-Art-of-Sea-of-Thieves.pdf) descrive l'uso di un oceano FFT e tecniche locali per l'acqua sulle navi. È un riferimento per separare scale del problema, non un sistema trasferibile automaticamente nel progetto.

La documentazione Epic distingue [onde Water/Gerstner](https://dev.epicgames.com/documentation/en-us/unreal-engine/simulating-waves-using-the-water-waves-asset-in-unreal-engine), [galleggiamento a punti](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-buoyancy-component-in-unreal-engine) e [simulazioni fluide locali](https://dev.epicgames.com/documentation/unreal-engine/fluid-simulation-in-unreal-engine---overview). Lo spike confronterà questi percorsi con eventuali alternative FFT: query della superficie sul server, costo, licenza, supporto nella versione 5.8.3 e coerenza grafica/fisica. L'esistenza di un componente non dimostra qualità, scalabilità o replica corrette nel nostro gioco.

[Fisica in rete](https://dev.epicgames.com/documentation/en-us/unreal-engine/networked-physics-overview) e [Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine) vanno valutati insieme: nave fisica e personaggi sul ponte mobile costituiscono un rischio iniziale. Non si assume determinismo di Chaos fra client né replica automatica corretta di tutta la simulazione.

## Vento e andature

[RYA sulle andature](https://www.rya.org.uk/training/do-you-know-your-points-of-sail/) e [US Sailing sul vento apparente](https://www.ussailing.org/wp-content/uploads/2018/01/Speed-Guide-Explanation.pdf) sostengono la distinzione fra vento reale e apparente e l'impossibilità di procedere direttamente controvento. Angoli e prestazioni dipendono dal rig; non copiare una polare moderna su tutte le navi storiche.

[NOAA sulle osservazioni delle onde](https://www.ndbc.noaa.gov/waveobs.shtml) distingue componenti di mare da vento e mare lungo: cambiare il vento locale non deve far ruotare istantaneamente tutto l'oceano. Per la demo useremo scenari limitati e riproducibili, non una simulazione meteorologica globale.

## Provenienza e diritti

Citare una fonte non autorizza il riuso dei suoi media. Prima di importare qualsiasi risorsa registrare origine, autore, licenza e restrizioni in [AssetRegister](../AssetRegister.md), verificando separatamente repository pubblico e distribuzione della build. Plugin, marketplace e cambi di engine richiedono un task esplicito.
