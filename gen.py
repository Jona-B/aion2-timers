#!/usr/bin/env python3
"""Génère le projet apktool (manifest, ressources, smali) de l'app AION 2 Timers."""
import os, shutil, sys

OUT = sys.argv[1]
PKG = "app.aion2.timers"
P = "Lapp/aion2/timers"

# name, cat, dayMask (bit = Calendar.DAY_OF_WEEK, dim=1..sam=7), startMin, step, count, durMin, utc
RULES = [
    ("Festival des Shugos",              0, 254,    0,  60, 24,   8, 0),
    ("Invasion dimensionnelle",          0, 254,   30,  60, 24,  13, 0),
    ("Faille spatio-temporelle",         1, 254,  120, 180,  8,  10, 0),
    ("Kaira la veilleuse",               2, 254,   60, 180,  8,  10, 0),
    ("Siège des artefacts",              3, 164, 1260,   1,  1,  30, 0),
    ("Exécuteurs Argo · Kaira · Tamasa", 2, 164, 1290,   1,  1,  15, 0),
    ("Seigneur gardien Nahma",           2,  66, 1260,   1,  1,  15, 0),
    ("Arène 10v10 (midi)",               3, 254,  660,   1,  1, 180, 0),
    ("Arène 10v10 (soir)",               3, 254, 1140,   1,  1, 120, 0),
    ("Reset quotidien",                  4, 254,  960,   1,  1,   0, 0),
    ("Reset hebdomadaire",               4,  16,  960,   1,  1,   0, 0),
    ("Boss niv. 80 : Dramos · Marakha · Ducal", 2, 164, 1290, 1, 1, 15, 0),
    ("Nahma enragé (niv. 80)",           2,  66, 1260,   1,  1,  15, 0),
]
N = len(RULES)
COLORS = [0xFF007AFF, 0xFFAF52DE, 0xFFFF2D55, 0xFFFF9500, 0xFF30B0C7]
ROWS = 7  # 1 hero + 6 list rows


def sesc(s):
    out = []
    for ch in s:
        if ch == '"': out.append('\\"')
        elif ch == '\\': out.append('\\\\')
        elif ch == '\n': out.append('\\n')
        elif ord(ch) > 126: out.append('\\u%04x' % ord(ch))
        else: out.append(ch)
    return '"' + ''.join(out) + '"'


def w(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)


if os.path.exists(OUT):
    shutil.rmtree(OUT)

# ---------------------------------------------------------------- apktool.yml
w('apktool.yml', """!!brut.androlib.apk.ApkInfo
version: 2.9.3
apkFileName: aion2-timers.apk
isFrameworkApk: false
usesFramework:
  ids:
  - 1
  tag: null
sdkInfo:
  minSdkVersion: 24
  targetSdkVersion: 34
packageInfo:
  forcedPackageId: 127
  renameManifestPackage: null
versionInfo:
  versionCode: 6
  versionName: 1.4
resourcesAreCompressed: false
sharedLibrary: false
sparseResources: false
doNotCompress:
- resources.arsc
""")

