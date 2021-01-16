import sys
from speed_monitor import measure_speed, extract_relevant_data
from db.connector import insert_to_db, build_table
from db.models import SpeedMeasurement

class CommandNotValidException(Exception):
    pass


if __name__== "__main__":
    try:
        if sys.argv[1] == 'measure':
            res = measure_speed()
            data = extract_relevant_data(res)
            obj = SpeedMeasurement(**data)
            print("Measured speed: ", obj)
            insert_to_db(obj)
        elif sys.argv[1] == 'build_table':
            build_table()
        else:
            raise CommandNotValidException(f"Command <{sys.argv[1]}> not valid")
    except IndexError:
        print("Please make sure you give an argument and that the argument is valid")