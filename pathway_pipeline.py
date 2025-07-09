import pathway as pw
from models.baseline_model import linear_price_update

@pw.udf
def baseline_pricing(prev_price: float, occupancy: int, capacity: int) -> float:
    return linear_price_update(prev_price, occupancy, capacity)

#def demand_pricing