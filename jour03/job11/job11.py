def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    if heures == 1:
        heures_str = "1 heure"
    else:
        heures_str = f"{heures} heures"

    if minutes_restantes == 1:
        minutes_str = "1 minute"
    else:
        minutes_str = f"{minutes_restantes} minutes"
    print(f"{heures_str} et {minutes_str}")
time_to_text(190)
