from datetime import datetime, timedelta
from db import fetch_historical_data

def generate_store_report(store_id):
    current_time = datetime.utcnow()
    last_hour_start_time = current_time - timedelta(hours=1)
    last_day_start_time = current_time - timedelta(days=1)
    last_week_start_time = current_time - timedelta(weeks=1)

    uptime_last_hour = 0
    downtime_last_hour = 0
    uptime_last_day = 0
    downtime_last_day = 0
    uptime_last_week = 0
    downtime_last_week = 0

    historical_data = fetch_historical_data(store_id, last_hour_start_time, current_time)

    for data_point in historical_data:
        if data_point[1] == 'active':
            uptime_last_hour += 1
        else:
            downtime_last_hour += 1

    report = {
        "store_id": store_id,
        "uptime_last_hour": uptime_last_hour,
        "downtime_last_hour": downtime_last_hour,
        "uptime_last_day": uptime_last_day,
        "downtime_last_day": downtime_last_day,
        "uptime_last_week": uptime_last_week,
        "downtime_last_week": downtime_last_week
    }

    return report
