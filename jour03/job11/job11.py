def time_to_text(minutes):
    hours = minutes // 60
    minutes_remaining = minutes % 60
    if hours == 1:
        hours_str = "1 heure"
    else:
        hours_str = f"{hours} heures"

    if minutes_remaining == 1:
        minutes_str = "1 minute"
    else:
        minutes_str = f"{minutes_remaining} minutes"
    print(f"{hours_str} et {minutes_str}")
time_to_text(190)
