#!/bin/sh
# Reconstruit l'APK : python3 gen.py -> apktool b -> apksigner
# Outils : apktool.jar et apksigner.jar (npm @postar/apktool-node), Java 17+.
set -e
APKTOOL=${APKTOOL:-apktool.jar}; APKSIGNER=${APKSIGNER:-apksigner.jar}
mkdir -p build
python3 gen.py src
java -jar "$APKTOOL" b src -o build/unsigned.apk
java -jar "$APKSIGNER" sign --ks keystore/aion2.jks --ks-pass pass:aion2timers \
  --ks-key-alias aion2 --key-pass pass:aion2timers --out build/AION2-Timers.apk build/unsigned.apk