# ---------------------------------------------------------------- manifest
w('AndroidManifest.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="{PKG}">
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" android:maxSdkVersion="32"/>
    <uses-permission android:name="android.permission.USE_EXACT_ALARM"/>
    <application android:label="@string/app_name" android:icon="@mipmap/ic_launcher"
        android:allowBackup="true" android:theme="@style/AppTheme">
        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <receiver android:name=".TimerWidget" android:exported="true" android:label="@string/widget_label">
            <intent-filter>
                <action android:name="android.appwidget.action.APPWIDGET_UPDATE"/>
                <action android:name="android.intent.action.TIME_SET"/>
                <action android:name="android.intent.action.TIMEZONE_CHANGED"/>
            </intent-filter>
            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info"/>
        </receiver>
    </application>
</manifest>
""")

# ---------------------------------------------------------------- resources (EN default, FR override)
NAMES_EN = ['Shugo Festival', 'Dimensional Invasion', 'Spacetime Rift', 'Watcher Kaira', 'Artifact Siege', 'Executors Argo · Kaira · Tamasa', 'Guardian Lord Nahma', 'Arena of Tactics (midday)', 'Arena of Tactics (evening)', 'Daily reset', 'Weekly reset', 'Lv. 80 bosses: Dramos · Marakha · Ducal', 'Enraged Nahma (Lv. 80)']

def xesc(t):
    return t.replace('&', '&amp;').replace("'", "\\'").replace('<', '&lt;')

STR_EN = dict(
    app_name="AION 2 Timers",
    widget_label="AION 2 · Bosses & Events",
    widget_desc="Upcoming AION 2 bosses and events with live countdowns",
    up_next="Up next",
    ongoing="live",
    after_that="AFTER THAT",
    today_at="Today at ",
    ongoing_until="Live · ends at ",
    preview_hero_when="Today at 22:00",
    cap_live="remaining · live",
    cap_until="until start",
    server_prefix="Server: ",
    unit_d="d", unit_h="h", unit_min="min",
    tab_0="Summary", tab_1="Events", tab_2="Bosses", tab_3="PvP",
    cat_0="Event", cat_1="Rift", cat_2="Boss", cat_3="PvP", cat_4="Reset",
    howto="To add the widget: long-press your home screen → Widgets → AION 2 Timers.",
    tz_note="The EU server time zone is not officially confirmed. Check in game: if Watcher Kaira spawns at 22:00 Paris time, keep Europe/Berlin. If she spawns at 21:00 or 00:00, switch to Asia/Tokyo with the link above. Resets happen at 16:00 server time, as on metabot.gg.",
    sources="Data: AION 2 global client (metabot.gg, aion2hub.com). NCSOFT publishes no official schedule.",
)
STR_FR = dict(
    widget_label="AION 2 · Boss & Évènements",
    widget_desc="Prochains boss et évènements d'AION 2 avec compte à rebours",
    up_next="À suivre",
    ongoing="en cours",
    after_that="ENSUITE",
    today_at="Aujourd'hui à ",
    ongoing_until="En cours · fin à ",
    preview_hero_when="Aujourd'hui à 22:00",
    cap_live="restantes · en cours",
    cap_until="avant le début",
    server_prefix="Serveur : ",
    unit_d="j", unit_h="h", unit_min="min",
    tab_0="Résumé", tab_1="Évènements", tab_2="Boss", tab_3="PvP",
    cat_0="Évènement", cat_1="Faille", cat_2="Boss", cat_3="PvP", cat_4="Reset",
    howto="Pour ajouter le widget : appui long sur l'écran d'accueil → Widgets → AION 2 Timers.",
    tz_note="Le fuseau du serveur EU n'est pas confirmé officiellement. Vérifie en jeu : si Kaira la veilleuse apparaît à 22:00 (heure de Paris), garde Europe/Berlin. Si elle apparaît à 21:00 ou 00:00, passe sur Asia/Tokyo avec le lien ci-dessus. Les resets sont à 16:00 heure serveur, comme sur metabot.gg.",
    sources="Données : client global AION 2 (metabot.gg, aion2hub.com). Pas de planning officiel NCSOFT.",
)
for i, r in enumerate(RULES):
    STR_EN['rule_%d' % i] = NAMES_EN[i]
    STR_FR['rule_%d' % i] = r[0]

def strings_xml(d):
    body = '\n'.join('    <string name="%s">%s</string>' % (k, xesc(v)) for k, v in d.items())
    return '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n' + body + '\n</resources>\n'

w('res/values/strings.xml', strings_xml(STR_EN))
w('res/values-fr/strings.xml', strings_xml(STR_FR))

w('res/values/colors.xml', """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="icon_bg">#FF1E1A33</color>
</resources>
""")

w('res/drawable/widget_bg.xml', """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <solid android:color="#EB16171D"/>
    <corners android:radius="20dp"/>
    <stroke android:width="1dp" android:color="#33FFFFFF"/>
</shape>
""")

w('res/drawable/btn_bg.xml', """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <solid android:color="#FF2A2540"/>
    <corners android:radius="12dp"/>
    <stroke android:width="1dp" android:color="#FF9B7FD4"/>
</shape>
""")

ICON_PATHS = """
    <path android:strokeColor="#FFE8C46A" android:strokeWidth="4"
        android:pathData="M54,30 A24,24 0 1,1 53.99,30 Z"/>
    <path android:strokeColor="#FFE8C46A" android:strokeWidth="4" android:strokeLineCap="round"
        android:pathData="M54,40 L54,55 L64,61"/>
    <path android:fillColor="#FF9B7FD4"
        android:pathData="M30,52 C22,46 16,40 14,30 C22,34 28,38 32,44 Z"/>
    <path android:fillColor="#FF9B7FD4"
        android:pathData="M78,52 C86,46 92,40 94,30 C86,34 80,38 76,44 Z"/>
"""
w('res/drawable/ic_fg.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108">{ICON_PATHS}</vector>
""")
w('res/mipmap-anydpi/ic_launcher.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="48dp" android:height="48dp" android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FF1E1A33" android:pathData="M54,2 A52,52 0 1,1 53.99,2 Z"/>{ICON_PATHS}</vector>
""")
w('res/mipmap-anydpi-v26/ic_launcher.xml', """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/icon_bg"/>
    <foreground android:drawable="@drawable/ic_fg"/>
</adaptive-icon>
""")

w('res/xml/widget_info.xml', """<?xml version="1.0" encoding="utf-8"?>
<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"
    android:minWidth="250dp" android:minHeight="180dp"
    android:minResizeWidth="180dp" android:minResizeHeight="90dp"
    android:targetCellWidth="4" android:targetCellHeight="3"
    android:updatePeriodMillis="1800000"
    android:initialLayout="@layout/widget"
    android:previewLayout="@layout/widget"
    android:resizeMode="horizontal|vertical"
    android:widgetCategory="home_screen"
    android:description="@string/widget_desc"/>
""")

# ---------------------------------------------------------------- widget (hero + "after that" list)
# placeholders so the picker preview looks real: (name, when, category)
PREVIEW = [("@string/rule_3", "@string/preview_hero_when", 2), ("@string/rule_1", "22:30", 0),
           ("@string/rule_2", "23:00", 1), ("@string/rule_7", "11:00", 3),
           ("@string/rule_9", "16:00", 4), ("@string/rule_8", "19:00", 3),
           ("@string/rule_4", "21:00", 3)]

w('res/drawable/widget_card.xml', """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <solid android:color="@color/card"/>
    <corners android:radius="22dp"/>
</shape>
""")
w('res/drawable-v31/widget_card.xml', """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <solid android:color="@color/card"/>
    <corners android:radius="@android:dimen/system_app_widget_background_radius"/>
</shape>
""")

hero_name, hero_when, hero_cat = PREVIEW[0]
rows = []
for k in range(1, ROWS):
    name, when, cat = PREVIEW[k]
    col = '#%08X' % COLORS[cat]
    rows.append(f"""
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
        android:orientation="horizontal" android:gravity="center_vertical" android:paddingTop="5dp">
        <TextView android:id="@+id/d{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
            android:text="●" android:textSize="9sp" android:textColor="{col}" android:paddingEnd="7dp"/>
        <TextView android:id="@+id/n{k}" android:layout_width="0dp" android:layout_weight="1"
            android:layout_height="wrap_content" android:singleLine="true" android:ellipsize="end"
            android:text="{name}" android:textColor="@color/label" android:textSize="13sp"/>
        <TextView android:id="@+id/w{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
            android:text="{when}" android:textColor="@color/secondary" android:textSize="12sp"
            android:paddingStart="6dp" android:paddingEnd="8dp" android:fontFeatureSettings="tnum"/>
        <Chronometer android:id="@+id/c{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
            android:minWidth="56dp" android:gravity="end" android:textColor="@color/label"
            android:textSize="13sp" android:fontFamily="sans-serif-medium" android:fontFeatureSettings="tnum"/>
    </LinearLayout>""")

w('res/layout/widget.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/root" android:layout_width="match_parent" android:layout_height="match_parent"
    android:orientation="vertical" android:paddingStart="16dp" android:paddingEnd="16dp"
    android:paddingTop="14dp" android:paddingBottom="12dp" android:background="@drawable/widget_card">
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
        android:orientation="horizontal">
        <LinearLayout android:layout_width="0dp" android:layout_weight="1" android:layout_height="wrap_content"
            android:orientation="vertical">
            <TextView android:id="@+id/n0" android:layout_width="match_parent" android:layout_height="wrap_content"
                android:text="{hero_name}" android:textColor="#{COLORS[hero_cat]:08X}" android:textSize="15sp"
                android:fontFamily="sans-serif-medium" android:singleLine="true" android:ellipsize="end"/>
            <TextView android:id="@+id/w0" android:layout_width="match_parent" android:layout_height="wrap_content"
                android:text="{hero_when}" android:textColor="@color/secondary" android:textSize="13sp"
                android:singleLine="true" android:ellipsize="end"/>
        </LinearLayout>
        <ImageView android:id="@+id/hi" android:layout_width="22dp" android:layout_height="22dp"
            android:layout_marginStart="8dp" android:src="@drawable/ic_boss"/>
        <TextView android:id="@+id/d0" android:layout_width="wrap_content" android:layout_height="wrap_content"
            android:visibility="gone"/>
    </LinearLayout>
    <Chronometer android:id="@+id/c0" android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:textColor="@color/label" android:textSize="38sp" android:fontFamily="sans-serif"
        android:textStyle="bold" android:fontFeatureSettings="tnum" android:includeFontPadding="false"
        android:layout_marginTop="4dp"/>
    <View android:layout_width="match_parent" android:layout_height="0.5dp" android:layout_marginTop="10dp"
        android:background="@color/separator"/>
    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="8dp"
        android:text="@string/after_that" android:textColor="@color/secondary" android:textSize="11sp"
        android:letterSpacing="0.06" android:fontFamily="sans-serif-medium"/>{''.join(rows)}
</LinearLayout>
""")

# ---------------------------------------------------------------- smali: Schedule
def int_array(field, values):
    data = '\n'.join('        0x%x' % (v & 0xffffffff) for v in values)
    label = 'arr_' + field.lower()
    code = f"""    const/16 v0, 0x{len(values):x}
    new-array v1, v0, [I
    fill-array-data v1, :{label}
    sput-object v1, {P}/Schedule;->{field}:[I
"""
    tail = f"""    :{label}
    .array-data 4
{data}
    .end array-data
"""
    return code, tail

clinit_code = f"""    const/16 v0, 0x{N:x}
    new-array v1, v0, [Ljava/lang/String;
"""
for i, r in enumerate(RULES):
    clinit_code += f"""    const/16 v2, 0x{i:x}
    const-string v0, {sesc(r[0])}
    aput-object v0, v1, v2
"""
clinit_code += f"    sput-object v1, {P}/Schedule;->NAMES:[Ljava/lang/String;\n"
tails = ''
for idx, field in [(1, 'CAT'), (2, 'MASK'), (3, 'START'), (4, 'STEP'), (5, 'COUNT'), (6, 'DUR'), (7, 'UTC')]:
    c, t = int_array(field, [r[idx] for r in RULES])
    clinit_code += c; tails += t
c, t = int_array('COLORS', COLORS)
clinit_code += c; tails += t

fields = '\n'.join(f'.field public static {f}:[I' for f in ['CAT', 'MASK', 'START', 'STEP', 'COUNT', 'DUR', 'UTC', 'COLORS'])

