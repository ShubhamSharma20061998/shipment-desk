# app.py
import gradio as gr
from session import TriageSession

# Initialize the stateful session manager for the running server instance
session = TriageSession()

def submit_exception(customer_name: str, shipment_value: float, report_text: str, is_premium: bool):
    """
    Processes a single exception through the session and returns formatting updates for the UI.
    """
    if not customer_name.strip() or not report_text.strip():
        return "⚠️ Error", "Please provide both customer name and report text.", format_session_log()
    
    try:
        val = float(shipment_value)
    except ValueError:
        return "⚠️ Error", "Shipment value must be a valid numeric amount.", format_session_log()

    # Run through session & pipeline logic
    result = session.process_report(
        customer_name=customer_name,
        shipment_value=val,
        report_text=report_text,
        is_premium=is_premium
    )
    
    status = result.get("status", "unknown").upper()
    output_content = result.get("output", "No output generated.")
    
    # Format status header with reason if escalated
    if status == "ESCALATED":
        reason = result.get("reason", "threshold/routing check")
        status_display = f"🚨 ESCALATED ({reason})"
    else:
        status_display = "✅ RESOLVED (Automated Customer Email)"

    return status_display, output_content, format_session_log()

def get_daily_summary_metrics():
    """
    Pulls cumulative aggregated metrics from the active session.
    """
    summary = session.get_daily_triage_summary()
    return (
        f"Total Reports Processed  : {summary['total_reports']}\n"
        f"Total Compensation Payout: ${summary['total_compensation']:.2f}\n"
        f"Escalation Rate          : {summary['escalation_rate']}\n"
        f"Costliest Category       : {summary['costliest_category']}"
    )

def format_session_log() -> str:
    """
    Formats the running session history into a readable log.
    """
    if not session.results:
        return "No reports processed in this session yet."
    
    log_lines = []
    for i, r in enumerate(session.results, 1):
        comp = r.get('compensation_details')
        comp_str = f" | Payout: ${comp.get('compensation_amount', 0.0)}" if comp else ""
        status = r.get('status', '').upper()
        reason = r.get('reason', 'automated')
        log_lines.append(f"[{i}] Status: {status}{comp_str} (Reason: {reason})")
    return "\n".join(log_lines)

# --- Gradio UI Layout ---
with gr.Blocks(title="Logistics Exception Triage Desk") as demo:
    gr.Markdown("# 📦 Logistics Exception Triage Desk")
    gr.Markdown("Automated classification, compensation rules, tier thresholds, and real-time session tracking.")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📝 Submit Exception Report")
            name_input = gr.Textbox(label="Customer Name", placeholder="e.g., Alice Smith")
            value_input = gr.Number(label="Shipment Value ($)", value=300.0)
            report_input = gr.Textbox(label="Exception Report Text", placeholder="Describe delay, damage, or loss details...", lines=4)
            premium_input = gr.Checkbox(label="Premium Customer (Lower escalation threshold: $200)", value=False)
            submit_btn = gr.Button("Process Exception", variant="primary")
        
        with gr.Column(scale=1):
            gr.Markdown("### 🔍 Pipeline Outcome & Steps")
            status_output = gr.Textbox(label="Routing Status", interactive=False)
            output_box = gr.Textbox(label="Generated Output (Customer Email or Escalation Note)", lines=8, interactive=False)

    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📋 Running Daily Triage Log")
            log_output = gr.Textbox(label="Session History", lines=6, interactive=False)
        
        with gr.Column(scale=1):
            gr.Markdown("### 📊 Daily Summary Aggregation")
            summary_btn = gr.Button("Pull Daily Summary Metrics", variant="secondary")
            summary_output = gr.Textbox(label="Cumulative Metrics Report", lines=5, interactive=False)

    # Wire up button actions
    submit_btn.click(
        fn=submit_exception,
        inputs=[name_input, value_input, report_input, premium_input],
        outputs=[status_output, output_box, log_output]
    )
    
    summary_btn.click(
        fn=get_daily_summary_metrics,
        inputs=[],
        outputs=[summary_output]
    )

if __name__ == "__main__":
    demo.launch()