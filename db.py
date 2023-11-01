import psycopg2

def connect_to_db():
    return psycopg2.connect(
        dbname='restaurant_reports',
        user='your_username',
        password='your_password',
        host='localhost'
    )

def fetch_historical_data(store_id, start_time, end_time):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp_utc, status 
        FROM store_status 
        WHERE store_id = %s 
            AND timestamp_utc >= %s 
            AND timestamp_utc <= %s
        """, (store_id, start_time, end_time))
    historical_data = cursor.fetchall()
    conn.close()
    return historical_data
