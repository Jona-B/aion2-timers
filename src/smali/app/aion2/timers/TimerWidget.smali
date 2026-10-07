.class public Lapp/aion2/timers/TimerWidget;
.super Landroid/appwidget/AppWidgetProvider;

.field static sCtx:Landroid/content/Context;
.field static sNow:J
.field static sElapsed:J
.field static sFmt:Ljava/text/SimpleDateFormat;
.field static sStarts:[J
.field static sFmtTime:Ljava/text/SimpleDateFormat;

.method public constructor <init>()V
    .locals 0
    invoke-direct {p0}, Landroid/appwidget/AppWidgetProvider;-><init>()V
    return-void
.end method

.method public onUpdate(Landroid/content/Context;Landroid/appwidget/AppWidgetManager;[I)V
    .locals 0
    invoke-static {p1}, Lapp/aion2/timers/TimerWidget;->update(Landroid/content/Context;)V
    return-void
.end method

.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .locals 2
    invoke-super {p0, p1, p2}, Landroid/appwidget/AppWidgetProvider;->onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :end
    const-string v1, "app.aion2.timers.REFRESH"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    const-string v1, "android.intent.action.TIME_SET"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    const-string v1, "android.intent.action.TIMEZONE_CHANGED"
    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v1
    if-nez v1, :doit
    goto :end
    :doit
    invoke-static {p1}, Lapp/aion2/timers/TimerWidget;->update(Landroid/content/Context;)V
    :end
    return-void
.end method

.method static vid(Landroid/content/Context;Ljava/lang/String;I)I
    .locals 2
    new-instance v0, Ljava/lang/StringBuilder;
    invoke-direct {v0, p1}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    const-string v1, "id"
    invoke-static {p0, v0, v1}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v0
    return v0
.end method

# Fill row p1 with rule p2; returns the time (ms) the row's countdown targets.
.method static row(Landroid/widget/RemoteViews;II)J
    .locals 13
    sget-object v0, Lapp/aion2/timers/TimerWidget;->sCtx:Landroid/content/Context;
    sget-object v1, Lapp/aion2/timers/TimerWidget;->sStarts:[J
    aget-wide v2, v1, p2
    sget-wide v4, Lapp/aion2/timers/TimerWidget;->sNow:J
    sget-object v1, Lapp/aion2/timers/Schedule;->DUR:[I
    aget v1, v1, p2
    int-to-long v6, v1
    const-wide/32 v8, 0xea60
    mul-long/2addr v6, v8
    add-long/2addr v6, v2
    const-string v1, "n"
    invoke-static {v0, v1, p1}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    const-string v1, "rule_"
    invoke-static {v0, v1, p2}, Lapp/aion2/timers/Schedule;->strk(Landroid/content/Context;Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v1
    invoke-virtual {p0, v8, v1}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    const-string v1, "d"
    invoke-static {v0, v1, p1}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    sget-object v1, Lapp/aion2/timers/Schedule;->CAT:[I
    aget v1, v1, p2
    sget-object v9, Lapp/aion2/timers/Schedule;->COLORS:[I
    aget v1, v9, v1
    invoke-virtual {p0, v8, v1}, Landroid/widget/RemoteViews;->setTextColor(II)V
    cmp-long v1, v2, v4
    if-gtz v1, :future
    const-string v10, "ongoing"
    invoke-static {v0, v10}, Lapp/aion2/timers/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v10
    move-wide v11, v6
    goto :settext
    :future
    sget-object v1, Lapp/aion2/timers/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v9, Ljava/util/Date;
    invoke-direct {v9, v2, v3}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {v1, v9}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v10
    move-wide v11, v2
    :settext
    const-string v1, "w"
    invoke-static {v0, v1, p1}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    invoke-virtual {p0, v8, v10}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    const-string v1, "c"
    invoke-static {v0, v1, p1}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v8
    sub-long v4, v11, v4
    sget-wide v6, Lapp/aion2/timers/TimerWidget;->sElapsed:J
    add-long/2addr v4, v6
    move-object v2, p0
    move v3, v8
    const/4 v6, 0x0
    const/4 v7, 0x1
    invoke-virtual/range {v2 .. v7}, Landroid/widget/RemoteViews;->setChronometer(IJLjava/lang/String;Z)V
    const/4 v7, 0x1
    invoke-virtual {p0, v8, v7}, Landroid/widget/RemoteViews;->setChronometerCountDown(IZ)V
    return-wide v11
.end method

# Hero block (row 0): colored name, category icon, "Today at 22:00" / "Live · ends at 22:08".
.method static hero(Landroid/content/Context;Landroid/widget/RemoteViews;I)V
    .locals 12
    sget-object v0, Lapp/aion2/timers/Schedule;->CAT:[I
    aget v0, v0, p2
    sget-object v1, Lapp/aion2/timers/Schedule;->COLORS:[I
    aget v1, v1, v0
    const-string v2, "n"
    const/4 v3, 0x0
    invoke-static {p0, v2, v3}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v2
    invoke-virtual {p1, v2, v1}, Landroid/widget/RemoteViews;->setTextColor(II)V
    const-string v2, "hi"
    const-string v3, "id"
    invoke-static {p0, v2, v3}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v2
    sget-object v3, Lapp/aion2/timers/MainActivity;->ICONS:[Ljava/lang/String;
    aget-object v3, v3, v0
    const-string v4, "drawable"
    invoke-static {p0, v3, v4}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v3
    invoke-virtual {p1, v2, v3}, Landroid/widget/RemoteViews;->setImageViewResource(II)V
    const-string v3, "setColorFilter"
    invoke-virtual {p1, v2, v3, v1}, Landroid/widget/RemoteViews;->setInt(ILjava/lang/String;I)V
    sget-object v3, Lapp/aion2/timers/TimerWidget;->sStarts:[J
    aget-wide v4, v3, p2
    sget-wide v6, Lapp/aion2/timers/TimerWidget;->sNow:J
    new-instance v8, Ljava/lang/StringBuilder;
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V
    cmp-long v3, v4, v6
    if-gtz v3, :future
    const-string v2, "ongoing_until"
    invoke-static {p0, v2}, Lapp/aion2/timers/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    sget-object v2, Lapp/aion2/timers/Schedule;->DUR:[I
    aget v2, v2, p2
    int-to-long v9, v2
    const-wide/32 v2, 0xea60
    mul-long/2addr v9, v2
    add-long/2addr v9, v4
    goto :time
    :future
    move-wide v9, v4
    invoke-static {v4, v5}, Landroid/text/format/DateUtils;->isToday(J)Z
    move-result v2
    if-eqz v2, :other
    const-string v2, "today_at"
    invoke-static {p0, v2}, Lapp/aion2/timers/Schedule;->str(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    goto :time
    :other
    sget-object v2, Lapp/aion2/timers/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v3, Ljava/util/Date;
    invoke-direct {v3, v4, v5}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {v2, v3}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    goto :settext
    :time
    sget-object v2, Lapp/aion2/timers/TimerWidget;->sFmtTime:Ljava/text/SimpleDateFormat;
    new-instance v3, Ljava/util/Date;
    invoke-direct {v3, v9, v10}, Ljava/util/Date;-><init>(J)V
    invoke-virtual {v2, v3}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;
    move-result-object v2
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    :settext
    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v8
    const-string v2, "w"
    const/4 v3, 0x0
    invoke-static {p0, v2, v3}, Lapp/aion2/timers/TimerWidget;->vid(Landroid/content/Context;Ljava/lang/String;I)I
    move-result v2
    invoke-virtual {p1, v2, v8}, Landroid/widget/RemoteViews;->setTextViewText(ILjava/lang/CharSequence;)V
    return-void
.end method

.method public static update(Landroid/content/Context;)V
    .locals 14
    sput-object p0, Lapp/aion2/timers/TimerWidget;->sCtx:Landroid/content/Context;
    invoke-static {p0}, Landroid/appwidget/AppWidgetManager;->getInstance(Landroid/content/Context;)Landroid/appwidget/AppWidgetManager;
    move-result-object v0
    new-instance v1, Landroid/content/ComponentName;
    const-class v2, Lapp/aion2/timers/TimerWidget;
    invoke-direct {v1, p0, v2}, Landroid/content/ComponentName;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    invoke-virtual {v0, v1}, Landroid/appwidget/AppWidgetManager;->getAppWidgetIds(Landroid/content/ComponentName;)[I
    move-result-object v1
    array-length v2, v1
    if-nez v2, :has
    return-void
    :has
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J
    move-result-wide v2
    sput-wide v2, Lapp/aion2/timers/TimerWidget;->sNow:J
    invoke-static {}, Landroid/os/SystemClock;->elapsedRealtime()J
    move-result-wide v4
    sput-wide v4, Lapp/aion2/timers/TimerWidget;->sElapsed:J
    new-instance v4, Ljava/text/SimpleDateFormat;
    const-string v5, "EEE HH:mm"
    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;
    move-result-object v6
    invoke-direct {v4, v5, v6}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    sput-object v4, Lapp/aion2/timers/TimerWidget;->sFmt:Ljava/text/SimpleDateFormat;
    new-instance v4, Ljava/text/SimpleDateFormat;
    const-string v5, "HH:mm"
    invoke-direct {v4, v5, v6}, Ljava/text/SimpleDateFormat;-><init>(Ljava/lang/String;Ljava/util/Locale;)V
    sput-object v4, Lapp/aion2/timers/TimerWidget;->sFmtTime:Ljava/text/SimpleDateFormat;
    invoke-static {p0}, Lapp/aion2/timers/Schedule;->serverTz(Landroid/content/Context;)Ljava/util/TimeZone;
    move-result-object v4
    invoke-static {v2, v3, v4}, Lapp/aion2/timers/Schedule;->computeAll(JLjava/util/TimeZone;)[J
    move-result-object v5
    sput-object v5, Lapp/aion2/timers/TimerWidget;->sStarts:[J
    invoke-static {v5}, Lapp/aion2/timers/Schedule;->order([J)[I
    move-result-object v6
    new-instance v7, Landroid/widget/RemoteViews;
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    move-result-object v8
    const-string v9, "widget"
    const-string v10, "layout"
    invoke-static {p0, v9, v10}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v9
    invoke-direct {v7, v8, v9}, Landroid/widget/RemoteViews;-><init>(Ljava/lang/String;I)V
    const-wide/32 v8, 0x1b7740
    add-long/2addr v8, v2
    const/4 v10, 0x0
    :loop
    const/16 v11, 0x7
    if-ge v10, v11, :loopdone
    aget v11, v6, v10
    invoke-static {v7, v10, v11}, Lapp/aion2/timers/TimerWidget;->row(Landroid/widget/RemoteViews;II)J
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
    invoke-static {p0, v7, v10}, Lapp/aion2/timers/TimerWidget;->hero(Landroid/content/Context;Landroid/widget/RemoteViews;I)V
    new-instance v10, Landroid/content/Intent;
    const-class v11, Lapp/aion2/timers/MainActivity;
    invoke-direct {v10, p0, v11}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const/4 v11, 0x0
    const/high16 v12, 0xc000000
    invoke-static {p0, v11, v10, v12}, Landroid/app/PendingIntent;->getActivity(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;
    move-result-object v10
    const-string v11, "root"
    const-string v12, "id"
    invoke-static {p0, v11, v12}, Lapp/aion2/timers/Schedule;->id(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)I
    move-result v11
    invoke-virtual {v7, v11, v10}, Landroid/widget/RemoteViews;->setOnClickPendingIntent(ILandroid/app/PendingIntent;)V
    invoke-virtual {v0, v1, v7}, Landroid/appwidget/AppWidgetManager;->updateAppWidget([ILandroid/widget/RemoteViews;)V
    const-wide/16 v10, 0x3e8
    add-long/2addr v8, v10
    invoke-static {p0, v8, v9}, Lapp/aion2/timers/TimerWidget;->schedule(Landroid/content/Context;J)V
    return-void
.end method

.method static schedule(Landroid/content/Context;J)V
    .locals 5
    const-string v0, "alarm"
    invoke-virtual {p0, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;
    move-result-object v0
    check-cast v0, Landroid/app/AlarmManager;
    new-instance v1, Landroid/content/Intent;
    const-class v2, Lapp/aion2/timers/TimerWidget;
    invoke-direct {v1, p0, v2}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const-string v2, "app.aion2.timers.REFRESH"
    invoke-virtual {v1, v2}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;
    const/4 v2, 0x1
    const/high16 v3, 0xc000000
    invoke-static {p0, v2, v1, v3}, Landroid/app/PendingIntent;->getBroadcast(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;
    move-result-object v1
    const/4 v2, 0x1
    :try_start
    invoke-virtual {v0, v2, p1, p2, v1}, Landroid/app/AlarmManager;->setExact(IJLandroid/app/PendingIntent;)V
    :try_end
    .catch Ljava/lang/SecurityException; {:try_start .. :try_end} :fallback
    return-void
    :fallback
    invoke-virtual {v0, v2, p1, p2, v1}, Landroid/app/AlarmManager;->set(IJLandroid/app/PendingIntent;)V
    return-void
.end method
