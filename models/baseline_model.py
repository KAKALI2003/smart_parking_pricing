def linear_price_update(prev_price, occupancy, capacity, alpha = 0.1 ):
    """
        Computes the next price based on current occupancy using a linear formula.

        Args:
            prev_price (float): The previous price of the parking lot.
            occupancy (int or float): Number of currently parked vehicles.
            capacity (int): Total parking capacity of the lot.
            alpha (float): Slope coefficient that controls how sensitively price responds to occupancy.

        Returns:
            float: Updated parking price.
        """

    occupancy_ratio = occupancy / capacity if capacity > 0 else 0
    next_price = prev_price + alpha * occupancy_ratio
    return round(next_price, 2)