w(f'smali/app/aion2/timers/Schedule.smali', f""".class public final {P}/Schedule;
.super Ljava/lang/Object;

.field public static NAMES:[Ljava/lang/String;
{fields}

.method static constructor <clinit>()V
    .locals 3
{clinit_code}    return-void

{tails}.end method

.method public constructor <init>()V
    .locals 0
    invoke-direct {{p0}}, Ljava/lang/Object;-><init>()V
    return-void
.end method

# Start (ms) of the first occurrence of rule p0 that has not ended yet at time p1:p2.
.method public static nextStart(IJLjava/util/TimeZone;)J
    .locals 12
    sget-object v2, {P}/Schedule;->UTC:[I
    aget v2, v2, p0
    if-eqz v2, :tzok
    const-string v2, "UTC"
    invoke-static {{v2}}, Ljava/util/TimeZone;->getTimeZone(Ljava/lang/String;)Ljava/util/TimeZone;
    move-result-object p3
    :tzok
    sget-object v2, {P}/Schedule;->DUR:[I
    aget v2, v2, p0
    int-to-long v3, v2
    const-wide/32 v9, 0xea60
    mul-long/2addr v3, v9
    invoke-static {{p3}}, Ljava/util/Calendar;->getInstance(Ljava/util/TimeZone;)Ljava/util/Calendar;
    move-result-object v0
    const/4 v1, -0x1
    :dayloop
    const/16 v2, 0x8
    if-ge v1, v2, :notfound
    invoke-virtual {{v0, p1, p2}}, Ljava/util/Calendar;->setTimeInMillis(J)V
    const/4 v2, 0x5
    invoke-virtual {{v0, v2, v1}}, Ljava/util/Calendar;->add(II)V
    const/4 v2, 0x7
    invoke-virtual {{v0, v2}}, Ljava/util/Calendar;->get(I)I
    move-result v2
    sget-object v11, {P}/Schedule;->MASK:[I
    aget v11, v11, p0
    shr-int/2addr v11, v2
    and-int/lit8 v11, v11, 0x1
    if-eqz v11, :nextday
    const/4 v5, 0x0
    :slotloop
    sget-object v11, {P}/Schedule;->COUNT:[I
    aget v11, v11, p0
    if-ge v5, v11, :nextday
    sget-object v11, {P}/Schedule;->STEP:[I
    aget v11, v11, p0
    mul-int v6, v5, v11
    sget-object v11, {P}/Schedule;->START:[I
    aget v11, v11, p0
    add-int/2addr v6, v11
    div-int/lit8 v11, v6, 0x3c
    const/16 v2, 0xb
    invoke-virtual {{v0, v2, v11}}, Ljava/util/Calendar;->set(II)V
    rem-int/lit8 v11, v6, 0x3c
    const/16 v2, 0xc
    invoke-virtual {{v0, v2, v11}}, Ljava/util/Calendar;->set(II)V
    const/4 v11, 0x0
    const/16 v2, 0xd
    invoke-virtual {{v0, v2, v11}}, Ljava/util/Calendar;->set(II)V
    const/16 v2, 0xe
    invoke-virtual {{v0, v2, v11}}, Ljava/util/Calendar;->set(II)V
    invoke-virtual {{v0}}, Ljava/util/Calendar;->getTimeInMillis()J
    move-result-wide v7
    add-long v9, v7, v3
    cmp-long v11, v9, p1
    if-gtz v11, :found
    add-int/lit8 v5, v5, 0x1
    goto :slotloop
    :nextday
    add-int/lit8 v1, v1, 0x1
    goto :dayloop
    :found
    return-wide v7
    :notfound
    const-wide v7, 0x7fffffffffffffffL
    return-wide v7
.end method

.method public static computeAll(JLjava/util/TimeZone;)[J
    .locals 5
    const/16 v0, 0x{N:x}
    new-array v1, v0, [J
    const/4 v2, 0x0
    :loop
    if-ge v2, v0, :done
    invoke-static {{v2, p0, p1, p2}}, {P}/Schedule;->nextStart(IJLjava/util/TimeZone;)J
    move-result-wide v3
    aput-wide v3, v1, v2
    add-int/lit8 v2, v2, 0x1
    goto :loop
    :done
    return-object v1
.end method

# Indices sorted by ascending time (selection sort).
.method public static order([J)[I
    .locals 10
    array-length v0, p0
    new-array v1, v0, [I
    const/4 v2, 0x0
    :init
    if-ge v2, v0, :initdone
    aput v2, v1, v2
    add-int/lit8 v2, v2, 0x1
    goto :init
    :initdone
    const/4 v2, 0x0
    :outer
    if-ge v2, v0, :done
    move v3, v2
    add-int/lit8 v4, v2, 0x1
    :inner
    if-ge v4, v0, :innerdone
    aget v5, v1, v4
    aget-wide v6, p0, v5
    aget v5, v1, v3
    aget-wide v8, p0, v5
    cmp-long v5, v6, v8
    if-gez v5, :noswap
    move v3, v4
    :noswap
    add-int/lit8 v4, v4, 0x1
    goto :inner
    :innerdone
    aget v5, v1, v2
    aget v6, v1, v3
    aput v6, v1, v2
    aput v5, v1, v3
    add-int/lit8 v2, v2, 0x1
    goto :outer
    :done
    return-object v1
.end method

.method public static tzName(Landroid/content/Context;)Ljava/lang/String;
    .locals 3
    const-string v0, "aion"
    const/4 v1, 0x0
    invoke-virtual {{p0, v0, v1}}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
    move-result-object v0
    const-string v1, "tz"
    const-string v2, "Europe/Berlin"
    invoke-interface {{v0, v1, v2}}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method public static setTzName(Landroid/content/Context;Ljava/lang/String;)V
    .locals 2
    const-string v0, "aion"
    const/4 v1, 0x0
    invoke-virtual {{p0, v0, v1}}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
    move-result-object v0
    invoke-interface {{v0}}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;
    move-result-object v0
    const-string v1, "tz"
    invoke-interface {{v0, v1, p1}}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;
    move-result-object v0
    invoke-interface {{v0}}, Landroid/content/SharedPreferences$Editor;->apply()V
    return-void
.end method

.method public static serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    .locals 1
    invoke-static {{p0}}, {P}/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v0
    invoke-static {{v0}}, Ljava/util/TimeZone;->getTimeZone(Ljava/lang/String;)Ljava/util/TimeZone;
    move-result-object v0
    return-object v0
.end method

.method public static id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    .locals 2
    invoke-virtual {{p0}}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;
    move-result-object v0
    invoke-virtual {{p0}}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v1
    invoke-virtual {{v0, p1, p2, v1}}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    return v0
.end method

.method public static str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    const-string v0, "string"
    invoke-static {{p0, p1, v0}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {{p0, v0}}, Landroid/content/Context;->getString(I)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method public static strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    .locals 1
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {{v0, p1}}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {{v0, p2}}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {{v0}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {{p0, v0}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

# "42 min" or "3 h 05" for a positive duration in ms (rounded up to the minute).
.method public static rel(J)Ljava/lang/String;
    .locals 10
    const-wide/32 v0, 0xea5f
    add-long/2addr v0, p0
    const-wide/32 v2, 0xea60
    div-long/2addr v0, v2
    const-wide/16 v2, 0x3c
    cmp-long v4, v0, v2
    if-gez v4, :hours
    new-instance v4, Ljava/lang/StringBuilder;
    invoke-direct {{v4}}, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual {{v4, v0, v1}}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;
    const-string v5, " min"
    invoke-virtual {{v4, v5}}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {{v4}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v4
    return-object v4
    :hours
    div-long v4, v0, v2
    rem-long v6, v0, v2
    invoke-static {{v4, v5}}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v4
    invoke-static {{v6, v7}}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v6
    const/4 v8, 0x2
    new-array v8, v8, [Ljava/lang/Object;
    const/4 v9, 0x0
    aput-object v4, v8, v9
    const/4 v9, 0x1
    aput-object v6, v8, v9
    const-string v9, "%d h %02d"
    invoke-static {{v9, v8}}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v9
    return-object v9
.end method
""")

