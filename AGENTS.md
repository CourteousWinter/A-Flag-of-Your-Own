# Repository instructions

- Read `CONTRIBUTING.md` and `Docs/Planning.md` before changing the project.
- Work in this checkout. Use a short-lived `codex/<issue>-<topic>` branch, one focused issue/PR at a time. Repository bootstrap may use a descriptive branch without an issue number.
- Keep `main` playable. Merge through a PR after `Repository checks` succeeds; never force-push `main`.
- Estimate implementation issues in OA (agent-hours), including implementation, verification, review fixes and integration. Use 0.5, 1, 2, 4 or 8 OA; split larger work. Record uncertainty, dependencies and separate human playtest effort. Do not invent actual hours.
- Do not create or delegate to extra agents unless the user explicitly requests it. Claim an issue and list the files/assets you intend to edit before concurrent work.
- Do not edit the same `.uasset` or `.umap` concurrently. Coordinate ownership in the issue; use Git LFS locks when different GitHub identities collaborate. Rename assets in Unreal and fix redirectors.
- Unreal Engine is 5.8.3 (association `5.8`). Engine upgrades, marketplace dependencies and game design decisions need an explicit task. Keep game assets under `/Game/AFlagOfYourOwn`.
- Keep binary/source art in LFS and generated caches out of Git. Record external asset origin, license and redistribution restrictions before adding assets.
- Run `python Tools/CI/check_repository.py` for repository changes. For gameplay changes, compile changed Blueprints, run the relevant editor/playtest checks and report evidence. CI without Unreal does not prove gameplay or packaging works.
- Do not mark an issue complete from code generation alone. Meet its acceptance criteria, link the PR, report checks and actual OA if measured. Note unperformed human checks plainly.
