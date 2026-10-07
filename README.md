# AION 2 Timers (Android)

Widget d'écran d'accueil + app au style Santé d'Apple listant les prochains boss et évènements
AION 2 (serveurs EU), avec comptes à rebours en direct. Horaires alignés sur metabot.gg.

## Modifier les horaires
Tout est dans `gen.py`, tableau `RULES` (heures serveur, fuseau Europe/Berlin par défaut).

## Build automatique
Chaque push sur `main` lance `.github/workflows/build-apk.yml` :
`gen.py` régénère le projet apktool (`src/`), puis l'APK est compilé, signé et publié
dans l'onglet **Releases** du dépôt.

Prérequis : un secret `KEYSTORE_BASE64` (keystore de signature encodé en base64).
La clé n'est jamais commitée ; garde-la précieusement, elle est nécessaire pour installer
les mises à jour par-dessus l'app existante.

## Build local
`APKTOOL=apktool.jar APKSIGNER=apksigner.jar ./build.sh` (Java 17+, Python 3).
