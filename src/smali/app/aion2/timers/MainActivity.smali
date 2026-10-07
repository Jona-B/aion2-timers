.class public Lapp/aion2/timers/MainActivity;
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
    const/16 v0, 0x4
    new-array v1, v0, [Ljava/lang/String;
    const/16 v2, 0x0
    const-string v0, "R\u00e9sum\u00e9"
    aput-object v0, v1, v2
    const/16 v2, 0x1
    const-string v0, "\u00c9v\u00e8nements"
    aput-object v0, v1, v2
    const/16 v2, 0x2
    const-string v0, "Boss"
    aput-object v0, v1, v2
    const/16 v2, 0x3
    const-string v0, "PvP"
    aput-object v0, v1, v2
    sput-object v1, Lapp/aion2/timers/MainActivity;->TITLES:[Ljava/lang/String;
    const/16 v0, 0x5
    new-array v1, v0, [Ljava/lang/String;
    const/16 v2, 0x0
    const-string v0, "\u00c9v\u00e8nement"
    aput-object v0, v1, v2
    const/16 v2, 0x1
    const-string v0, "Faille"
    aput-object v0, v1, v2
    const/16 v2, 0x2
    const-string v0, "Boss"
    aput-object v0, v1, v2
    const/16 v2, 0x3
    const-string v0, "PvP"
    aput-object v0, v1, v2
    const/16 v2, 0x4
    const-string v0, "Reset"
    aput-object v0, v1, v2
    sput-object v1, Lapp/aion2/timers/MainActivity;->CATS:[Ljava/lang/String;
    const/16 v0, 0x5
    new-array v1, v0, [Ljava/lang/String;
    const/16 v2, 0x0
    const-string v0, "ic_event"
    aput-object v0, v1, v2
    const/16 v2, 0x1
    const-string v0, "ic_rift"
    aput-object v0, v1, v2
    const/16 v2, 0x2
    const-string v0, "ic_boss"
    aput-object v0, v1, v2
    const/16 v2, 0x3
    const-string v0, "ic_pvp"
    aput-object v0, v1, v2
    const/16 v2, 0x4
    const-string v0, "ic_reset"
    aput-object v0, v1, v2
    sput-object v1, Lapp/aion2/timers/MainActivity;->ICONS:[Ljava/lang/String;
    const/4 v0, 0x4
    new-array v1, v0, [I
    fill-array-data v1, :arr_filters
    sput-object v1, Lapp/aion2/timers/MainActivity;->FILTERS:[I
    return-void

    :arr_filters
    .array-data 4
        -0x1
        0x0
        0x2
        0x3
    .end array-data
.end method

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V
    return-void
.end method

# ---------- helpers vues
.method private vk(Ljava/lang/String;I)Landroid/view/View;
    .locals 2
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0, p1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v0
    return-object v0
.end method

.method private vn(Ljava/lang/String;)Landroid/view/View;
    .locals 1
    const-string v0, "id"
    invoke-static {p0, p1, v0}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {p0, v0}, Lapp/aion2/timers/MainActivity;->findViewById(I)Landroid/view/View;
    move-result-object v0
    return-object v0
.end method

.method private tv(Ljava/lang/String;ILjava/lang/String;)V
    .locals 2
    invoke-direct {p0, p1, p2}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    check-cast v0, Landroid/widget/TextView;
    invoke-virtual {v0, p3}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    const/4 v1, 0x0
    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setVisibility(I)V
    return-void
.end method

.method private gone(Ljava/lang/String;I)V
    .locals 2
    invoke-direct {p0, p1, p2}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    const/16 v1, 0x8
    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V
    return-void
.end method

.method private listen(Ljava/lang/String;)V
    .locals 1
    invoke-direct {p0, p1}, Lapp/aion2/timers/MainActivity;->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v0
    invoke-virtual {v0, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V
    return-void
.end method

# ---------- cycle de vie
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 3
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V
    const-string v0, "activity_main"
    const-string v1, "layout"
    invoke-static {p0, v0, v1}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    invoke-virtual {p0, v0}, Lapp/aion2/timers/MainActivity;->setContentView(I)V
    new-instance v0, Landroid/os/Handler;
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;
    move-result-object v1
    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V
    iput-object v0, p0, Lapp/aion2/timers/MainActivity;->handler:Landroid/os/Handler;
    const/4 v0, -0x1
    iput v0, p0, Lapp/aion2/timers/MainActivity;->filter:I
    const/4 v0, 0x0
    iput v0, p0, Lapp/aion2/timers/MainActivity;->tab:I
    new-instance v0, Ljava/text/SimpleDateFormat;
    const-string v1, "EEE HH:mm"
    sget-object v2, Ljava/util/Locale;->FRANCE:Ljava/util/Locale;
    invoke-direct {v0, v1, v2}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    iput-object v0, p0, Lapp/aion2/timers/MainActivity;->fmt:Ljava/text/SimpleDateFormat;
    const-string v0, "tzlink"
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->listen(Ljava/lang/String;)V
    const-string v0, "tab0"
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->listen(Ljava/lang/String;)V
    const-string v0, "tab1"
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->listen(Ljava/lang/String;)V
    const-string v0, "tab2"
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->listen(Ljava/lang/String;)V
    const-string v0, "tab3"
    invoke-direct {p0, v0}, Lapp/aion2/timers/MainActivity;->listen(Ljava/lang/String;)V
    invoke-static {p0}, Lapp/aion2/timers/TimerWidget;->update(Landroid/content/Context;)V
    return-void
.end method

.method protected onResume()V
    .locals 0
    invoke-super {p0}, Landroid/app/Activity;->onResume()V
    invoke-virtual {p0}, Lapp/aion2/timers/MainActivity;->run()V
    return-void
.end method

.method protected onPause()V
    .locals 1
    invoke-super {p0}, Landroid/app/Activity;->onPause()V
    iget-object v0, p0, Lapp/aion2/timers/MainActivity;->handler:Landroid/os/Handler;
    invoke-virtual {v0, p0}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V
    return-void
.end method

.method public run()V
    .locals 3
    invoke-direct {p0}, Lapp/aion2/timers/MainActivity;->refresh()V
    iget-object v0, p0, Lapp/aion2/timers/MainActivity;->handler:Landroid/os/Handler;
    invoke-virtual {v0, p0}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V
    const-wide/16 v1, 0x3a98
    invoke-virtual {v0, p0, v1, v2}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z
    return-void
.end method

# ---------- clics : lien fuseau + onglets
.method public onClick(Landroid/view/View;)V
    .locals 4
    invoke-virtual {p1}, Landroid/view/View;->getId()I
    move-result v0
    const-string v1, "tzlink"
    const-string v2, "id"
    invoke-static {p0, v1, v2}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v1
    if-ne v0, v1, :tabs
    invoke-static {p0}, Lapp/aion2/timers/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v0
    const-string v1, "Europe/Berlin"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :toBerlin
    const-string v1, "Asia/Tokyo"
    goto :settz
    :toBerlin
    const-string v1, "Europe/Berlin"
    :settz
    invoke-static {p0, v1}, Lapp/aion2/timers/Schedule;->setTzName(Landroid/content/Context;Ljava/lang/String;)V
    invoke-direct {p0}, Lapp/aion2/timers/MainActivity;->refresh()V
    invoke-static {p0}, Lapp/aion2/timers/TimerWidget;->update(Landroid/content/Context;)V
    return-void
    :tabs
    const/4 v2, 0x0
    :tloop
    const/4 v1, 0x4
    if-ge v2, v1, :end
    new-instance v1, Ljava/lang/StringBuilder;
    const-string v3, "tab"
    invoke-direct {v1, v3}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v1
    const-string v3, "id"
    invoke-static {p0, v1, v3}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v1
    if-ne v0, v1, :next
    iput v2, p0, Lapp/aion2/timers/MainActivity;->tab:I
    sget-object v1, Lapp/aion2/timers/MainActivity;->FILTERS:[I
    aget v1, v1, v2
    iput v1, p0, Lapp/aion2/timers/MainActivity;->filter:I
    invoke-direct {p0}, Lapp/aion2/timers/MainActivity;->refresh()V
    const-string v1, "scroll"
    invoke-direct {p0, v1}, Lapp/aion2/timers/MainActivity;->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v1
    const/4 v2, 0x0
    invoke-virtual {v1, v2, v2}, Landroid/view/View;->scrollTo(II)V
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
    iget v0, p0, Lapp/aion2/timers/MainActivity;->filter:I
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
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v0
    iput-wide v0, p0, Lapp/aion2/timers/MainActivity;->now:J
    invoke-static {p0}, Lapp/aion2/timers/Schedule;->serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    move-result-object v2
    invoke-static {v0, v1, v2}, Lapp/aion2/timers/Schedule;->computeAll(JLjava/util/TimeZone;)[J
    move-result-object v2
    iput-object v2, p0, Lapp/aion2/timers/MainActivity;->starts:[J
    invoke-static {v2}, Lapp/aion2/timers/Schedule;->order([J)[I
    move-result-object v3
    const/4 v4, 0x0
    :loop
    const/16 v5, 0xd
    if-ge v4, v5, :done
    aget v5, v3, v4
    invoke-direct {p0, v4, v5}, Lapp/aion2/timers/MainActivity;->fillCard(II)V
    add-int/lit8 v4, v4, 0x1
    goto :loop
    :done
    sget-object v4, Lapp/aion2/timers/MainActivity;->TITLES:[Ljava/lang/String;
    iget v5, p0, Lapp/aion2/timers/MainActivity;->tab:I
    aget-object v4, v4, v5
    const-string v5, "title"
    invoke-direct {p0, v5}, Lapp/aion2/timers/MainActivity;->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v5
    check-cast v5, Landroid/widget/TextView;
    invoke-virtual {v5, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    new-instance v4, Ljava/lang/StringBuilder;
    const-string v5, "Serveur : "
    invoke-direct {v4, v5}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-static {p0}, Lapp/aion2/timers/Schedule;->tzName(Landroid/content/Context;)Ljava/lang/String;
    move-result-object v5
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const-string v5, "tzlink"
    invoke-direct {p0, v5}, Lapp/aion2/timers/MainActivity;->vn(Ljava/lang/String;)Landroid/view/View;
    move-result-object v5
    check-cast v5, Landroid/widget/TextView;
    invoke-virtual {v5, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    const/4 v4, 0x0
    :tloop
    const/4 v5, 0x4
    if-ge v4, v5, :tdone
    iget v5, p0, Lapp/aion2/timers/MainActivity;->tab:I
    if-ne v4, v5, :inactive
    const v6, -0xff8501
    goto :tint
    :inactive
    const v6, -0x71716d
    :tint
    const-string v7, "ti"
    invoke-direct {p0, v7, v4}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v7
    check-cast v7, Landroid/widget/ImageView;
    invoke-virtual {v7, v6}, Landroid/widget/ImageView;->setColorFilter(I)V
    const-string v7, "tl"
    invoke-direct {p0, v7, v4}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v7
    check-cast v7, Landroid/widget/TextView;
    invoke-virtual {v7, v6}, Landroid/widget/TextView;->setTextColor(I)V
    add-int/lit8 v4, v4, 0x1
    goto :tloop
    :tdone
    return-void
.end method

# ---------- une carte : p1 = position k, p2 = règle r
.method private fillCard(II)V
    .locals 12
    iget-object v9, p0, Lapp/aion2/timers/MainActivity;->starts:[J
    aget-wide v0, v9, p2
    iget-wide v2, p0, Lapp/aion2/timers/MainActivity;->now:J
    sget-object v9, Lapp/aion2/timers/Schedule;->CAT:[I
    aget v4, v9, p2
    sget-object v9, Lapp/aion2/timers/Schedule;->COLORS:[I
    aget v5, v9, v4
    invoke-direct {p0, v4}, Lapp/aion2/timers/MainActivity;->visibleFor(I)Z
    move-result v9
    const-string v10, "card"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    if-eqz v9, :hide
    const/4 v9, 0x0
    goto :setvis
    :hide
    const/16 v9, 0x8
    :setvis
    invoke-virtual {v10, v9}, Landroid/view/View;->setVisibility(I)V
    const-string v10, "ic"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/ImageView;
    sget-object v9, Lapp/aion2/timers/MainActivity;->ICONS:[Ljava/lang/String;
    aget-object v9, v9, v4
    const-string v11, "drawable"
    invoke-static {p0, v9, v11}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v9
    invoke-virtual {v10, v9}, Landroid/widget/ImageView;->setImageResource(I)V
    invoke-virtual {v10, v5}, Landroid/widget/ImageView;->setColorFilter(I)V
    const-string v10, "cl"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/TextView;
    sget-object v9, Lapp/aion2/timers/MainActivity;->CATS:[Ljava/lang/String;
    aget-object v9, v9, v4
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {v10, v5}, Landroid/widget/TextView;->setTextColor(I)V
    const-string v10, "tm"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/TextView;
    iget-object v9, p0, Lapp/aion2/timers/MainActivity;->fmt:Ljava/text/SimpleDateFormat;
    new-instance v11, Ljava/util/Date;
    invoke-direct {v11, v0, v1}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {v9, v11}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v9
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    const-string v10, "nm"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/TextView;
    sget-object v9, Lapp/aion2/timers/Schedule;->NAMES:[Ljava/lang/String;
    aget-object v9, v9, p2
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    cmp-long v9, v0, v2
    if-gtz v9, :upcoming
    const/4 v6, 0x1
    sget-object v9, Lapp/aion2/timers/Schedule;->DUR:[I
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
    invoke-direct {p0, p1, v7, v8}, Lapp/aion2/timers/MainActivity;->fillValue(IJ)V
    const-string v10, "cap"
    invoke-direct {p0, v10, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v10
    check-cast v10, Landroid/widget/TextView;
    if-eqz v6, :capup
    const-string v9, "restantes \u00b7 en cours"
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    invoke-virtual {v10, v5}, Landroid/widget/TextView;->setTextColor(I)V
    goto :ring
    :capup
    const-string v9, "avant le d\u00e9but"
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V
    const v9, -0x71716d
    invoke-virtual {v10, v9}, Landroid/widget/TextView;->setTextColor(I)V
    :ring
    if-eqz v6, :ringup
    sub-long v0, v2, v0
    const-wide/16 v2, 0x3e8
    mul-long/2addr v0, v2
    sget-object v9, Lapp/aion2/timers/Schedule;->DUR:[I
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
    invoke-direct {p0, p1, v0, v5}, Lapp/aion2/timers/MainActivity;->setRing(III)V
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
    const-string v8, "j"
    const-string v9, "h"
    goto :show2
    :lt_day
    const-wide/16 v2, 0x3c
    cmp-long v4, v0, v2
    if-ltz v4, :lt_hour
    rem-long v4, v0, v2
    div-long v2, v0, v2
    const-string v8, "h"
    const-string v9, "min"
    :show2
    invoke-static {v2, v3}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vh"
    invoke-direct {p0, v7, p1, v6}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v7, "uh"
    invoke-direct {p0, v7, p1, v8}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    invoke-static {v4, v5}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vm"
    invoke-direct {p0, v7, p1, v6}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v7, "um"
    invoke-direct {p0, v7, p1, v9}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    return-void
    :lt_hour
    const-string v7, "vh"
    invoke-direct {p0, v7, p1}, Lapp/aion2/timers/MainActivity;->gone(Ljava/lang/String;I)V
    const-string v7, "uh"
    invoke-direct {p0, v7, p1}, Lapp/aion2/timers/MainActivity;->gone(Ljava/lang/String;I)V
    invoke-static {v0, v1}, Ljava/lang/Long;->toString(J)Ljava/lang/String;
    move-result-object v6
    const-string v7, "vm"
    invoke-direct {p0, v7, p1, v6}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    const-string v6, "min"
    const-string v7, "um"
    invoke-direct {p0, v7, p1, v6}, Lapp/aion2/timers/MainActivity;->tv(Ljava/lang/String;ILjava/lang/String;)V
    return-void
.end method

# ---------- anneau : p1 = k, p2 = progression (0..1000), p3 = couleur
.method private setRing(III)V
    .locals 3
    const-string v0, "rg"
    invoke-direct {p0, v0, p1}, Lapp/aion2/timers/MainActivity;->vk(Ljava/lang/String;I)Landroid/view/View;
    move-result-object v0
    check-cast v0, Landroid/widget/ProgressBar;
    invoke-virtual {v0, p2}, Landroid/widget/ProgressBar;->setProgress(I)V
    invoke-static {p3}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;
    move-result-object v1
    invoke-virtual {v0, v1}, Landroid/widget/ProgressBar;->setProgressTintList(Landroid/content/res/ColorStateList;)V
    const v1, 0xffffff
    and-int/2addr v1, p3
    const/high16 v2, 0x26000000
    or-int/2addr v1, v2
    invoke-static {v1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;
    move-result-object v1
    invoke-virtual {v0, v1}, Landroid/widget/ProgressBar;->setProgressBackgroundTintList(Landroid/content/res/ColorStateList;)V
    return-void
.end method
