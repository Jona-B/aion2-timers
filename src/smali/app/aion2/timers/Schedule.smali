.class public final Lapp/aion2/timers/Schedule;
.super Ljava/lang/Object;

.field public static NAMES:[Ljava/lang/String;
.field public static CAT:[I
.field public static MASK:[I
.field public static START:[I
.field public static STEP:[I
.field public static COUNT:[I
.field public static DUR:[I
.field public static UTC:[I
.field public static COLORS:[I

.method static constructor <clinit>()V
    .locals 3
    const/16 v0, 0xd
    new-array v1, v0, [Ljava/lang/String;
    const/16 v2, 0x0
    const-string v0, "Festival des Shugos"
    aput-object v0, v1, v2
    const/16 v2, 0x1
    const-string v0, "Invasion dimensionnelle"
    aput-object v0, v1, v2
    const/16 v2, 0x2
    const-string v0, "Faille spatio-temporelle"
    aput-object v0, v1, v2
    const/16 v2, 0x3
    const-string v0, "Kaira la veilleuse"
    aput-object v0, v1, v2
    const/16 v2, 0x4
    const-string v0, "Si\u00e8ge des artefacts"
    aput-object v0, v1, v2
    const/16 v2, 0x5
    const-string v0, "Ex\u00e9cuteurs Argo \u00b7 Kaira \u00b7 Tamasa"
    aput-object v0, v1, v2
    const/16 v2, 0x6
    const-string v0, "Seigneur gardien Nahma"
    aput-object v0, v1, v2
    const/16 v2, 0x7
    const-string v0, "Ar\u00e8ne 10v10 (midi)"
    aput-object v0, v1, v2
    const/16 v2, 0x8
    const-string v0, "Ar\u00e8ne 10v10 (soir)"
    aput-object v0, v1, v2
    const/16 v2, 0x9
    const-string v0, "Reset quotidien"
    aput-object v0, v1, v2
    const/16 v2, 0xa
    const-string v0, "Reset hebdomadaire"
    aput-object v0, v1, v2
    const/16 v2, 0xb
    const-string v0, "Boss niv. 80 : Dramos \u00b7 Marakha \u00b7 Ducal"
    aput-object v0, v1, v2
    const/16 v2, 0xc
    const-string v0, "Nahma enrag\u00e9 (niv. 80)"
    aput-object v0, v1, v2
    sput-object v1, Lapp/aion2/timers/Schedule;->NAMES:[Ljava/lang/String;
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_cat
    sput-object v1, Lapp/aion2/timers/Schedule;->CAT:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_mask
    sput-object v1, Lapp/aion2/timers/Schedule;->MASK:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_start
    sput-object v1, Lapp/aion2/timers/Schedule;->START:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_step
    sput-object v1, Lapp/aion2/timers/Schedule;->STEP:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_count
    sput-object v1, Lapp/aion2/timers/Schedule;->COUNT:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_dur
    sput-object v1, Lapp/aion2/timers/Schedule;->DUR:[I
    const/16 v0, 0xd
    new-array v1, v0, [I
    fill-array-data v1, :arr_utc
    sput-object v1, Lapp/aion2/timers/Schedule;->UTC:[I
    const/16 v0, 0x5
    new-array v1, v0, [I
    fill-array-data v1, :arr_colors
    sput-object v1, Lapp/aion2/timers/Schedule;->COLORS:[I
    return-void

    :arr_cat
    .array-data 4
        0x0
        0x0
        0x1
        0x2
        0x3
        0x2
        0x2
        0x3
        0x3
        0x4
        0x4
        0x2
        0x2
    .end array-data
    :arr_mask
    .array-data 4
        0xfe
        0xfe
        0xfe
        0xfe
        0xa4
        0xa4
        0x42
        0xfe
        0xfe
        0xfe
        0x10
        0xa4
        0x42
    .end array-data
    :arr_start
    .array-data 4
        0x0
        0x1e
        0x78
        0x3c
        0x4ec
        0x50a
        0x4ec
        0x294
        0x474
        0x3c0
        0x3c0
        0x50a
        0x4ec
    .end array-data
    :arr_step
    .array-data 4
        0x3c
        0x3c
        0xb4
        0xb4
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
    .end array-data
    :arr_count
    .array-data 4
        0x18
        0x18
        0x8
        0x8
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
        0x1
    .end array-data
    :arr_dur
    .array-data 4
        0x8
        0xd
        0xa
        0xa
        0x1e
        0xf
        0xf
        0xb4
        0x78
        0x0
        0x0
        0xf
        0xf
    .end array-data
    :arr_utc
    .array-data 4
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
        0x0
    .end array-data
    :arr_colors
    .array-data 4
        0xff007aff
        0xffaf52de
        0xffff2d55
        0xffff9500
        0xff30b0c7
    .end array-data
.end method

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    return-void
.end method

# Start (ms) of the first occurrence of rule p0 that has not ended yet at time p1:p2.
.method public static nextStart(IJLjava/util/TimeZone;)J
    .locals 12
    sget-object v2, Lapp/aion2/timers/Schedule;->UTC:[I
    aget v2, v2, p0
    if-eqz v2, :tzok
    const-string v2, "UTC"
    invoke-static {v2}, Ljava/util/TimeZone;->getTimeZone(Ljava/lang/String;)Ljava/util/TimeZone;
    move-result-object p3
    :tzok
    sget-object v2, Lapp/aion2/timers/Schedule;->DUR:[I
    aget v2, v2, p0
    int-to-long v3, v2
    const-wide/32 v9, 0xea60
    mul-long/2addr v3, v9
    invoke-static {p3}, Ljava/util/Calendar;->getInstance(Ljava/util/TimeZone;)Ljava/util/Calendar;
    move-result-object v0
    const/4 v1, -0x1
    :dayloop
    const/16 v2, 0x8
    if-ge v1, v2, :notfound
    invoke-virtual {v0, p1, p2}, Ljava/util/Calendar;->setTimeInMillis(J)V
    const/4 v2, 0x5
    invoke-virtual {v0, v2, v1}, Ljava/util/Calendar;->add(II)V
    const/4 v2, 0x7
    invoke-virtual {v0, v2}, Ljava/util/Calendar;->get(I)I
    move-result v2
    sget-object v11, Lapp/aion2/timers/Schedule;->MASK:[I
    aget v11, v11, p0
    shr-int/2addr v11, v2
    and-int/lit8 v11, v11, 0x1
    if-eqz v11, :nextday
    const/4 v5, 0x0
    :slotloop
    sget-object v11, Lapp/aion2/timers/Schedule;->COUNT:[I
    aget v11, v11, p0
    if-ge v5, v11, :nextday
    sget-object v11, Lapp/aion2/timers/Schedule;->STEP:[I
    aget v11, v11, p0
    mul-int v6, v5, v11
    sget-object v11, Lapp/aion2/timers/Schedule;->START:[I
    aget v11, v11, p0
    add-int/2addr v6, v11
    div-int/lit8 v11, v6, 0x3c
    const/16 v2, 0xb
    invoke-virtual {v0, v2, v11}, Ljava/util/Calendar;->set(II)V
    rem-int/lit8 v11, v6, 0x3c
    const/16 v2, 0xc
    invoke-virtual {v0, v2, v11}, Ljava/util/Calendar;->set(II)V
    const/4 v11, 0x0
    const/16 v2, 0xd
    invoke-virtual {v0, v2, v11}, Ljava/util/Calendar;->set(II)V
    const/16 v2, 0xe
    invoke-virtual {v0, v2, v11}, Ljava/util/Calendar;->set(II)V
    invoke-virtual {v0}, Ljava/util/Calendar;->getTimeInMillis()J
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
    const/16 v0, 0xd
    new-array v1, v0, [J
    const/4 v2, 0x0
    :loop
    if-ge v2, v0, :done
    invoke-static {v2, p0, p1, p2}, Lapp/aion2/timers/Schedule;->nextStart(IJLjava/util/TimeZone;)J
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
    invoke-virtual {p0, v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
    move-result-object v0
    const-string v1, "tz"
    const-string v2, "Europe/Berlin"
    invoke-interface {v0, v1, v2}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method public static setTzName(Landroid/content/Context;Ljava/lang/String;)V
    .locals 2
    const-string v0, "aion"
    const/4 v1, 0x0
    invoke-virtual {p0, v0, v1}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;
    move-result-object v0
    invoke-interface {v0}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;
    move-result-object v0
    const-string v1, "tz"
    invoke-interface {v0, v1, p1}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;
    move-result-object v0
    invoke-interface {v0}, Landroid/content/SharedPreferences$Editor;->apply()V
    return-void
.end method

.method public static serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    .locals 1
    invoke-static {p0}, Lapp/aion2/timers/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v0
    invoke-static {v0}, Ljava/util/TimeZone;->getTimeZone(Ljava/lang/String;)Ljava/util/TimeZone;
    move-result-object v0
    return-object v0
.end method

.method public static id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    .locals 2
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;
    move-result-object v0
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v1
    invoke-virtual {v0, p1, p2, v1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    return v0
.end method

.method public static str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    const-string v0, "string"
    invoke-static {p0, p1, v0}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {p0, v0}, Landroid/content/Context;->getString(I)Ljava/lang/String;
    move-result-object v0
    return-object v0
.end method

.method public static strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    .locals 1
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0, p1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-static {p0, v0}, Lapp/aion2/timers/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
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
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V
    invoke-virtual {v4, v0, v1}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;
    const-string v5, " min"
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v4
    return-object v4
    :hours
    div-long v4, v0, v2
    rem-long v6, v0, v2
    invoke-static {v4, v5}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v4
    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;
    move-result-object v6
    const/4 v8, 0x2
    new-array v8, v8, [Ljava/lang/Object;
    const/4 v9, 0x0
    aput-object v4, v8, v9
    const/4 v9, 0x1
    aput-object v6, v8, v9
    const-string v9, "%d h %02d"
    invoke-static {v9, v8}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;
    move-result-object v9
    return-object v9
.end method
