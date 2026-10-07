# AION 2 Timers (Android)

Android home-screen widget and companion app that track upcoming **AION 2** bosses and
recurring events on the European servers, with live countdowns.

The app is available in **English** and **French**: it follows the phone's language
(French on French-language devices, English everywhere else).

## Features

- **Home-screen widget**: the next 8 events sorted by start time, with a live countdown,
  a colour dot per category and an "ongoing" state while an event is running.
- **App**: one card per event (category, local time, countdown, progress ring),
  tabs to filter by Events, Bosses and PvP, light and dark themes.
- **Server time zone switch**: Europe/Berlin (default) or Asia/Tokyo, applied to both
  the app and the widget.

## Tracked schedule (server time)

| Event | When |
|---|---|
| Shugo Festival | every hour at :00 |
| Dimensional Invasion | every hour at :30 |
| Spacetime Rift | every 3 h from 02:00 |
| Watcher Kaira (Lv. 65) | every 3 h from 01:00 |
| Artifact Siege | Mon / Thu / Sat 21:00 |
| Executors Argo, Kaira, Tamasa (Lv. 65) | Mon / Thu / Sat 21:30 |
| Guardian Lord Nahma (Lv. 65) | Fri / Sun 21:00 |
| Lv. 80 bosses: Dramos, Marakha, Ducal | Mon / Thu / Sat 21:30 |
| Enraged Nahma (Lv. 80) | Fri / Sun 21:00 |
| Arena of Tactics (10v10) | daily 11:00–14:00 and 19:00–21:00 |
| Daily / weekly reset | 16:00 daily / Wednesday 16:00 |

Times match [metabot.gg](https://metabot.gg/en/aion-2/events), which reads them from the
global game client. NCSOFT does not publish an official schedule, and the EU server time
zone is not officially confirmed.

## Install

Download `AION2-Timers.apk` from the latest [release](../../releases), open it on your
phone and allow installation from that source. Then long-press the home screen →
Widgets → AION 2 Timers.

## Editing the schedule

Everything lives in `gen.py`: the `RULES` table (server times), the English names
(`NAMES_EN`) and the French and English UI strings (`STR_EN`, `STR_FR`).

## Automatic builds

Every push to `main` runs `.github/workflows/build-apk.yml`: `gen.py` regenerates the
apktool project (`src/`), then the APK is built, signed and published under **Releases**.

Requirement: a `KEYSTORE_BASE64` repository secret (the signing keystore, base64-encoded).
The key is never committed. Keep it safe: the same key is needed to install updates over
an existing install.

## Local build

```sh
APKTOOL=apktool.jar APKSIGNER=apksigner.jar ./build.sh
```

Requires Java 17+ and Python 3. `apktool.jar` and `apksigner.jar` come from the
`@postar/apktool-node` npm package.
