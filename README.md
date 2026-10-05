# 🛡️ Social Media Privacy Risk Assessment Framework

A defensive cybersecurity and privacy-awareness platform that evaluates
social-media privacy exposure using voluntarily entered assessment data.

The application calculates a Privacy Risk Score from 0–100, identifies
privacy weaknesses, provides personalized security recommendations,
visualizes category-wise risk, and generates a downloadable privacy
assessment report.

---

## 📌 Project Overview

Social-media platforms can expose personal information through public
profiles, location sharing, contact information, weak authentication,
excessive connections, third-party applications, and unsafe content-sharing
practices.

This project provides an educational framework for assessing these privacy
risks without accessing or monitoring real social-media accounts.

The system uses a questionnaire-based risk model to evaluate privacy and
security practices and provide actionable recommendations.

---

## 🎯 Objectives

- Assess common social-media privacy risks.
- Calculate a Privacy Risk Score from 0–100.
- Classify users into different risk levels.
- Identify privacy and security weaknesses.
- Generate personalized security recommendations.
- Visualize category-wise privacy risk.
- Provide a privacy protection checklist.
- Generate downloadable PDF assessment reports.
- Demonstrate aggregate analysis using synthetic profiles.
- Promote privacy and cybersecurity awareness.

---

## 🚦 Risk Classification

| Score | Risk Level |
|------:|------------|
| 0–20 | 🟢 LOW |
| 21–40 | 🟡 MODERATE |
| 41–70 | 🟠 HIGH |
| 71–100 | 🔴 CRITICAL |

A higher score indicates greater potential privacy exposure.

The score is an educational risk indicator and does not guarantee whether
an account will or will not be compromised.

---

## ✨ Key Features

### 🔐 Privacy Risk Assessment

The application evaluates multiple privacy and security categories,
including:

- Profile Visibility
- Personal Information
- Contact Information
- Location Exposure
- Identity Exposure
- Content Visibility
- Social Connections
- Application Security
- Authentication
- Account Monitoring
- Social Engineering
- Technical Privacy
- Content Exposure

---

### 📊 Risk Scoring

Each assessment question contributes risk points based on the selected
answer.

The framework calculates:

- Overall Privacy Risk Score
- Risk Level
- Category-wise Risk Scores
- Individual Question Scores

---

### ⚠️ Weakness Detection

The application identifies high-risk answers and converts them into
specific privacy weaknesses.

---

### 🛠️ Personalized Recommendations

The system generates defensive recommendations based on detected
weaknesses.

Examples include:

- Restricting profile visibility
- Limiting public personal information
- Enabling MFA
- Using unique passwords
- Reviewing connected applications
- Restricting tagging
- Reviewing old posts
- Avoiding suspicious links
- Verifying unknown connection requests

---

### 📈 Data Visualization

Interactive visualizations are provided using Plotly, including:

- Category-wise risk analysis
- Synthetic profile risk distribution
- Synthetic privacy risk score distribution

---

### 📄 PDF Privacy Report

Users can generate and download a privacy risk assessment report
containing:

- Overall risk score
- Risk level
- Category-wise risk
- Detected weaknesses
- Security recommendations

---

### 👥 Synthetic Data Dashboard

The project includes fictional synthetic profiles for demonstrating
aggregate privacy-risk analysis.

No real social-media users are represented.

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────────┐
                    │      Streamlit UI       │
                    │        app.py           │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Privacy Assessment    │
                    │      questions.py       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Input Validation     │
                    │      validators.py      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Risk Engine        │
                    │     risk_engine.py      │
                    └────────────┬────────────┘
                                 │
                  ┌──────────────┴──────────────┐
                  ▼                             ▼
       ┌─────────────────────┐       ┌─────────────────────┐
       │ Weakness Detection  │       │ Recommendations     │
       │ recommendations.py  │       │ recommendations.py  │
       └──────────┬──────────┘       └──────────┬──────────┘
                  │                             │
                  └──────────────┬──────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │    Results Dashboard    │
                    │   Charts + Checklist    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      PDF Report         │
                    │   report_generator.py   │
                    └─────────────────────────┘