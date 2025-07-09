import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def Haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371     # Earth radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])  # convert degree to radian
    dis_lat, dis_lon = lat2 - lat1, lon2 - lon1
    a = sin(dis_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dis_lon / 2) ** 2
    return 2 * R * asin(sqrt(a))


def get_nearby_lots(my_lat, my_lon, all_lots, radius_km = 0.5 ):
    nearby_lots = []
    for lot in all_lots:

        distance = Haversine_distance(my_lat, my_lon, lot["lat"], lot["lon"])
        if distance <= radius_km:
            nearby_lots.append(lot)
    return nearby_lots




def competitive_price(base_price, occupancy, capacity, nearby_lots, alpha=0.4, beta=0.2):
    """
        Compute new price based on occupancy and competitor prices.

        Parameters:
            base_price (float): Starting price (e.g., $10)
            occupancy (int): Current vehicles parked
            capacity (int): Max capacity
            nearby_lots (list): List of dicts with info on nearby lots:
                [
                  {'price': 9.5, 'lat': 18.52, 'lon': 73.84},
                  ...
                ]
            alpha (float): How much to scale based on your occupancy
            beta (float): How much to scale based on average competitor price

        Returns:
            float: Updated price, smoothed and clipped
        """

    if capacity == 0:
        return base_price

    occupancy_ratio = occupancy / capacity

    if nearby_lots:
        avg_nearby_price = sum([lot['price'] for lot in nearby_lots]) / len(nearby_lots)
    else:
        avg_nearby_price = base_price  # fallback

    new_price = base_price * (1 + alpha * occupancy_ratio) + beta * (base_price - avg_nearby_price)

    # Clip price to stay within 0.5x – 2x base range
    return round(min(max(new_price, 0.5 * base_price), 2 * base_price), 2)


def suggest_rerouting(occupancy, capacity, nearby_lots):
    """
    Return True if occupancy is full and cheaper nearby lots exist.
    """
    if occupancy < capacity:
        return False
    for lot in nearby_lots:
        if lot['price'] < 10:  # your base price
            return True
    return False