# ---------------------------------------------------------------- smali: TimerWidget
w('smali/app/aion2/timers/TimerWidget.smali', f""".class public {P}/TimerWidget;
.super Landroid/appwidget/AppWidgetProvider;

.field static sCtx:Landroid/content/Context;
.field static sNow:J
.field static sElapsed:J
.field static sFmt:Ljava/text/SimpleDateFormat;
.field static sStarts:[J
.field static sFmtTime:Ljava/text/SimpleDateFormat;

.method public constructor <init>()V
    .locals 0
    invoke-direct {{p0}}, Landroid/appwidget/AppWidgetProvider;-><init>()V
    return-void
.end method

.method public onUpdate(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V
    .locals 0
    invoke-static {{p1}}, {P}/TimerWidget;->update(Landroid/content/Context;)V
    return-void
.end method

.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 2
    invoke-super {{p0, p1, p2}}, Landroid/appwidget/AppWidgetProvider;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    invoke-virtual {{p2}}, Landroid/content/Intent;->getAction()Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :end
    const-string v1, "app.aion2.timers.REFRESH"
    invoke-virtual {{v1, v0}}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    const-string v1, "android.intent.action.TIME_SET"
    invoke-virtual {{v1, v0}}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    const-string v1, "android.intent.action.TIMEZONE_CHANGED"
    invoke-virtual {{v1, v0}}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    goto :end
    :doit
    invoke-static {{p1}}, {P}/TimerWidget;->update(Landroid/content/Context;)V
    :end
    return-void
.end method

.method static vid(Landroid/content/Context;Ljava/lang/String;I)I
    .locals 2
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {{v0, p1}}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {{v0, p2}}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {{v0}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    const-string v1, "id"
    invoke-static {{p0, v0, v1}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    return v0
.end method

# Fill row p1 with rule p2; returns the time (ms) the row's countdown targets.
.method static row(Landroid/widget/RemoteViews;II)J
    .locals 13
    sget-object v0, {P}/TimerWidget;->sCtx:Landroid/content/Context;
    sget-object v1, {P}/TimerWidget;->sStarts:[J
    aget-wide v2, v1, p2
    sget-wide v4, {P}/TimerWidget;->sNow:J
    sget-object v1, {P}/Schedule;->DUR:[I
    aget v1, v1, p2
    int-to-long v6, v1
    const-wide/32 v8, 0xea60
    mul-long/2addr v6, v8
    add-long/2addr v6, v2
    const-string v1, "n"
    invoke-static {{v0, v1, p1}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    const-string v1, "rule_"
    invoke-static {{v0, v1, p2}}, {P}/Schedule;->strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {{p0, v8, v1}}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    const-string v1, "d"
    invoke-static {{v0, v1, p1}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    sget-object v1, {P}/Schedule;->CAT:[I
    aget v1, v1, p2
    sget-object v9, {P}/Schedule;->COLORS:[I
    aget v1, v9, v1
    invoke-virtual {{p0, v8, v1}}, Landroid/widget/RemoteViews;->setTextColor(II)V
    cmp-long v1, v2, v4
    if-gtz v1, :future
    const-string v10, "ongoing"
    invoke-static {{v0, v10}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v10
    move-wide v11, v6
    goto :settext
    :future
    sget-object v1, {P}/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v9, Ljava/util/Date;
    invoke-direct {{v9, v2, v3}}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {{v1, v9}}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v10
    move-wide v11, v2
    :settext
    const-string v1, "w"
    invoke-static {{v0, v1, p1}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    invoke-virtual {{p0, v8, v10}}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    const-string v1, "c"
    invoke-static {{v0, v1, p1}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    sub-long v4, v11, v4
    sget-wide v6, {P}/TimerWidget;->sElapsed:J
    add-long/2addr v4, v6
    move-object v2, p0
    move v3, v8
    const/4 v6, 0x0
    const/4 v7, 0x1
    invoke-virtual/range {{v2 .. v7}}, Landroid/widget/RemoteViews;->setChronometer(IJLjava/lang/String;Z)V
    const/4 v7, 0x1
    invoke-virtual {{p0, v8, v7}}, Landroid/widget/RemoteViews;->setChronometerCountDown(IZ)V
    return-wide v11
.end method

# Hero block (row 0): colored name, category icon, "Today at 22:00" / "Live · ends at 22:08".
.method static hero(Landroid/content/Context;Landroid/widget/RemoteViews;I)V
    .locals 12
    sget-object v0, {P}/Schedule;->CAT:[I
    aget v0, v0, p2
    sget-object v1, {P}/Schedule;->COLORS:[I
    aget v1, v1, v0
    const-string v2, "n"
    const/4 v3, 0x0
    invoke-static {{p0, v2, v3}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v2
    invoke-virtual {{p1, v2, v1}}, Landroid/widget/RemoteViews;->setTextColor(II)V
    const-string v2, "hi"
    const-string v3, "id"
    invoke-static {{p0, v2, v3}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v2
    sget-object v3, {P}/MainActivity;->ICONS:[Ljava/lang/String;
    aget-object v3, v3, v0
    const-string v4, "drawable"
    invoke-static {{p0, v3, v4}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v3
    invoke-virtual {{p1, v2, v3}}, Landroid/widget/RemoteViews;->setImageViewResource(II)V
    const-string v3, "setColorFilter"
    invoke-virtual {{p1, v2, v3, v1}}, Landroid/widget/RemoteViews;->setInt(ILjava/lang/String;I)V
    sget-object v3, {P}/TimerWidget;->sStarts:[J
    aget-wide v4, v3, p2
    sget-wide v6, {P}/TimerWidget;->sNow:J
    new-instance v8, Ljava/lang/StringBuilder;
    invoke-direct {{v8}}, Ljava/lang/StringBuilder;-><init>()V
    cmp-long v3, v4, v6
    if-gtz v3, :future
    const-string v2, "ongoing_until"
    invoke-static {{p0, v2}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {{v8, v2}}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    sget-object v2, {P}/Schedule;->DUR:[I
    aget v2, v2, p2
    int-to-long v9, v2
    const-wide/32 v2, 0xea60
    mul-long/2addr v9, v2
    add-long/2addr v9, v4
    goto :time
    :future
    move-wide v9, v4
    invoke-static {{v4, v5}}, Landroid/text/format/DateUtils;->isToday(J)Z
    move-result v2
    if-eqz v2, :other
    const-string v2, "today_at"
    invoke-static {{p0, v2}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {{v8, v2}}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    goto :time
    :other
    sget-object v2, {P}/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v3, Ljava/util/Date;
    invoke-direct {{v3, v4, v5}}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {{v2, v3}}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {{v8, v2}}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    goto :settext
    :time
    sget-object v2, {P}/TimerWidget;->sFmtTime:Ljava/text/SimpleDateFormat;
    new-instance v3, Ljava/util/Date;
    invoke-direct {{v3, v9, v10}}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {{v2, v3}}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {{v8, v2}}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :settext
    invoke-virtual {{v8}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v8
    const-string v2, "w"
    const/4 v3, 0x0
    invoke-static {{p0, v2, v3}}, {P}/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v2
    invoke-virtual {{p1, v2, v8}}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    return-void
.end method

.method public static update(Landroid/content/Context;)V
    .locals 14
    sput-object p0, {P}/TimerWidget;->sCtx:Landroid/content/Context;
    invoke-static {{p0}}, Landroid/appwidget/AppWidgetManager;->getInstance(Landroid/content/Context;)Landroid/appwidget/AppWidgetManager;
    move-result-object v0
    new-instance v1, Landroid/content/ComponentName;
    const-class v2, {P}/TimerWidget;
    invoke-direct {{v1, p0, v2}}, Landroid/content/ComponentName;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    invoke-virtual {{v0, v1}}, Landroid/appwidget/AppWidgetManager;->getAppWidgetIds(Landroid/content/ComponentName;)[I
    move-result-object v1
    array-length v2, v1
    if-nez v2, :has
    return-void
    :has
    invoke-static {{}}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v2
    sput-wide v2, {P}/TimerWidget;->sNow:J
    invoke-static {{}}, Landroid/os/SystemClock;->elapsedRealtime()J
    move-result-wide v4
    sput-wide v4, {P}/TimerWidget;->sElapsed:J
    new-instance v4, Ljava/text/SimpleDateFormat;
    const-string v5, "EEE HH:mm"
    invoke-static {{}}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;
    move-result-object v6
    invoke-direct {{v4, v5, v6}}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    sput-object v4, {P}/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v4, Ljava/text/SimpleDateFormat;
    const-string v5, "HH:mm"
    invoke-direct {{v4, v5, v6}}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    sput-object v4, {P}/TimerWidget;->sFmtTime:Ljava/text/SimpleDateFormat;
    invoke-static {{p0}}, {P}/Schedule;->serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    move-result-object v4
    invoke-static {{v2, v3, v4}}, {P}/Schedule;->computeAll(JLjava/util/TimeZone;)[J
    move-result-object v5
    sput-object v5, {P}/TimerWidget;->sStarts:[J
    invoke-static {{v5}}, {P}/Schedule;->order([J)[I
    move-result-object v6
    new-instance v7, Landroid/widget/RemoteViews;
    invoke-virtual {{p0}}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v8
    const-string v9, "widget"
    const-string v10, "layout"
    invoke-static {{p0, v9, v10}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v9
    invoke-direct {{v7, v8, v9}}, Landroid/widget/RemoteViews;-><init>(Ljava/lang/String;I)V
    const-wide/32 v8, 0x1b7740
    add-long/2addr v8, v2
    const/4 v10, 0x0
    :loop
    const/16 v11, 0x{ROWS:x}
    if-ge v10, v11, :loopdone
    aget v11, v6, v10
    invoke-static {{v7, v10, v11}}, {P}/TimerWidget;->row(Landroid/widget/RemoteViews;II)J
    move-result-wide v12
    cmp-long v11, v12, v8
    if-gez v11, :nomin
    move-wide v8, v12
    :nomin
    add-int/lit8 v10, v10, 0x1
    goto :loop
    :loopdone
    const/4 v10, 0x0
    aget v10, v6, v10
    invoke-static {{p0, v7, v10}}, {P}/TimerWidget;->hero(Landroid/content/Context;Landroid/widget/RemoteViews;I)V
    new-instance v10, Landroid/content/Intent;
    const-class v11, {P}/MainActivity;
    invoke-direct {{v10, p0, v11}}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const/4 v11, 0x0
    const/high16 v12, 0xc000000
    invoke-static {{p0, v11, v10, v12}}, Landroid/app/PendingIntent;->getActivity(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;
    move-result-object v10
    const-string v11, "root"
    const-string v12, "id"
    invoke-static {{p0, v11, v12}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v11
    invoke-virtual {{v7, v11, v10}}, Landroid/widget/RemoteViews;->setOnClickPendingIntent(ILandroid/app/PendingIntent;)V
    invoke-virtual {{v0, v1, v7}}, Landroid/appwidget/AppWidgetManager;->updateAppWidget([ILandroid/widget/RemoteViews;)V
    const-wide/16 v10, 0x3e8
    add-long/2addr v8, v10
    invoke-static {{p0, v8, v9}}, {P}/TimerWidget;->schedule(Landroid/content/Context;J)V
    return-void
.end method

.method static schedule(Landroid/content/Context;J)V
    .locals 5
    const-string v0, "alarm"
    invoke-virtual {{p0, v0}}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;
    move-result-object v0
    check-cast v0, Landroid/app/AlarmManager;
    new-instance v1, Landroid/content/Intent;
    const-class v2, {P}/TimerWidget;
    invoke-direct {{v1, p0, v2}}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const-string v2, "app.aion2.timers.REFRESH"
    invoke-virtual {{v1, v2}}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;
    const/4 v2, 0x1
    const/high16 v3, 0xc000000
    invoke-static {{p0, v2, v1, v3}}, Landroid/app/PendingIntent;->getBroadcast(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;
    move-result-object v1
    const/4 v2, 0x1
    :try_start
    invoke-virtual {{v0, v2, p1, p2, v1}}, Landroid/app/AlarmManager;->setExact(IJLandroid/app/PendingIntent;)V
    :try_end
    .catch Ljava/lang/SecurityException; {{:try_start .. :try_end}} :fallback
    return-void
    :fallback
    invoke-virtual {{v0, v2, p1, p2, v1}}, Landroid/app/AlarmManager;->set(IJLandroid/app/PendingIntent;)V
    return-void
.end method
""")


