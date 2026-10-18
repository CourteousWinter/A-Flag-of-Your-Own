# Sviluppo di A Flag of Your Own

## Flusso quotidiano

1. Scegli una issue piccola e verificabile. Prima di iniziare, assegna un responsabile, criteri di accettazione, dipendenze e stima secondo [Planning](Docs/Planning.md).
2. Aggiorna `main` con `git pull --ff-only`, poi crea `codex/<numero>-<argomento>`. Mantieni un solo task attivo per responsabile; un blocco va dichiarato nella issue.
3. Indica nella issue gli asset binari che modificherai. Per lo stesso asset lavora un solo responsabile alla volta, anche quando più agenti usano lo stesso account GitHub.
4. Crea una PR anche lavorando da solo. Collega la issue con `Closes #numero`, descrivi il comportamento ottenuto e allega evidenze per modifiche visibili o Blueprint.
5. Esegui i controlli pertinenti, risolvi le conversazioni, ricontrolla il diff e integra con squash. Il branch viene eliminato automaticamente dopo il merge.
6. Chiudi la issue solo dopo i criteri di accettazione; registra OA effettive misurate e controlli umani. Rilascia piccoli incrementi giocabili.

Sono sufficienti `main` e branch brevi. Usa milestone per risultati giocabili; evita un branch `develop` permanente. Un'eventuale checklist di release resta separata dalle issue già consegnate.

## Da solo e in piccolo team

Le regole di `main` richiedono PR, cronologia lineare, conversazioni risolte e `Repository checks` aggiornato sulla base. Force push e cancellazione di `main` sono vietati, senza esenzioni ordinarie. Le approvazioni obbligatorie sono **0**, così l'autore può integrare dopo autocontrollo e CI. Quando una seconda persona collabora stabilmente, portare `required_approving_review_count` a **1** nel ruleset e su GitHub; non richiedere approvazioni che nessuno può fornire.

Il proprietario mantiene le impostazioni amministrative per recuperare una configurazione guasta: una modifica d'emergenza alle regole va motivata in una issue e ripristinata appena possibile. Non usare l'auto-approvazione di un bot come revisione umana.

Priorità: `priority:P0` blocca apertura/build o causa perdita di dati; `P1` serve alla milestone corrente; `P2` è normale; `P3` è un miglioramento rinviabile. Gli stati sono `status:triage`, `ready`, `in-progress`, `blocked`, `review`; mantenere un solo stato alla volta. Una issue è `ready` soltanto con scope, accettazione, responsabile, dipendenze risolte e una sola stima OA valida.

## Unreal e asset

- Configurazione condivisa in `Config/Default*.ini`; mai `Saved`, `Intermediate`, `DerivedDataCache` o `Binaries`. Conservare in `Build/` eventuali icone e risorse di packaging originali.
- Nessun merge testuale di `.uasset` e `.umap`. Rinominare nell'editor, correggere redirector e controllare i riferimenti. Separare mappe o asset solo quando aiuta il lavoro concreto.
- Prima di importare asset esterni, registrare origine e licenza in [Asset register](Docs/AssetRegister.md). Non pubblicare contenuto di terzi quando la licenza non consente la redistribuzione nel repository pubblico.
- Aggiornamenti dell'engine e dei plugin sono PR dedicate con verifica di apertura e build Windows. Nessun cambio di versione insieme a una feature.
- Non commettere `.env`, credenziali, build distribuite o dati personali. Git LFS non sostituisce un backup: mantenere una copia esterna periodica del progetto e dei sorgenti artistici.

Con identità GitHub distinte, prima di modificare un asset condiviso:

```shell
git lfs pull
git lfs locks
git lfs lock Content/AFlagOfYourOwn/Maps/L_PrototypeHarbor.umap
# Modificare, salvare, pubblicare la PR; attendere il merge.
git lfs unlock Content/AFlagOfYourOwn/Maps/L_PrototypeHarbor.umap
```

Verificare localmente i lock in pre-push con `git config --local lfs.https://github.com/CourteousWinter/A-Flag-of-Your-Own.git/info/lfs.locksverify true`. I lock non distinguono due agenti sullo stesso account e non sostituiscono il coordinamento nella issue. Non impostiamo `lockable` globale: renderebbe gli asset non bloccati in sola lettura anche nel flusso solitario.

## Verifica e consegna

`python Tools/CI/check_repository.py` controlla descrittore, sorgenti Python, cache versionate, attributi e puntatori LFS nell'indice Git. Il job GitHub scarica anche gli oggetti LFS e ne verifica l'integrità. Non installa Unreal sui runner pubblici e non esegue un build del gioco.

Per gameplay: compilare i Blueprint interessati, aprire la mappa, riprodurre i criteri in Play e controllare i log. Per salvataggi: provare nuovo profilo, riavvio e file assente/corrotto secondo lo scope della issue. Per UI: screenshot e risoluzioni previste. Prima di una milestone giocabile: packaging Windows Development e prova dell'eseguibile fuori dall'editor su dati puliti. Registrare versione engine, commit, passi ed esito nella PR.

Per release usare tag annotati `v0.x.y` e note con cambiamenti, problemi noti e commit. I tag `v*` sono protetti contro riscrittura e cancellazione. Allegare build soltanto dopo il controllo dei diritti degli asset e il playtest.

## Configurazione GitHub versionata

`.github/repository-settings.json`, `.github/labels.json` e `.github/rulesets/` descrivono le impostazioni desiderate. Sono documenti di configurazione: GitHub non li applica automaticamente. Le modifiche future vanno applicate anche nelle impostazioni/API e verificate dopo il merge. I workflow hanno permessi minimi e azioni fissate a commit; Dependabot propone gli aggiornamenti mensili.

Riferimenti: [regole GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets), [sicurezza Actions](https://docs.github.com/en/actions/reference/security/secure-use), [Git LFS e lock](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-config.adoc).
