from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from pathlib import Path

# Locate the text audit report
input_file = Path("reports/email_audit_report.txt")

# PDF output location
output_file = Path("reports/email_audit_report.pdf")

# Check whether the text report exists
if not input_file.exists():
    print("Audit report not found. Run email_analyzer.py first.")
else:
    # Read the report
    report_text = input_file.read_text(encoding="utf-8")

    # Create PDF document
    pdf = SimpleDocTemplate(
        str(output_file),
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    content = []

    # Add report text line by line
    for line in report_text.splitlines():
        if line.strip():
            paragraph = Paragraph(
                line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"),
                styles["Normal"]
            )
            content.append(paragraph)
        else:
            content.append(Spacer(1, 10))

    # Generate PDF
    pdf.build(content)

    print("PDF report generated successfully!")
    print("PDF location:", output_file)