from speed_monitor import measure_speed, extract_relevant_data
from db.connector import insert_to_db
from db.models import SpeedMeasurement

if __name__== "__main__":
    res = measure_speed()
    data = extract_relevant_data(res)
    obj = SpeedMeasurement(**data)
    insert_to_db(obj)