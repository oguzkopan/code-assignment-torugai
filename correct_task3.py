# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    """
    Calculate the average of valid measurements, ignoring None values.
    
    Args:
        values: List of numeric values (may contain None)
        
    Returns:
        float: Average of non-None values, or 0 if no valid values
    """
    if not values:
        return 0
    
    total = 0
    count = 0
    
    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (ValueError, TypeError):
                # Skip values that cannot be converted to float
                continue
    
    return total / count if count > 0 else 0
