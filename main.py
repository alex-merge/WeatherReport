#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import meteofrance_api
import time
import os
import datetime

CHATID = os.getenv('CHATID')
BOTID = os.getenv('BOTID')

# 1 : Vent
# 2 : pluie/inondation
# 3 : orage
# 4 : crues
# 5 :
# 6 :
# 7 :
# 8 : avalanche

Forecast = meteofrance_api.MeteoFranceClient()
phenomenons_names = {
    1 : "Vent",
    2 : "Pluie/inondation",
    3 : "Orage",
    }

while True:
    alerts = Forecast.get_warning_current_phenomenoms("31").phenomenons_max_colors
    alert_sent = 0
    try :
        for elem in alerts:
            if (elem["phenomenon_id"] in [1, 2, 3]) and \
                (elem["phenomenons_max_color_id"] > 1):
                subprocess.run(["./telegram_msg",
                                f"Nouvelle alerte : {phenomenons_names[elem['phenomenon_id']]}",
				CHATID,
				BOTID])
                alert_sent += 1
    except : 
        0 == 0
        
    if alert_sent == 0:
        subprocess.run(["./telegram_bot",
                        f"Pas d'alerte meteo pour le moment",
			CHATID,
			BOTID])
    
    t_hour, t_min = datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%M")
    n_min, n_hour = 60-int(t_min), 23-int(t_hour)+8
    n_sec = n_min*60+n_hour*60*60

    time.sleep(n_sec)
