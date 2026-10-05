from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


def generate_pdf_report(
    overall_score,
    risk_level,
    category_scores,
    weaknesses,
    recommendations
):
    """
    Generate a professional Privacy Risk Assessment PDF report.

    Returns:
        BytesIO object containing the generated PDF.
    """

    # --------------------------------------------------------
    # Create PDF in memory
    # --------------------------------------------------------

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    # --------------------------------------------------------
    # Styles
    # --------------------------------------------------------

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        leading=28,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=11,
        leading=16,
        textColor=colors.grey,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=15,
        leading=20,
        spaceBefore=12,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalText",
        parent=styles["Normal"],
        fontSize=10,
        leading=15,
        spaceAfter=6
    )

    small_style = ParagraphStyle(
        "SmallText",
        parent=styles["Normal"],
        fontSize=8,
        leading=11
    )

    # --------------------------------------------------------
    # PDF content container
    # --------------------------------------------------------

    story = []

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Social Media Privacy Risk Assessment",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Defensive Cybersecurity & Privacy Awareness Report",
            subtitle_style
        )
    )

    # --------------------------------------------------------
    # Assessment Summary
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Assessment Summary",
            heading_style
        )
    )

    summary_data = [
        ["Assessment Metric", "Result"],
        ["Privacy Risk Score", f"{overall_score} / 100"],
        ["Risk Level", risk_level],
        ["Detected Weaknesses", str(len(weaknesses))]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[80 * mm, 80 * mm]
    )

    summary_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#172033")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.whitesmoke
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ]
        )
    )

    story.append(summary_table)

    story.append(Spacer(1, 12))

    # --------------------------------------------------------
    # Risk Interpretation
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Risk Interpretation",
            heading_style
        )
    )

    if risk_level == "LOW":

        interpretation = (
            "The assessment indicates relatively low privacy exposure. "
            "Continue reviewing privacy settings regularly and maintain "
            "strong account-security practices."
        )

    elif risk_level == "MODERATE":

        interpretation = (
            "The assessment indicates moderate privacy exposure. "
            "Several privacy and security practices should be reviewed "
            "and improved."
        )

    elif risk_level == "HIGH":

        interpretation = (
            "The assessment indicates high potential privacy exposure. "
            "Important privacy settings and account-security practices "
            "should be improved."
        )

    else:

        interpretation = (
            "The assessment indicates critical potential privacy exposure. "
            "Immediate attention to privacy settings and account-security "
            "practices is recommended."
        )

    story.append(
        Paragraph(
            interpretation,
            normal_style
        )
    )

    # --------------------------------------------------------
    # Category-wise Risk
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Category-wise Risk Analysis",
            heading_style
        )
    )

    category_data = [
        ["Privacy Category", "Risk Score"]
    ]

    for category, score in category_scores.items():

        category_data.append(
            [
                category,
                f"{score:.2f} / 100"
            ]
        )

    category_table = Table(
        category_data,
        colWidths=[100 * mm, 60 * mm]
    )

    category_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#172033")
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ]
        )
    )

    story.append(category_table)

    # --------------------------------------------------------
    # Page Break
    # --------------------------------------------------------

    story.append(
        PageBreak()
    )

    # --------------------------------------------------------
    # Detected Weaknesses
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Detected Privacy Weaknesses",
            heading_style
        )
    )

    if weaknesses:

        for number, weakness in enumerate(
            weaknesses,
            start=1
        ):

            story.append(
                Paragraph(
                    f"<b>{number}. {weakness['category']}</b>",
                    normal_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Issue:</b> "
                    f"{weakness['question']}",
                    normal_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Selected Answer:</b> "
                    f"{weakness['answer']}",
                    normal_style
                )
            )

            story.append(
                Paragraph(
                    f"<b>Risk Points:</b> "
                    f"{weakness['risk_score']} / 5",
                    normal_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

    else:

        story.append(
            Paragraph(
                "No high-risk privacy weaknesses were detected.",
                normal_style
            )
        )

    # --------------------------------------------------------
    # Recommendations
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Personalized Security Recommendations",
            heading_style
        )
    )

    if recommendations:

        for number, recommendation in enumerate(
            recommendations,
            start=1
        ):

            story.append(
                Paragraph(
                    f"<b>{number}. "
                    f"{recommendation['category']}</b>",
                    normal_style
                )
            )

            story.append
            Paragraph(
                    recommendation["recommendation"],
                    normal_style
                )

    else:

        story.append(
            Paragraph(
                "No immediate recommendations were generated.",
                normal_style
            )
        )

    # --------------------------------------------------------
    # Privacy Checklist
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "Privacy Protection Checklist",
            heading_style
        )
    )

    checklist = [
        "Keep profile visibility restricted when possible.",
        "Avoid publicly sharing unnecessary personal information.",
        "Do not publicly expose personal contact information.",
        "Avoid publicly sharing current or regular locations.",
        "Use strong and unique passwords.",
        "Enable multi-factor authentication (MFA).",
        "Review connected third-party applications.",
        "Review follower and connection requests.",
        "Restrict tagging and mention permissions.",
        "Review older posts periodically.",
        "Be cautious with unexpected messages and links.",
        "Review privacy settings regularly."
    ]

    for item in checklist:

        story.append(
            Paragraph(
                f"☐ {item}",
                normal_style
            )
        )

    # --------------------------------------------------------
    # Disclaimer
    # --------------------------------------------------------

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Important Educational Disclaimer",
            heading_style
        )
    )

    disclaimer = (
        "This report is generated by an educational defensive "
        "cybersecurity framework. The assessment is based only on "
        "the answers provided by the user. The Privacy Risk Score "
        "is an indicator of potential privacy exposure and does not "
        "guarantee that an account will or will not be compromised. "
        "This project does not scrape social-media profiles, access "
        "private accounts, enumerate users, bypass privacy controls, "
        "or track real individuals."
    )

    story.append(
        Paragraph(
            disclaimer,
            small_style
        )
    )

    # --------------------------------------------------------
    # Build PDF
    # --------------------------------------------------------

    document.build(story)

    buffer.seek(0)

    return buffer