# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    """
    Calculate the average order value excluding cancelled orders.
    
    Args:
        orders: List of order dictionaries with 'status' and 'amount' keys
        
    Returns:
        float: Average order value, or 0 if no valid orders
    """
    if not orders:
        return 0
    
    total = 0
    count = 0
    
    for order in orders:
        if order.get("status") != "cancelled":
            total += order.get("amount", 0)
            count += 1
    
    return total / count if count > 0 else 0