# ================================================================ main screen UI
def s32(x):
    """Littéral smali signé pour une constante 32 bits."""
    x &= 0xffffffff
    if x >= 0x80000000:
        x -= 0x100000000
    return ('-0x%x' % -x) if x < 0 else ('0x%x' % x)

TITLES = ["Résumé", "Évènements", "Boss", "PvP"]
FILTERS = [-1, 0, 2, 3]
CATS = ["Évènement", "Faille", "Boss", "PvP", "Reset"]
ICONS = ["ic_event", "ic_rift", "ic_boss", "ic_pvp", "ic_reset"]
TAB_ICONS = ["ic_heart", "ic_event", "ic_boss", "ic_pvp"]
BLUE, GREY = 0xFF007AFF, 0xFF8E8E93

# ---- couleurs (clair / sombre)
w('res/values/colors.xml', """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="icon_bg">#FF1E1A33</color>
    <color name="bg">#FFF2F2F7</color>
    <color name="card">#FFFFFFFF</color>
    <color name="label">#FF000000</color>
    <color name="secondary">#FF8E8E93</color>
    <color name="tertiary">#FFC7C7CC</color>
    <color name="separator">#FFC6C6C8</color>
    <color name="tabbar">#FFF9F9F9</color>
    <color name="link">#FF007AFF</color>
</resources>
""")
w('res/values-night/colors.xml', """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="bg">#FF000000</color>
    <color name="card">#FF1C1C1E</color>
    <color name="label">#FFFFFFFF</color>
    <color name="secondary">#FF98989D</color>
    <color name="tertiary">#FF48484A</color>
    <color name="separator">#FF38383A</color>
    <color name="tabbar">#FF161618</color>
    <color name="link">#FF0A84FF</color>
</resources>
""")
w('res/values/styles.xml', """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="@android:style/Theme.DeviceDefault.Light.NoActionBar">
        <item name="android:windowBackground">@color/bg</item>
        <item name="android:statusBarColor">@color/bg</item>
        <item name="android:navigationBarColor">@color/tabbar</item>
        <item name="android:windowLightStatusBar">true</item>
        <item name="android:windowLightNavigationBar">true</item>
    </style>
</resources>
""")
w('res/values-night/styles.xml', """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="@android:style/Theme.DeviceDefault.NoActionBar">
        <item name="android:windowBackground">@color/bg</item>
        <item name="android:statusBarColor">@color/bg</item>
        <item name="android:navigationBarColor">@color/tabbar</item>
        <item name="android:windowLightStatusBar">false</item>
        <item name="android:windowLightNavigationBar">false</item>
    </style>
</resources>
""")

# ---- drawables
w('res/drawable/card_bg.xml', """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="rectangle">
    <solid android:color="@color/card"/>
    <corners android:radius="12dp"/>
</shape>
""")
w('res/drawable/ring.xml', """<?xml version="1.0" encoding="utf-8"?>
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@android:id/background">
        <shape android:shape="ring" android:innerRadius="19dp" android:thickness="9dp" android:useLevel="false">
            <solid android:color="#FFFFFFFF"/>
        </shape>
    </item>
    <item android:id="@android:id/progress">
        <rotate android:fromDegrees="270" android:toDegrees="270" android:pivotX="50%" android:pivotY="50%">
            <shape android:shape="ring" android:innerRadius="19dp" android:thickness="9dp" android:useLevel="true">
                <solid android:color="#FFFFFFFF"/>
            </shape>
        </rotate>
    </item>
</layer-list>
""")

