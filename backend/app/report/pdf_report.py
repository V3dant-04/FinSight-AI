from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_pdf_report(filepath, report_data):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filepath, pagesize=A4)

    elements = []

    elements.append(Paragraph("<b>FinSight AI – Monthly Report</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Total Expenses: {report_data['total_expenses']}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Category Breakdown</b>", styles["Heading2"]))
    for cat, amt in report_data["category_breakdown"].items():
        elements.append(Paragraph(f"{cat}: {amt}", styles["Normal"]))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Forecast</b>", styles["Heading2"]))
    elements.append(Paragraph(str(report_data["forecast_next_period"]), styles["Normal"]))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Insights</b>", styles["Heading2"]))
    for ins in report_data["key_insights"]:
        elements.append(Paragraph(ins, styles["Normal"]))

    doc.build(elements)
