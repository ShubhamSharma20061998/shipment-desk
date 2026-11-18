# triage_check.py
from session import TriageSession

def run_triage_validation():
    print("==================================================")
    print("🧪 RUNNING TRIAGE VALIDATION CHECK SUITE")
    print("==================================================\n")

    session = TriageSession()

    # --- Test 1: Mild Delay (Expected: Resolved with email) ---
    print("Test 1: Mild Delay Report")
    res_1 = session.process_report(
        customer_name="Alice Miller",
        shipment_value=150.0,
        report_text="The package is running 1 day late due to minor weather.",
        is_premium=False
    )
    print(f"-> Status: {res_1['status'].upper()} (Expected: RESOLVED)\n")

    # --- Test 2: High-Value Loss (Expected: Escalated due to threshold/payout rules) ---
    print("Test 2: High-Value Loss Report")
    res_2 = session.process_report(
        customer_name="Bridget Vance",
        shipment_value=1500.0,
        report_text="The package has been confirmed lost and stolen in transit.",
        is_premium=False
    )
    print(f"-> Status: {res_2['status'].upper()} (Expected: ESCALATED)\n")

    # --- Test 3: Minor Damage Claim (Expected: Resolved with small email payout) ---
    print("Test 3: Minor Damage Claim")
    res_3 = session.process_report(
        customer_name="Chris Paul",
        shipment_value=200.0,
        report_text="The package arrived with a minor scratch and small dent.",
        is_premium=False
    )
    print(f"-> Status: {res_3['status'].upper()} (Expected: RESOLVED)\n")

    # --- Test 4: Garbled Unclassifiable Report (Expected: Auto-escalated regardless of value) ---
    print("Test 4: Garbled Unclassifiable Report")
    res_4 = session.process_report(
        customer_name="David Lee",
        shipment_value=50.0,
        report_text="asdfghjkl qwertyuiop zxcvbnm garbage input data test 12345.",
        is_premium=False
    )
    print(f"-> Status: {res_4['status'].upper()} (Expected: ESCALATED - Unknown category)\n")

    print("=" * 50)
    print("📊 SESSION DAILY TRIAGE SUMMARY AGGREGATION")
    print("=" * 50)
    summary = session.get_daily_triage_summary()
    print(f"Total Reports Processed : {summary['total_reports']}")
    print(f"Total Compensation Payout: ${summary['total_compensation']}")
    print(f"Escalation Rate         : {summary['escalation_rate']}")
    print(f"Costliest Category      : {summary['costliest_category']}")
    print("==================================================")

if __name__ == "__main__":
    run_triage_validation()