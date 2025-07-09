## Dynamic Pricing for Urban Parking Lots

- Capstone Project — **Summer Analytics 2025**  
- Hosted by: Consulting & Analytics Club × Pathway  
- Built using: Python · Pandas · NumPy · Pathway · Bokeh

---

##  Objective

Urban parking lots are high-demand, limited-capacity spaces. Static pricing leads to under- or over-utilization. This project builds an **intelligent dynamic pricing engine** for 14 real-world parking spaces using:

- Real-time demand simulation
- Queue length, occupancy, traffic, vehicle type
- Competitor pricing (via location proximity)
- Real-time visualization

---

##  Features

-  Real-time data streaming with **Pathway**
-  Live interactive visualization with **Bokeh**
- 3 layered pricing logic:
  - Linear Model
  - Demand-based Model
  - Competitive Pricing Model
-  Clean modular repo structure
-  Base price: $10, bounded dynamic changes (0.5x–2x)

---

##  Models

###  Model 1: Linear Pricing
- Price increases with occupancy.

- Priceₜ₊₁ = Priceₜ + α · (Occupancy / Capacity)

---

### Model 2: Demand-Based Pricing
Factors in:
- Occupancy
- Queue Length
- Traffic Congestion
- Special Days
- Vehicle Type

- Demand = α·(Occupancy/Capacity) + β·QueueLength − γ·Traffic + δ·IsSpecialDay + ε·VehicleTypeWeight
- Price = BasePrice × (1 + λ × NormalizedDemand)

---

###  Model 3: Competitive Pricing
Adds:
- Nearby lot detection via lat-long
- Competitor price comparison
- Rerouting suggestions when needed

---

##  Real-Time Streaming

- Simulates real-time incoming parking data using **Pathway**
- Reads from historical CSV with controlled delay
- Emits time-ordered data rows to the pricing engine

```python
pw.io.csv.read(csv_path, mode="streaming", autocommit_duration_ms=2000)


## Real-Time Visualization

- Bokeh-powered live plot
- Y-axis: parking price
- X-axis: real-time timestamps
- Updates every 2 seconds




