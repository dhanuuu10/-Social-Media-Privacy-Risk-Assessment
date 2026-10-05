from collections import defaultdict


def calculate_question_score(question, selected_answer):
    """
    Calculate the risk points for one assessment question.

    Each question contains an options dictionary where
    every answer is mapped to a risk value from 0 to 5.
    """

    options = question["options"]

    if selected_answer not in options:
        raise ValueError(
            f"Invalid answer for question: {question['id']}"
        )

    return options[selected_answer]


def get_risk_level(score):
    """
    Convert a 0-100 privacy risk score into a risk level.
    """

    if score <= 20:
        return "LOW"

    elif score <= 40:
        return "MODERATE"

    elif score <= 70:
        return "HIGH"

    else:
        return "CRITICAL"


def calculate_risk(questions, answers):
    """
    Calculate the overall privacy risk score and
    category-wise risk scores.

    Parameters:
        questions: List of assessment questions.
        answers: Dictionary containing question IDs and selected answers.

    Returns:
        Dictionary containing overall score, risk level,
        category scores, and individual question scores.
    """

    total_score = 0
    question_scores = {}
    category_totals = defaultdict(int)
    category_maximums = defaultdict(int)

    for question in questions:

        question_id = question["id"]

        if question_id not in answers:
            raise ValueError(
                f"Missing answer for question: {question_id}"
            )

        selected_answer = answers[question_id]

        score = calculate_question_score(
            question,
            selected_answer
        )

        total_score += score

        question_scores[question_id] = score

        category = question["category"]

        category_totals[category] += score

        category_maximums[category] += question["weight"]

    risk_level = get_risk_level(total_score)

    category_scores = {}

    for category in category_totals:

        maximum = category_maximums[category]

        if maximum == 0:
            category_scores[category] = 0

        else:
            category_scores[category] = round(
                (category_totals[category] / maximum) * 100,
                2
            )

    return {
        "overall_score": total_score,
        "risk_level": risk_level,
        "question_scores": question_scores,
        "category_scores": category_scores
    }