def vec(name, body, size=24):
    w(f'res/drawable/{name}.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="{size}dp" android:height="{size}dp" android:viewportWidth="24" android:viewportHeight="24">
{body}
</vector>
""")

vec('ic_heart', '    <path android:fillColor="#FFFFFFFF" android:pathData="M12,21.35l-1.45,-1.32C5.4,15.36 2,12.28 2,8.5 2,5.42 4.42,3 7.5,3c1.74,0 3.41,0.81 4.5,2.09C13.09,3.81 14.76,3 16.5,3 19.58,3 22,5.42 22,8.5c0,3.78 -3.4,6.86 -8.55,11.54L12,21.35z"/>')
vec('ic_event', '    <path android:fillColor="#FFFFFFFF" android:pathData="M12,2l2.9,6.9L22,9.3l-5.4,4.7L18.2,21L12,17.3L5.8,21l1.6,-7L2,9.3l7.1,-0.4z"/>')
vec('ic_rift', '    <path android:fillColor="#FFFFFFFF" android:fillType="evenOdd" android:pathData="M12,2A10,10 0 1,1 12,22A10,10 0 1,1 12,2Z M12,6.5A5.5,5.5 0 1,0 12,17.5A5.5,5.5 0 1,0 12,6.5Z M12,10A2,2 0 1,1 12,14A2,2 0 1,1 12,10Z"/>')
vec('ic_boss', '    <path android:fillColor="#FFFFFFFF" android:pathData="M12,12.9l-2.13,2.09C9.31,15.55 9,16.28 9,17.06C9,18.68 10.35,20 12,20s3,-1.32 3,-2.94c0,-0.78 -0.31,-1.52 -0.87,-2.07L12,12.9z M16,6l-0.44,0.55C14.38,8.02 12,7.19 12,5.3V2c0,0 -8,4 -8,11c0,2.92 1.56,5.47 3.89,6.86C7.33,19.06 7,18.11 7,17.06c0,-1.32 0.52,-2.56 1.47,-3.5L12,10.1l3.53,3.47c0.95,0.93 1.47,2.17 1.47,3.5c0,1.02 -0.31,1.96 -0.85,2.75c1.89,-1.15 3.29,-3.06 3.71,-5.3C20.52,10.97 18.79,7.62 16,6z"/>')
vec('ic_pvp', '    <path android:strokeColor="#FFFFFFFF" android:strokeWidth="2.3" android:strokeLineCap="round" android:pathData="M4.5,4.5L15,15 M19.5,4.5L9,15 M7.5,16.5L4.5,19.5 M16.5,16.5L19.5,19.5 M7.5,13L11,16.5 M16.5,13L13,16.5"/>')
vec('ic_reset', '    <path android:fillColor="#FFFFFFFF" android:pathData="M17.65,6.35C16.2,4.9 14.21,4 12,4c-4.42,0 -7.99,3.58 -7.99,8s3.57,8 7.99,8c3.73,0 6.84,-2.55 7.73,-6h-2.08c-0.82,2.33 -3.04,4 -5.65,4 -3.31,0 -6,-2.69 -6,-6s2.69,-6 6,-6c1.66,0 3.14,0.69 4.22,1.78L13,11h7V4l-2.35,2.35z"/>')
vec('ic_chevron', '    <path android:strokeColor="@color/tertiary" android:strokeWidth="2.4" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M9,5L16,12L9,19"/>')

# ---- layout principal
def card(k):
    return f"""
            <LinearLayout android:id="@+id/card{k}" android:layout_width="match_parent" android:layout_height="wrap_content"
                android:orientation="vertical" android:background="@drawable/card_bg"
                android:paddingStart="16dp" android:paddingEnd="14dp" android:paddingTop="13dp" android:paddingBottom="14dp"
                android:layout_marginTop="10dp">
                <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
                    android:orientation="horizontal" android:gravity="center_vertical">
                    <ImageView android:id="@+id/ic{k}" android:layout_width="18dp" android:layout_height="18dp"/>
                    <TextView android:id="@+id/cl{k}" android:layout_width="0dp" android:layout_weight="1"
                        android:layout_height="wrap_content" android:layout_marginStart="6dp"
                        android:fontFamily="sans-serif-medium" android:textSize="16sp" android:singleLine="true"/>
                    <TextView android:id="@+id/tm{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                        android:textColor="@color/secondary" android:textSize="15sp" android:fontFeatureSettings="tnum"/>
                    <ImageView android:layout_width="14dp" android:layout_height="14dp" android:layout_marginStart="6dp"
                        android:src="@drawable/ic_chevron"/>
                </LinearLayout>
                <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
                    android:orientation="horizontal" android:gravity="center_vertical" android:layout_marginTop="8dp">
                    <LinearLayout android:layout_width="0dp" android:layout_weight="1" android:layout_height="wrap_content"
                        android:orientation="vertical">
                        <TextView android:id="@+id/nm{k}" android:layout_width="match_parent" android:layout_height="wrap_content"
                            android:textColor="@color/label" android:textSize="19sp" android:textStyle="bold"
                            android:fontFamily="sans-serif"/>
                        <LinearLayout android:layout_width="wrap_content" android:layout_height="wrap_content"
                            android:orientation="horizontal" android:baselineAligned="true" android:layout_marginTop="2dp">
                            <TextView android:id="@+id/vh{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                                android:textColor="@color/label" android:textSize="32sp" android:textStyle="bold"
                                android:fontFamily="sans-serif" android:fontFeatureSettings="tnum"/>
                            <TextView android:id="@+id/uh{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                                android:textColor="@color/secondary" android:textSize="17sp" android:fontFamily="sans-serif-medium"
                                android:layout_marginStart="3dp" android:layout_marginEnd="8dp"/>
                            <TextView android:id="@+id/vm{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                                android:textColor="@color/label" android:textSize="32sp" android:textStyle="bold"
                                android:fontFamily="sans-serif" android:fontFeatureSettings="tnum"/>
                            <TextView android:id="@+id/um{k}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                                android:textColor="@color/secondary" android:textSize="17sp" android:fontFamily="sans-serif-medium"
                                android:layout_marginStart="3dp"/>
                        </LinearLayout>
                        <TextView android:id="@+id/cap{k}" android:layout_width="match_parent" android:layout_height="wrap_content"
                            android:textColor="@color/secondary" android:textSize="15sp"/>
                    </LinearLayout>
                    <ProgressBar android:id="@+id/rg{k}" style="?android:attr/progressBarStyleHorizontal"
                        android:layout_width="56dp" android:layout_height="56dp" android:layout_marginStart="10dp"
                        android:indeterminate="false" android:max="1000" android:progress="0"
                        android:progressDrawable="@drawable/ring"/>
                </LinearLayout>
            </LinearLayout>"""

def tab(i):
    return f"""
        <LinearLayout android:id="@+id/tab{i}" android:layout_width="0dp" android:layout_weight="1"
            android:layout_height="wrap_content" android:orientation="vertical" android:gravity="center_horizontal"
            android:paddingTop="7dp" android:paddingBottom="6dp" android:clickable="true" android:focusable="true">
            <ImageView android:id="@+id/ti{i}" android:layout_width="26dp" android:layout_height="26dp"
                android:src="@drawable/{TAB_ICONS[i]}"/>
            <TextView android:id="@+id/tl{i}" android:layout_width="wrap_content" android:layout_height="wrap_content"
                android:layout_marginTop="2dp" android:text="@string/tab_{i}" android:textSize="10sp"
                android:fontFamily="sans-serif-medium" android:textColor="@color/secondary"/>
        </LinearLayout>"""

w('res/layout/activity_main.xml', f"""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent"
    android:orientation="vertical" android:background="@color/bg" android:fitsSystemWindows="true">
    <ScrollView android:id="@+id/scroll" android:layout_width="match_parent" android:layout_height="0dp"
        android:layout_weight="1" android:scrollbars="none">
        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
            android:orientation="vertical" android:paddingStart="16dp" android:paddingEnd="16dp" android:paddingBottom="24dp">
            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
                android:orientation="horizontal" android:gravity="center_vertical" android:paddingTop="28dp">
                <TextView android:id="@+id/title" android:layout_width="0dp" android:layout_weight="1"
                    android:layout_height="wrap_content" android:text="@string/tab_0" android:textColor="@color/label"
                    android:textSize="34sp" android:textStyle="bold" android:fontFamily="sans-serif"
                    android:letterSpacing="-0.01"/>
                <ImageView android:layout_width="38dp" android:layout_height="38dp" android:src="@mipmap/ic_launcher"/>
            </LinearLayout>
            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
                android:orientation="horizontal" android:gravity="bottom" android:paddingTop="20dp" android:paddingBottom="2dp">
                <TextView android:layout_width="0dp" android:layout_weight="1" android:layout_height="wrap_content"
                    android:text="@string/up_next" android:textColor="@color/label" android:textSize="22sp"
                    android:textStyle="bold" android:fontFamily="sans-serif"/>
                <TextView android:id="@+id/tzlink" android:layout_width="wrap_content" android:layout_height="wrap_content"
                    android:textColor="@color/link" android:textSize="17sp" android:clickable="true" android:focusable="true"
                    android:paddingStart="12dp" android:paddingTop="4dp" android:paddingBottom="4dp"/>
            </LinearLayout>{''.join(card(k) for k in range(N))}
            <TextView android:layout_width="match_parent" android:layout_height="wrap_content"
                android:layout_marginTop="22dp" android:text="@string/howto"
                android:textColor="@color/secondary" android:textSize="13sp"/>
            <TextView android:layout_width="match_parent" android:layout_height="wrap_content"
                android:layout_marginTop="10dp" android:text="@string/tz_note"
                android:textColor="@color/secondary" android:textSize="13sp"/>
            <TextView android:layout_width="match_parent" android:layout_height="wrap_content"
                android:layout_marginTop="10dp" android:text="@string/sources"
                android:textColor="@color/secondary" android:textSize="12sp"/>
        </LinearLayout>
    </ScrollView>
    <View android:layout_width="match_parent" android:layout_height="0.5dp" android:background="@color/separator"/>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content"
        android:orientation="horizontal" android:background="@color/tabbar">{''.join(tab(i) for i in range(4))}
    </LinearLayout>
</LinearLayout>
""")

# ---- smali MainActivity
A = f'{P}/MainActivity'
SB_APPEND = "Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;"

def str_array(field, values):
    s = f"    const/16 v0, 0x{len(values):x}\n    new-array v1, v0, [Ljava/lang/String;\n"
    for i, v in enumerate(values):
        s += f"    const/16 v2, 0x{i:x}\n    const-string v0, {sesc(v)}\n    aput-object v0, v1, v2\n"
    return s + f"    sput-object v1, {A};->{field}:[Ljava/lang/String;\n"

filters_data = '\n'.join('        ' + s32(v) for v in FILTERS)
TV = 'Landroid/widget/TextView;'

w('smali/app/aion2/timers/MainActivity.smali', f""".class public {A};
.super Landroid/app/Activity;
.implements Landroid/view/View$OnClickListener;
.implements Ljava/lang/Runnable;

.field static TITLES:[Ljava/lang/String;
.field static CATS:[Ljava/lang/String;
.field static ICONS:[Ljava/lang/String;
.field static FILTERS:[I

.field private handler:Landroid/os/Handler;
.field private filter:I
.field private tab:I
.field private now:J
.field private starts:[J
.field private fmt:Ljava/text/SimpleDateFormat;

.method static constructor <clinit>()V
    .locals 3
{str_array('TITLES', TITLES)}{str_array('CATS', CATS)}{str_array('ICONS', ICONS)}    const/4 v0, 0x4
    new-array v1, v0, [I
    fill-array-data v1, :arr_filters
    sput-object v1, {A};->FILTERS:[I
    return-void

    :arr_filters
    .array-data 4
{filters_data}
    .end array-data
.end method

.method public constructor <init>()V
    .locals 0
    invoke-direct {{p0}}, Landroid/app/Activity;-><init>()V
    return-void
.end method

# ---------- helpers vues
.method private vk(Ljava/lang/String;I)Landroid/view/View;
    .locals 2
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {{v0, p1}}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {{v0, p2}}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {{v0}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-direct {{p0, v0}}, {A};->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v0
    return-object v0
.end method

.method private vn(Ljava/lang/String;)Landroid/view/View;
    .locals 1
    const-string v0, "id"
    invoke-static {{p0, p1, v0}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {{p0, v0}}, {A};->findViewById(I)Landroid/view/View;
    move-result-object v0
    return-object v0
.end method

.method private tv(Ljava/lang/String;ILjava/lang/String;)V
    .locals 2
    invoke-direct {{p0, p1, p2}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    check-cast v0, {TV}
    invoke-virtual {{v0, p3}}, {TV}->setText(Ljava/lang/CharSequence;)V
    const/4 v1, 0x0
    invoke-virtual {{v0, v1}}, {TV}->setVisibility(I)V
    return-void
.end method

.method private gone(Ljava/lang/String;I)V
    .locals 2
    invoke-direct {{p0, p1, p2}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    const/16 v1, 0x8
    invoke-virtual {{v0, v1}}, Landroid/view/View;->setVisibility(I)V
    return-void
.end method

.method private listen(Ljava/lang/String;)V
    .locals 1
    invoke-direct {{p0, p1}}, {A};->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v0
    invoke-virtual {{v0, p0}}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V
    return-void
.end method

# ---------- cycle de vie
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 3
    invoke-super {{p0, p1}}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V
    const-string v0, "activity_main"
    const-string v1, "layout"
    invoke-static {{p0, v0, v1}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {{p0, v0}}, {A};->setContentView(I)V
    new-instance v0, Landroid/os/Handler;
    invoke-static {{}}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;
    move-result-object v1
    invoke-direct {{v0, v1}}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V
    iput-object v0, p0, {A};->handler:Landroid/os/Handler;
    const/4 v0, -0x1
    iput v0, p0, {A};->filter:I
    const/4 v0, 0x0
    iput v0, p0, {A};->tab:I
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "EEE HH:mm"
    invoke-static {{}}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;
    move-result-object v2
    invoke-direct {{v0, v1, v2}}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    iput-object v0, p0, {A};->fmt:Ljava/text/SimpleDateFormat;
    const-string v0, "tzlink"
    invoke-direct {{p0, v0}}, {A};->listen(Ljava/lang/String;)V
    const-string v0, "tab0"
    invoke-direct {{p0, v0}}, {A};->listen(Ljava/lang/String;)V
    const-string v0, "tab1"
    invoke-direct {{p0, v0}}, {A};->listen(Ljava/lang/String;)V
    const-string v0, "tab2"
    invoke-direct {{p0, v0}}, {A};->listen(Ljava/lang/String;)V
    const-string v0, "tab3"
    invoke-direct {{p0, v0}}, {A};->listen(Ljava/lang/String;)V
    invoke-static {{p0}}, {P}/TimerWidget;->update(Landroid/content/Context;)V
    return-void
.end method

.method protected onResume()V
    .locals 0
    invoke-super {{p0}}, Landroid/app/Activity;->onResume()V
    invoke-virtual {{p0}}, {A};->run()V
    return-void
.end method

.method protected onPause()V
    .locals 1
    invoke-super {{p0}}, Landroid/app/Activity;->onPause()V
    iget-object v0, p0, {A};->handler:Landroid/os/Handler;
    invoke-virtual {{v0, p0}}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V
    return-void
.end method

.method public run()V
    .locals 3
    invoke-direct {{p0}}, {A};->refresh()V
    iget-object v0, p0, {A};->handler:Landroid/os/Handler;
    invoke-virtual {{v0, p0}}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V
    const-wide/16 v1, 0x3a98
    invoke-virtual {{v0, p0, v1, v2}}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z
    return-void
.end method

# ---------- clics : lien fuseau + onglets
.method public onClick(Landroid/view/View;)V
    .locals 4
    invoke-virtual {{p1}}, Landroid/view/View;->getId()I
    move-result v0
    const-string v1, "tzlink"
    const-string v2, "id"
    invoke-static {{p0, v1, v2}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v1
    if-ne v0, v1, :tabs
    invoke-static {{p0}}, {P}/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "Europe/Berlin"
    invoke-virtual {{v1, v0}}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :toBerlin
    const-string v1, "Asia/Tokyo"
    goto :settz
    :toBerlin
    const-string v1, "Europe/Berlin"
    :settz
    invoke-static {{p0, v1}}, {P}/Schedule;->setTzName(Landroid/content/Context;Ljava/lang/String;)V
    invoke-direct {{p0}}, {A};->refresh()V
    invoke-static {{p0}}, {P}/TimerWidget;->update(Landroid/content/Context;)V
    return-void
    :tabs
    const/4 v2, 0x0
    :tloop
    const/4 v1, 0x4
    if-ge v2, v1, :end
    new-instance v1, Ljava/lang/StringBuilder;
    const-string v3, "tab"
    invoke-direct {{v1, v3}}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {{v1, v2}}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {{v1}}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v1
    const-string v3, "id"
    invoke-static {{p0, v1, v3}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v1
    if-ne v0, v1, :next
    iput v2, p0, {A};->tab:I
    sget-object v1, {A};->FILTERS:[I
    aget v1, v1, v2
    iput v1, p0, {A};->filter:I
    invoke-direct {{p0}}, {A};->refresh()V
    const-string v1, "scroll"
    invoke-direct {{p0, v1}}, {A};->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v1
    const/4 v2, 0x0
    invoke-virtual {{v1, v2, v2}}, Landroid/view/View;->scrollTo(II)V
    return-void
    :next
    add-int/lit8 v2, v2, 0x1
    goto :tloop
    :end
    return-void
.end method

# ---------- filtre d'onglet
.method private visibleFor(I)Z
    .locals 2
    iget v0, p0, {A};->filter:I
    const/4 v1, -0x1
    if-eq v0, v1, :yes
    if-eq v0, p1, :yes
    if-nez v0, :no
    const/4 v1, 0x1
    if-eq p1, v1, :yes
    :no
    const/4 v0, 0x0
    return v0
    :yes
    const/4 v0, 0x1
    return v0
.end method

# ---------- rafraîchissement global
.method private refresh()V
    .locals 8
    invoke-static {{}}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v0
    iput-wide v0, p0, {A};->now:J
    invoke-static {{p0}}, {P}/Schedule;->serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    move-result-object v2
    invoke-static {{v0, v1, v2}}, {P}/Schedule;->computeAll(JLjava/util/TimeZone;)[J
    move-result-object v2
    iput-object v2, p0, {A};->starts:[J
    invoke-static {{v2}}, {P}/Schedule;->order([J)[I
    move-result-object v3
    const/4 v4, 0x0
    :loop
    const/16 v5, 0x{N:x}
    if-ge v4, v5, :done
    aget v5, v3, v4
    invoke-direct {{p0, v4, v5}}, {A};->fillCard(II)V
    add-int/lit8 v4, v4, 0x1
    goto :loop
    :done
    iget v5, p0, {A};->tab:I
    const-string v4, "tab_"
    invoke-static {{p0, v4, v5}}, {P}/Schedule;->strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v4
    const-string v5, "title"
    invoke-direct {{p0, v5}}, {A};->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v5
    check-cast v5, {TV}
    invoke-virtual {{v5, v4}}, {TV}->setText(Ljava/lang/CharSequence;)V
    new-instance v4, Ljava/lang/StringBuilder;
    const-string v5, "server_prefix"
    invoke-static {{p0, v5}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v5
    invoke-direct {{v4, v5}}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-static {{p0}}, {P}/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v5
    invoke-virtual {{v4, v5}}, {SB_APPEND}
    const-string v5, "tzlink"
    invoke-direct {{p0, v5}}, {A};->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v5
    check-cast v5, {TV}
    invoke-virtual {{v5, v4}}, {TV}->setText(Ljava/lang/CharSequence;)V
    const/4 v4, 0x0
    :tloop
    const/4 v5, 0x4
    if-ge v4, v5, :tdone
    iget v5, p0, {A};->tab:I
    if-ne v4, v5, :inactive
    const v6, {s32(BLUE)}
    goto :tint
    :inactive
    const v6, {s32(GREY)}
    :tint
    const-string v7, "ti"
    invoke-direct {{p0, v7, v4}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v7
    check-cast v7, Landroid/widget/ImageView;
    invoke-virtual {{v7, v6}}, Landroid/widget/ImageView;->setColorFilter(I)V
    const-string v7, "tl"
    invoke-direct {{p0, v7, v4}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v7
    check-cast v7, {TV}
    invoke-virtual {{v7, v6}}, {TV}->setTextColor(I)V
    add-int/lit8 v4, v4, 0x1
    goto :tloop
    :tdone
    return-void
.end method

# ---------- une carte : p1 = position k, p2 = règle r
.method private fillCard(II)V
    .locals 12
    iget-object v9, p0, {A};->starts:[J
    aget-wide v0, v9, p2
    iget-wide v2, p0, {A};->now:J
    sget-object v9, {P}/Schedule;->CAT:[I
    aget v4, v9, p2
    sget-object v9, {P}/Schedule;->COLORS:[I
    aget v5, v9, v4
    invoke-direct {{p0, v4}}, {A};->visibleFor(I)Z
    move-result v9
    const-string v10, "card"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    if-eqz v9, :hide
    const/4 v9, 0x0
    goto :setvis
    :hide
    const/16 v9, 0x8
    :setvis
    invoke-virtual {{v10, v9}}, Landroid/view/View;->setVisibility(I)V
    const-string v10, "ic"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/ImageView;
    sget-object v9, {A};->ICONS:[Ljava/lang/String;
    aget-object v9, v9, v4
    const-string v11, "drawable"
    invoke-static {{p0, v9, v11}}, {P}/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v9
    invoke-virtual {{v10, v9}}, Landroid/widget/ImageView;->setImageResource(I)V
    invoke-virtual {{v10, v5}}, Landroid/widget/ImageView;->setColorFilter(I)V
    const-string v10, "cl"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, {TV}
    const-string v9, "cat_"
    invoke-static {{p0, v9, v4}}, {P}/Schedule;->strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {{v10, v9}}, {TV}->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {{v10, v5}}, {TV}->setTextColor(I)V
    const-string v10, "tm"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, {TV}
    iget-object v9, p0, {A};->fmt:Ljava/text/SimpleDateFormat;
    new-instance v11, Ljava/util/Date;
    invoke-direct {{v11, v0, v1}}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {{v9, v11}}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {{v10, v9}}, {TV}->setText(Ljava/lang/CharSequence;)V
    const-string v10, "nm"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, {TV}
    const-string v9, "rule_"
    invoke-static {{p0, v9, p2}}, {P}/Schedule;->strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {{v10, v9}}, {TV}->setText(Ljava/lang/CharSequence;)V
    cmp-long v9, v0, v2
    if-gtz v9, :upcoming
    const/4 v6, 0x1
    sget-object v9, {P}/Schedule;->DUR:[I
    aget v9, v9, p2
    int-to-long v7, v9
    const-wide/32 v10, 0xea60
    mul-long/2addr v7, v10
    add-long/2addr v7, v0
    sub-long/2addr v7, v2
    goto :rem
    :upcoming
    const/4 v6, 0x0
    sub-long v7, v0, v2
    :rem
    invoke-direct {{p0, p1, v7, v8}}, {A};->fillValue(IJ)V
    const-string v10, "cap"
    invoke-direct {{p0, v10, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, {TV}
    if-eqz v6, :capup
    const-string v9, "cap_live"
    invoke-static {{p0, v9}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {{v10, v9}}, {TV}->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {{v10, v5}}, {TV}->setTextColor(I)V
    goto :ring
    :capup
    const-string v9, "cap_until"
    invoke-static {{p0, v9}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {{v10, v9}}, {TV}->setText(Ljava/lang/CharSequence;)V
    const v9, {s32(GREY)}
    invoke-virtual {{v10, v9}}, {TV}->setTextColor(I)V
    :ring
    if-eqz v6, :ringup
    sub-long v0, v2, v0
    const-wide/16 v2, 0x3e8
    mul-long/2addr v0, v2
    sget-object v9, {P}/Schedule;->DUR:[I
    aget v9, v9, p2
    int-to-long v2, v9
    const-wide/32 v10, 0xea60
    mul-long/2addr v2, v10
    div-long/2addr v0, v2
    goto :setring
    :ringup
    const-wide/32 v0, 0x36ee80
    cmp-long v9, v7, v0
    if-ltz v9, :near
    const-wide/16 v0, 0x0
    goto :setring
    :near
    sub-long/2addr v0, v7
    const-wide/16 v2, 0x3e8
    mul-long/2addr v0, v2
    const-wide/32 v2, 0x36ee80
    div-long/2addr v0, v2
    :setring
    long-to-int v0, v0
    invoke-direct {{p0, p1, v0, v5}}, {A};->setRing(III)V
    return-void
.end method

# ---------- valeur "1 h 5 min" / "2 j 3 h" / "42 min" : p1 = k, p2:p3 = durée ms
.method private fillValue(IJ)V
    .locals 10
    const-wide/32 v0, 0xea5f
    add-long/2addr v0, p2
    const-wide/32 v2, 0xea60
    div-long/2addr v0, v2
    const-wide/16 v2, 0x5a0
    cmp-long v4, v0, v2
    if-ltz v4, :lt_day
    div-long v2, v0, v2
    const-wide/16 v4, 0x5a0
    rem-long v4, v0, v4
    const-wide/16 v6, 0x3c
    div-long/2addr v4, v6
    const-string v8, "unit_d"
    invoke-static {{p0, v8}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v8
    const-string v9, "unit_h"
    invoke-static {{p0, v9}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    goto :show2
    :lt_day
    const-wide/16 v2, 0x3c
    cmp-long v4, v0, v2
    if-ltz v4, :lt_hour
    rem-long v4, v0, v2
    div-long v2, v0, v2
    const-string v8, "unit_h"
    invoke-static {{p0, v8}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v8
    const-string v9, "unit_min"
    invoke-static {{p0, v9}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v9
    :show2
    invoke-static {{v2, v3}}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vh"
    invoke-direct {{p0, v7, p1, v6}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v7, "uh"
    invoke-direct {{p0, v7, p1, v8}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    invoke-static {{v4, v5}}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vm"
    invoke-direct {{p0, v7, p1, v6}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v7, "um"
    invoke-direct {{p0, v7, p1, v9}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    return-void
    :lt_hour
    const-string v7, "vh"
    invoke-direct {{p0, v7, p1}}, {A};->gone(Ljava/lang/String;I)V
    const-string v7, "uh"
    invoke-direct {{p0, v7, p1}}, {A};->gone(Ljava/lang/String;I)V
    invoke-static {{v0, v1}}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vm"
    invoke-direct {{p0, v7, p1, v6}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v6, "unit_min"
    invoke-static {{p0, v6}}, {P}/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v6
    const-string v7, "um"
    invoke-direct {{p0, v7, p1, v6}}, {A};->tv(Ljava/lang/String;ILjava/lang/String;)V
    return-void
.end method

# ---------- anneau : p1 = k, p2 = progression (0..1000), p3 = couleur
.method private setRing(III)V
    .locals 3
    const-string v0, "rg"
    invoke-direct {{p0, v0, p1}}, {A};->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    check-cast v0, Landroid/widget/ProgressBar;
    invoke-virtual {{v0, p2}}, Landroid/widget/ProgressBar;->setProgress(I)V
    invoke-static {{p3}}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;
    move-result-object v1
    invoke-virtual {{v0, v1}}, Landroid/widget/ProgressBar;->setProgressTintList(Landroid/content/res/ColorStateList;)V
    const v1, 0xffffff
    and-int/2addr v1, p3
    const/high16 v2, 0x26000000
    or-int/2addr v1, v2
    invoke-static {{v1}}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;
    move-result-object v1
    invoke-virtual {{v0, v1}}, Landroid/widget/ProgressBar;->setProgressBackgroundTintList(Landroid/content/res/ColorStateList;)V
    return-void
.end method
""")

print("generated", OUT)
