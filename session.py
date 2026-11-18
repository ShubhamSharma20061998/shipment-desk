# session.py

class TriageSession:
    def __init__(self):
        self.results = []

    def process_report(self, customer_name: str, shipment_value: float, report_text: str, is_premium: bool = False) -> dict:
        """
        Imports and runs the pipeline, recording the outcome into the session state.
        """
        from pipeline import run_exception_pipeline
        
        result = run_exception_pipeline(
            customer_name=customer_name,
            shipment_value=shipment_value,
            report_text=report_text,
            is_premium=is_premium
        )
        self.results.append(result)
        return result

    def get_daily_triage_summary(self) -> dict:
        """
        Aggregates session data with real calculations:
        - Total compensation paid across all resolved reports.
        - Escalation rate percentage.
        - Costliest category by cumulative total compensation.
        """
        total_reports = len(self.results)
        if total_reports == 0:
            return {
                "total_reports": 0,
                "total_compensation": 0.0,
                "escalation_rate": "0.0%",
                "costliest_category": "None"
            }

        total_compensation = 0.0
        escalated_count = 0
        # Tracks cumulative spending per category to properly weigh high-volume small payouts vs single large ones
        category_costs = {"delay": 0.0, "damaged": 0.0, "lost": 0.0}

        for res in self.results:
            if res.get("status") == "escalated":
                escalated_count += 1
                
            comp_details = res.get("compensation_details")
            if comp_details:
                amount = comp_details.get("compensation_amount", 0.0)
                comp_type = comp_details.get("type", "").lower()
                
                total_compensation += amount
                if comp_type in category_costs:
                    category_costs[comp_type] += amount

        escalation_rate = (escalated_count / total_reports) * 100

        # Determine costliest category by cumulative total compensation
        costliest_type = max(category_costs, key=category_costs.get)
        max_cost = category_costs[costliest_type]
        
        if max_cost == 0.0:
            costliest_display = "None (No automated payouts)"
        else:
            costliest_display = f"{costliest_type.capitalize()} (${max_cost:.2f})"

        return {
            "total_reports": total_reports,
            "total_compensation": round(total_compensation, 2),
            "escalation_rate": f"{escalation_rate:.1f}%",
            "costliest_category": costliest_display
        }