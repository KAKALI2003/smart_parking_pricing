def calculate_demand(occupancy, capacity, queue_length, traffic, is_special_day, vehicle_type, alpha=0.4, beta=0.3, gamma=0.2, delta=0.3, epsilon=0.2):
    """
        Calculates a linear demand score using weighted features.

        Parameters:
            occupancy (int): Number of parked vehicles
            capacity (int): Total lot capacity
            queue_length (int): Number of vehicles waiting
            traffic (float): Traffic congestion
            is_special_day (int): 1 if special day, 0 otherwise
            vehicle_type (str): Type of vehicle ('car', 'bike', 'truck')

        Returns:
            float: Raw demand score (not yet normalized)
        """

    # Assign weights to vehicle types
    vehicle_weights = {
        "cycle": 0.3,
        "bike": 0.5,
        "car": 1.0,
        "truck": 1.5
    }

    # Assign traffic level
    traffic_levels = {
        "low": 1.0,
        "average": 2.0,
        "high": 3.0
    }
    vehicle_weight = vehicle_weights.get(vehicle_type.lower(), 1.0)
    traffic_levels = traffic_levels.get(vehicle_type.lower(), 1.0)

    occupancy_ratio = occupancy / capacity if capacity > 0 else 0

    demand = (alpha * occupancy_ratio +
              beta * queue_length -
              gamma * traffic_levels +
              delta * is_special_day +
              epsilon * vehicle_weight)
    return demand


def demand_based_price(base_price, demand, lambda_ = 0.5):
    """
        Adjusts the price using a normalized demand score.

        Parameters:
            base_price (float): Default price ($10)
            demand (float): Raw demand score
            lambda_ (float): Controls how aggressively price reacts to demand

        Returns:
            float: Adjusted price, clipped between 0.5x and 2x base price
        """

    # Normalized demand (assume max possible raw demand is around 10 for scaling)
    norm_demand = max(0, min(demand / 10, 1))

    adjusted_price = base_price * ( 1 + lambda_ * norm_demand)

    # Clip the price to stay within 0.5x and 2x range
    clipped_price = max(0.5 * base_price, min(2 * base_price, adjusted_price))

    return round(clipped_price, 2)


