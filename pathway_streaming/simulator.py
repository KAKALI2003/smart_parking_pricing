
## pathway_streaming

import pathway as pw
import pandas as pd

class ParkingStreamSchema(pw.Schema):
    ID: int
    SystemCodeNumber: str
    Capacity: int
    Latitude: float
    Longitude: float
    Occupancy: int
    VehicleType: str
    TrafficConditionNearby: str
    QueueLength: int
    IsSpecialDay: int
    LastUpdatedDate: str
    LastUpdatedTime: str


def get_stream(csv_path):
    return pw.io.csv.read(
        csv_path,
        schema=ParkingStreamSchema,
        mode="streaming",
        autocommit_duration_ms=2000,  # every 2 sec a new row

    )
