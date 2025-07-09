

# main.py
import pandas as pd
from models.baseline_model import linear_price_update
from models.demand_model import calculate_demand, demand_based_price
from models.competitive_model import competitive_price, suggest_rerouting
from visualization.visualization import update_plot, get_layout
from pathway_streaming.simulator import get_stream
from bokeh.io import curdoc

# Initial settings
base_price = 10
previous_price = base_price
model_type = "demand"  # Options: "baseline", "demand", "competitive"

# Load dataset
df = pd.read_csv("data/parking_dynamic_pricing.csv")
step_index = 0
# Simulate streaming loop
def simulate_step():
    global step_index, previous_price
    if step_index >= len(df): return

    row = df.iloc[step_index]
    occupancy = row["Occupancy"]
    capacity = row["Capacity"]
    queue = row["QueueLength"]
    traffic = row["TrafficConditionNearby"]
    special = row["IsSpecialDay"]
    vtype = row["VehicleType"]

    # For competitive model, fake some nearby lots
    nearby = [{'price': 9.5, 'lat': row["Latitude"]+0.001, 'lon': row["Longitude"]+0.001},
              {'price': 10.5, 'lat': row["Latitude"]-0.001, 'lon': row["Longitude"]-0.001}]

    if model_type == "baseline":
        price = linear_price_update(previous_price, occupancy, capacity)
    elif model_type == "demand":
        demand = calculate_demand(occupancy, capacity, queue, traffic, special, vtype)
        price = demand_based_price(base_price, demand)
    else:  # competitive
        price = competitive_price(base_price, occupancy, capacity, nearby)

    previous_price = price
    update_plot(price)
    step_index += 1  # advance to next row


# Bokeh document setup
doc = curdoc()
doc.add_root(get_layout())
doc.add_periodic_callback(simulate_step, 2000)
# Schedule streaming steps every 2 sec
# from bokeh.driving import linear
#
# @linear()
# def stream_step(i):
#     simulate_step(i)
#
# doc.add_periodic_callback(stream_step, 2000)


