# orchestrator.py
from chains import classify_chain, escalate_chain, draft_email_chain
from calculations import execute_compensation

def process_single_exception(customer_name: str, shipment_value: float, report_text: str, is_premium: bool = False) -> dict:
    """
    Orchestrates classification, compensation calculation, tier threshold checks, 
    and routing to escalation or customer email drafting.
    """
    escalation_threshold = 200.0 if is_premium else 500.0
    
    print(f"--- Processing Exception for {customer_name} (Premium: {is_premium}) ---")
    
    # 1. Classify the report
    classification = classify_chain.invoke({"report_text": report_text}).strip().lower()
    print(f"Classification: {classification}")
    
    # 2. Automatically escalate if unknown
    if "unknown" in classification:
        print("-> Reason: Unrecognized exception category. Routing to escalation.")
        escalation_note = escalate_chain.invoke({
            "shipment_value": shipment_value,
            "report_text": report_text
        })
        return {
            "status": "escalated",
            "reason": "unknown_classification",
            "output": escalation_note
        }
        
    # 3. Calculate compensation for known categories
    comp_result = execute_compensation(
        classification=classification,
        shipment_value=shipment_value,
        report_text=report_text
    )
    
    compensation_amount = comp_result.get("compensation_amount", 0.0)
    print(f"Calculated Compensation: ${compensation_amount} ({comp_result.get('rate_applied')} rate)")
    
    # 4. Check if compensation exceeds customer tier threshold
    if compensation_amount > escalation_threshold:
        print(f"-> Reason: Compensation (${compensation_amount}) exceeds threshold (${escalation_threshold}).")
        escalation_note = escalate_chain.invoke({
            "shipment_value": shipment_value,
            "report_text": f"{report_text} [Calculated Comp: ${compensation_amount} exceeds tier threshold]"
        })
        return {
            "status": "escalated",
            "reason": "threshold_exceeded",
            "compensation_details": comp_result,
            "output": escalation_note
        }
        
    # 5. Draft customer-facing email if within limits
    print("-> Status: Approved for automated customer resolution.")
    enriched_report = (
        f"{report_text} | Approved Compensation: ${compensation_amount} "
        f"({comp_result.get('rate_applied')} of shipment value)"
    )
    email_draft = draft_email_chain.invoke({
        "customer_name": customer_name,
        "shipment_value": shipment_value,
        "report_text": enriched_report
    })
    
    return {
        "status": "resolved",
        "compensation_details": comp_result,
        "output": email_draft
    }