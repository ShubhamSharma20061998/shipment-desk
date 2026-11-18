# tools.py
import re

def calculate_delay_compensation(shipment_value: float, report_text: str) -> dict:
    """Delay compensation: a percentage of shipment value based on the delay duration described in the report."""
    text = report_text.lower()
    
    # Extract days if mentioned (e.g., "4 days late")
    match = re.search(r"(\d+)\s*day", text)
    days = int(match.group(1)) if match else 1
    
    if days >= 5:
        rate = 0.25  # 25% for 5+ days
    elif days >= 3:
        rate = 0.15  # 15% for 3-4 days
    else:
        rate = 0.05  # 5% for 1-2 days
        
    compensation = round(shipment_value * rate, 2)
    return {
        "type": "delay",
        "days_delayed": days,
        "rate_applied": f"{int(rate * 100)}%",
        "compensation_amount": compensation
    }


def calculate_damaged_compensation(shipment_value: float, report_text: str) -> dict:
    """Damaged compensation: a percentage of shipment value based on the severity of damage described in the report."""
    text = report_text.lower()
    
    if any(word in text for word in ["severely", "destroyed", "shattered", "broken", "unusable", "total"]):
        rate = 0.80  # 80% for severe damage
        severity = "severe"
    elif any(word in text for word in ["moderate", "cracked", "dented", "bent"]):
        rate = 0.40  # 40% for moderate damage
        severity = "moderate"
    else:
        rate = 0.15  # 15% for minor/cosmetic damage
        severity = "minor"
        
    compensation = round(shipment_value * rate, 2)
    return {
        "type": "damaged",
        "severity": severity,
        "rate_applied": f"{int(rate * 100)}%",
        "compensation_amount": compensation
    }


def calculate_lost_compensation(shipment_value: float, report_text: str) -> dict:
    """Lost compensation: full or partial reimbursement of shipment value based on the loss circumstances described in the report."""
    text = report_text.lower()
    
    if any(word in text for word in ["stolen", "missing", "unrecoverable", "confirmed lost"]):
        rate = 1.00  # 100% full reimbursement
        status = "confirmed_loss"
    else:
        rate = 0.50  # 50% provisional reimbursement while tracing
        status = "unconfirmed_loss"
        
    compensation = round(shipment_value * rate, 2)
    return {
        "type": "lost",
        "status": status,
        "rate_applied": f"{int(rate * 100)}%",
        "compensation_amount": compensation
    }