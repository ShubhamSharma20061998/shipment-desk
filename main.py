# main.py
from pipeline import run_exception_pipeline, run_daily_metrics_pipeline

def run_logistics_pipeline_demos():
    print("==================================================")
    print("🚀 STARTING LOGISTICS EXCEPTION PIPELINE & SUMMARY")
    print("==================================================\n")

    pipeline_results = []

    # --- Scenario 1 ---
    res_1 = run_exception_pipeline(
        customer_name="Alice Smith",
        shipment_value=300.0,
        report_text="The package arrived with a moderately cracked outer casing.",
        is_premium=False
    )
    pipeline_results.append(res_1)
    print("=" * 60)

    # --- Scenario 2 ---
    res_2 = run_exception_pipeline(
        customer_name="Bob Jones",
        shipment_value=350.0,
        report_text="The package arrived with a severely shattered screen and broken casing.",
        is_premium=True
    )
    pipeline_results.append(res_2)
    print("=" * 60)

    # --- Scenario 3 ---
    res_3 = run_exception_pipeline(
        customer_name="Charlie Davis",
        shipment_value=1200.0,
        report_text="Customs hold at international port due to missing hazmat classification documents.",
        is_premium=False
    )
    pipeline_results.append(res_3)
    print("=" * 60)

    # --- Scenario 4 ---
    res_4 = run_exception_pipeline(
        customer_name="Diana Prince",
        shipment_value=150.0,
        report_text="The shipment is running 4 days late due to carrier backlog.",
        is_premium=False
    )
    pipeline_results.append(res_4)
    print("=" * 60)

    # --- Generate Daily Summary ---
    summary = run_daily_metrics_pipeline(pipeline_results)
    
    print("\n📊 DAILY OPERATIONS SUMMARY REPORT")
    print("--------------------------------------------------")
    print(f"Total Reports Processed : {summary['total_reports']}")
    print(f"Total Compensation Payout: ${summary['total_compensation']}")
    print(f"Escalation Rate         : {summary['escalation_rate']}")
    print(f"Costliest Category      : {summary['costliest_category']}")
    print("==================================================")

if __name__ == "__main__":
    run_logistics_pipeline_demos()