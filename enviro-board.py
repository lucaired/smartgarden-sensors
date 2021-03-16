import os
import time
import json

from coral.enviro.board import EnviroBoard
from dotenv import load_dotenv
from influxdb import InfluxDBClient

def main():
    enviro = EnviroBoard()
    load_dotenv()
    client = InfluxDBClient(
        os.getenv("HOST"),
        os.getenv("PORT"),
    )
    client.switch_database(os.getenv("DBNAME"))
    location = "window"
    interval = 1 

    try:
        while True:
            iso = time.ctime()
            json_body = [
                {
                    "measurement": "temperature",
                        "tags": {
                            "sensor": "coral-enviro-temperature",
                            "location": location,
                            "unit": "celsius",
                        },
                        "time": iso,
                        "fields": {
                            "value": enviro.temperature
                        }
                },
                {
                    "measurement": "humidity",
                    "tags": {
                        "sensor": "coral-enviro-humidity",
                        "location": location,
                        "unit": "percentage",
                    },
                    "time": iso,
                    "fields": {
                        "value": enviro.humidity
                    }
                },
                {
                    "measurement": "ambient_light",
                    "tags": {
                        "sensor": "coral-enviro-ambient-light",
                        "location": location,
                        "unit": "lux"
                    },
                    "time": iso,
                    "fields": {
                        "value": enviro.ambient_light
                    }
                },
                {
                    "measurement": "pressure",
                    "tags": {
                        "sensor": "coral-enviro-pressure",
                        "location": location,
                        "unit": "kPa"
                    },
                    "time": iso,
                    "fields": {
                        "value": enviro.pressure
                    }
                }
            ]

            client.write_points(json_body)
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print('interrupted!')
        client.close()

if __name__ == '__main__':
    main()