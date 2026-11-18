# calculations.py
from tools import (
    calculate_delay_compensation,
    calculate_damaged_compensation,
    calculate_lost_compensation
)

def execute_compensation(classification: str, shipment_value: float, report_text: str):
    """
    Routes the shipment exception report to the appropriate calculation tool 
    based on the category returned by the classification chain.
    """
    category = classification.strip().lower()
    
    if "delay" in category:
        print("-> Routing to: calculate_delay_compensation")
        return calculate_delay_compensation(
            shipment_value=shipment_value, 
            report_text=report_text
        )
        
    elif "damag" in category:
        print("-> Routing to: calculate_damaged_compensation")
        return calculate_damaged_compensation(
            shipment_value=shipment_value, 
            report_text=report_text
        )
        
    elif "lost" in category:
        print("-> Routing to: calculate_lost_compensation")
        return calculate_lost_compensation(
            shipment_value=shipment_value, 
            report_text=report_text
        )
        
    else:
        print(f"-> Unrecognized or 'unknown' category: '{category}'. Skipping automated compensation.")
        return None