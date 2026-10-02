from src.questions import QUESTIONS


def validate_assessment(answers):
    """
    Validate assessment answers before calculating risk.

    Returns:
        True if the assessment is valid.

    Raises:
        ValueError if the assessment contains invalid data.
    """

    if not isinstance(answers, dict):
        raise ValueError(
            "Assessment answers must be provided as a dictionary."
        )


    # --------------------------------------------------
    # EXPECTED QUESTION IDs
    # --------------------------------------------------

    expected_ids = {
        question["id"]
        for question in QUESTIONS
    }


    # --------------------------------------------------
    # CHECK FOR MISSING QUESTIONS
    # --------------------------------------------------

    missing_ids = expected_ids - set(answers.keys())

    if missing_ids:

        raise ValueError(
            f"Missing answers for questions: "
            f"{', '.join(sorted(missing_ids))}"
        )


    # --------------------------------------------------
    # CHECK FOR UNEXPECTED QUESTIONS
    # --------------------------------------------------

    unexpected_ids = set(answers.keys()) - expected_ids

    if unexpected_ids:

        raise ValueError(
            f"Unexpected question IDs found: "
            f"{', '.join(sorted(unexpected_ids))}"
        )


    # --------------------------------------------------
    # VALIDATE EACH ANSWER
    # --------------------------------------------------

    for question in QUESTIONS:

        question_id = question["id"]

        selected_answer = answers[question_id]

        valid_options = question["options"].keys()

        if selected_answer not in valid_options:

            raise ValueError(
                f"Invalid answer for question: "
                f"{question_id}"
            )


    return True