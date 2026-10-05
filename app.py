import streamlit as st
import plotly.express as px
import pandas as pd

from src.questions import QUESTIONS
from src.risk_engine import calculate_risk
from src.recommendations import (
    detect_weaknesses,
    generate_recommendations
)
from src.validators import validate_assessment
from src.report_generator import generate_pdf_report


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Social Media Privacy Risk Assessment",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f4f7fb;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #5f6b7a;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        color: #172033;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .info-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    .risk-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 20px;
    }

    .risk-score {
        font-size: 52px;
        font-weight: 800;
        color: #172033;
    }

    .risk-level {
        font-size: 25px;
        font-weight: 700;
        margin-top: 5px;
    }

    .weakness-card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #e67e22;
        margin-bottom: 12px;
    }

    .recommendation-card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #2e86de;
        margin-bottom: 12px;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 14px;
        margin-top: 40px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🛡️ Social Media Privacy Risk Assessment'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Defensive cybersecurity framework for evaluating '
    'social-media privacy exposure'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PRIVACY DISCLAIMER
# ============================================================

st.info(
    "🔐 Privacy Notice: This assessment uses only voluntarily "
    "entered demo information. It does not scrape social-media "
    "profiles, access private accounts, track individuals, or "
    "bypass privacy controls."
)


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.markdown(
    '<div class="info-card">'
    '<b>🎯 Purpose</b><br>'
    'This tool evaluates common social-media privacy and security '
    'practices and calculates an educational Privacy Risk Score '
    'from 0 to 100.'
    '<br><br>'
    '<b>📌 Important:</b> A higher score indicates greater potential '
    'privacy exposure. It does not guarantee that an account will '
    'or will not be compromised.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ASSESSMENT SECTION
# ============================================================

st.markdown(
    '<div class="section-title">📝 Privacy Assessment</div>',
    unsafe_allow_html=True
)

st.write(
    "Answer all questions based on your current privacy "
    "and security practices."
)


answers = {}


# ============================================================
# QUESTIONS FORM
# ============================================================

with st.form("privacy_assessment_form"):

    for index, question in enumerate(QUESTIONS):

        st.markdown(
            f"### {index + 1}. {question['question']}"
        )

        selected_answer = st.radio(
            "Select one option:",
            list(question["options"].keys()),
            key=question["id"]
        )

        answers[question["id"]] = selected_answer

        st.divider()

    submitted = st.form_submit_button(
        "🔍 Assess Privacy Risk",
        width="stretch"
    )


# ============================================================
# PROCESS ASSESSMENT
# ============================================================

if submitted:

    try:

        # Validate answers
        validate_assessment(answers)

        # Calculate risk
        result = calculate_risk(
            QUESTIONS,
            answers
        )

        # Detect weaknesses
        weaknesses = detect_weaknesses(
            QUESTIONS,
            answers
        )

        # Generate recommendations
        recommendations = generate_recommendations(
            weaknesses
        )

    except ValueError as error:

        st.error(
            f"❌ Assessment validation error: {error}"
        )

    else:

        # ====================================================
        # RESULTS HEADER
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📊 Privacy Risk Assessment Results'
            '</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # SCORE INFORMATION
        # ====================================================

        score = result["overall_score"]
        risk_level = result["risk_level"]


        col1, col2, col3 = st.columns(3)


        with col1:

            st.markdown(
                f"""
                <div class="risk-card">
                    <div>🔢 Privacy Risk Score</div>
                    <div class="risk-score">{score}/100</div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            if risk_level == "LOW":
                risk_symbol = "🟢"

            elif risk_level == "MODERATE":
                risk_symbol = "🟡"

            elif risk_level == "HIGH":
                risk_symbol = "🟠"

            else:
                risk_symbol = "🔴"


            st.markdown(
                f"""
                <div class="risk-card">
                    <div>🚦 Risk Level</div>
                    <div class="risk-level">
                        {risk_symbol} {risk_level}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                f"""
                <div class="risk-card">
                    <div>⚠️ Weaknesses Detected</div>
                    <div class="risk-score">
                        {len(weaknesses)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # RISK MESSAGE
        # ====================================================

        if risk_level == "LOW":

            st.success(
                "🟢 Low privacy risk. Your current practices "
                "show relatively strong privacy protection."
            )

        elif risk_level == "MODERATE":

            st.warning(
                "🟡 Moderate privacy risk. Some privacy settings "
                "and security practices should be improved."
            )

        elif risk_level == "HIGH":

            st.warning(
                "🟠 High privacy risk. Several privacy or security "
                "areas require attention."
            )

        else:

            st.error(
                "🔴 Critical privacy risk. Immediate improvements "
                "to privacy and account-security practices "
                "are recommended."
            )


        # ====================================================
        # OVERALL RISK PROGRESS
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📈 Overall Risk Level'
            '</div>',
            unsafe_allow_html=True
        )

        st.progress(
            min(score / 100, 1.0)
        )

        st.caption(
            f"Privacy Risk Score: {score} / 100"
        )


        # ====================================================
        # CATEGORY-WISE RISK
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📊 Category-wise Risk Analysis'
            '</div>',
            unsafe_allow_html=True
        )

        category_scores = result["category_scores"]


        category_df = pd.DataFrame(
            {
                "Category": list(category_scores.keys()),
                "Risk Score": list(category_scores.values())
            }
        )


        category_df = category_df.sort_values(
            by="Risk Score",
            ascending=False
        )


        fig_category = px.bar(
            category_df,
            x="Risk Score",
            y="Category",
            orientation="h",
            range_x=[0, 100],
            title="Privacy Risk by Category",
            labels={
                "Risk Score": "Risk Score (0–100)",
                "Category": "Privacy Category"
            }
        )


        fig_category.update_layout(
            height=550,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )


        st.plotly_chart(
            fig_category,
            width="stretch"
        )


        # ====================================================
        # WEAKNESSES
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '⚠️ Detected Privacy Weaknesses'
            '</div>',
            unsafe_allow_html=True
        )


        if weaknesses:

            for weakness in weaknesses:

                st.markdown(
                    f"""
                    <div class="weakness-card">
                        <b>⚠️ {weakness['category']}</b>
                        <br><br>
                        <b>Issue:</b> {weakness['question']}
                        <br>
                        <b>Selected Answer:</b>
                        {weakness['answer']}
                        <br>
                        <b>Risk Points:</b>
                        {weakness['risk_score']}/5
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "✅ No high-risk privacy weaknesses were detected."
            )


        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '🛠️ Personalized Recommendations'
            '</div>',
            unsafe_allow_html=True
        )


        if recommendations:

            for recommendation in recommendations:

                st.markdown(
                    f"""
                    <div class="recommendation-card">
                        <b>🔐 {recommendation['category']}</b>
                        <br><br>
                        {recommendation['recommendation']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "✅ No immediate recommendations were generated."
            )


        # ====================================================
        # PRIVACY CHECKLIST
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '✅ Privacy Protection Checklist'
            '</div>',
            unsafe_allow_html=True
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


        for index, item in enumerate(checklist):

            st.checkbox(
                item,
                value=False,
                key=f"checklist_{index}"
            )


        # ====================================================
        # EDUCATIONAL NOTICE
        # ====================================================

        st.markdown(
            '<div class="info-card">'
            '<b>🎓 Educational Security Notice</b>'
            '<br><br>'
            'This framework is designed for cybersecurity education, '
            'privacy awareness, and defensive risk assessment. '
            'The calculated score is an indicator of potential exposure '
            'based on the selected answers and should not be interpreted '
            'as a prediction of an actual security incident.'
            '</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # PDF REPORT
        # ====================================================

        st.markdown(
            '<div class="section-title">'
            '📄 Privacy Risk Assessment Report'
            '</div>',
            unsafe_allow_html=True
        )


        pdf_report = generate_pdf_report(
            overall_score=score,
            risk_level=risk_level,
            category_scores=category_scores,
            weaknesses=weaknesses,
            recommendations=recommendations
        )


        st.download_button(
            label="📄 Download Privacy Risk Report",
            data=pdf_report,
            file_name="privacy_risk_assessment_report.pdf",
            mime="application/pdf",
            width="stretch"
        )


# ============================================================
# SYNTHETIC DATA DASHBOARD
# ============================================================

st.markdown(
    '<div class="section-title">'
    '📊 Synthetic Privacy Risk Dashboard'
    '</div>',
    unsafe_allow_html=True
)


st.write(
    "The following dashboard uses fictional synthetic profiles only. "
    "No real social-media users or accounts are represented."
)


# ============================================================
# LOAD SYNTHETIC DATA
# ============================================================

demo_data = pd.read_csv(
    "data/demo_profiles.csv"
)


# ============================================================
# SYNTHETIC DATA SUMMARY
# ============================================================

total_profiles = len(demo_data)

average_score = round(
    demo_data["risk_score"].mean(),
    2
)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "👥 Synthetic Profiles",
        total_profiles
    )


with col2:

    st.metric(
        "📊 Average Risk Score",
        average_score
    )


# ============================================================
# RISK DISTRIBUTION
# ============================================================

risk_distribution = (
    demo_data["risk_level"]
    .value_counts()
    .reindex(
        ["LOW", "MODERATE", "HIGH", "CRITICAL"],
        fill_value=0
    )
    .reset_index()
)


risk_distribution.columns = [
    "Risk Level",
    "Profiles"
]


fig_distribution = px.bar(
    risk_distribution,
    x="Risk Level",
    y="Profiles",
    title="Synthetic Profile Risk Distribution",
    labels={
        "Profiles": "Number of Profiles",
        "Risk Level": "Risk Level"
    }
)


fig_distribution.update_layout(
    height=400
)


st.plotly_chart(
    fig_distribution,
    width="stretch"
)


# ============================================================
# RISK SCORE DISTRIBUTION
# ============================================================

fig_scores = px.histogram(
    demo_data,
    x="risk_score",
    nbins=10,
    title="Synthetic Privacy Risk Score Distribution",
    labels={
        "risk_score": "Privacy Risk Score"
    }
)


fig_scores.update_layout(
    height=400
)


st.plotly_chart(
    fig_scores,
    width="stretch"
)


# ============================================================
# SYNTHETIC DATA TABLE
# ============================================================

st.markdown(
    "### 📋 Synthetic Profile Dataset"
)


st.dataframe(
    demo_data,
    width="stretch"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🛡️ Social Media Privacy Risk Assessment Framework
        <br>
        Defensive Cybersecurity & Privacy Awareness Project
        <br><br>
        Built for educational and security-awareness purposes.
    </div>
    """,
    unsafe_allow_html=True
)
if __name__ == "__main__":
    import os

    app.run(
        debug=False,
        host="0.0.0.0",

port=int(os.environ.get("PORT",5000))

    )