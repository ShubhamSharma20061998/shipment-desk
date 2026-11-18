# pipeline.py
from orchestrator import process_single_exception

def run_exception_pipeline(customer_name: str, shipment_value: float, report_text: str, is_premium: bool = False) -> dict:
    """
    Pipeline entry point: Calls the orchestrator and returns the final execution output.
    """
    return process_single_exception(
        customer_name=customer_name,
        shipment_value=shipment_value,
        report_text=report_text,
        is_premium=is_premium
    )