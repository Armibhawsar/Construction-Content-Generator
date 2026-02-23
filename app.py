import streamlit as st
from vector_db import build_vector_db, search_vector_db
from llm_engine import generate_report

from fpdf import FPDF
from io import BytesIO
from datetime import datetime

# ------------------ Load Knowledge Base ------------------

with open("data/construction_docs.txt") as f:
    texts = f.readlines()

index, _ = build_vector_db(texts)

# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Construction Content Generator")

st.title("🏗️ Construction Content Generator")
st.write("Generate professional construction site reports using AI")

topic = st.text_input("Enter construction topic:")

# ------------------ PDF Builder (fpdf2) ------------------

def create_pdf(report_text, topic):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Main Title
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Construction Site Report", ln=True, align="C")

    pdf.ln(4)

    # Project + Date
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, f"Project Name: {topic}", ln=True)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%d %B %Y')}", ln=True)

    pdf.ln(6)

    # Known subheadings to bold
    headings = [
        "Overview",
        "Work Executed",
        "Manpower & Machinery",
        "Safety Observations",
        "Issues & Remarks"
    ]

    # Clean markdown **
    report_text = report_text.replace("**", "")

    for line in report_text.split("\n"):

        clean_line = line.strip()

        if not clean_line:
            pdf.ln(2)
            continue

        # If line is a heading
        if clean_line in headings:
            pdf.set_font("Helvetica", "B", 13)
            pdf.cell(0, 9, clean_line, ln=True)
            pdf.ln(1)

        else:
            pdf.set_font("Helvetica", size=11)
            pdf.multi_cell(0, 7, clean_line)

    buffer = BytesIO()
    buffer.write(pdf.output(dest="S").encode("latin1"))
    buffer.seek(0)

    return buffer

# ------------------ Generate & Download ------------------

if st.button("Generate Site Report"):

    context = " ".join(search_vector_db(topic, texts, index))
    report = generate_report(topic, context)

    st.success("✅ Report generated successfully!")

    pdf_file = create_pdf(report, topic)

    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_file,
        file_name="site_report.pdf",
        mime="application/pdf"
    )
