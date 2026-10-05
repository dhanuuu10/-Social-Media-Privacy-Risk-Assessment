def detect_weaknesses(questions, answers):
    """
    Detect privacy and security weaknesses based on
    high-risk answers selected by the user.
    """

    weaknesses = []

    for question in questions:

        question_id = question["id"]
        selected_answer = answers.get(question_id)

        if selected_answer is None:
            continue

        score = question["options"].get(selected_answer, 0)

        if score >= 3:
            weaknesses.append({
                "question_id": question_id,
                "category": question["category"],
                "question": question["question"],
                "answer": selected_answer,
                "risk_score": score
            })

    return weaknesses


def generate_recommendations(weaknesses):
    """
    Generate defensive privacy and security recommendations
    based on detected weaknesses.
    """

    recommendations = []

    recommendation_map = {
        "profile_visibility": (
            "Review your profile visibility and restrict public "
            "access to information that does not need to be public."
        ),

        "personal_information": (
            "Reduce unnecessary personal information visible on "
            "your social-media profile."
        ),

        "contact_information": (
            "Avoid publicly exposing personal contact information "
            "such as phone numbers or email addresses."
        ),

        "location_exposure": (
            "Avoid publicly sharing your current or regular location. "
            "Review location-sharing and geotagging settings."
        ),

        "workplace_education": (
            "Limit unnecessary workplace and education details "
            "that are publicly visible."
        ),

        "birthday_exposure": (
            "Restrict visibility of your birthday and other "
            "date-of-birth information."
        ),

        "family_relationship": (
            "Limit publicly visible family and relationship details "
            "that could reveal sensitive personal information."
        ),

        "post_visibility": (
            "Review post-audience settings and restrict sensitive "
            "posts to trusted connections."
        ),

        "follower_controls": (
            "Review follower and connection requests carefully "
            "before accepting unknown accounts."
        ),

        "tagging_permissions": (
            "Restrict who can tag or mention you and enable "
            "tag-review controls where available."
        ),

        "third_party_apps": (
            "Review connected third-party applications and revoke "
            "access that is no longer necessary."
        ),

        "account_authentication": (
            "Use a strong, unique password and enable additional "
            "account-protection mechanisms."
        ),

        "mfa_usage": (
            "Enable multi-factor authentication on your social-media "
            "accounts whenever the platform supports it."
        ),

        "password_reuse": (
            "Avoid reusing passwords across accounts. Use unique "
            "passwords and consider a reputable password manager."
        ),

        "login_alerts": (
            "Enable login and security alerts and review unexpected "
            "login notifications promptly."
        ),

        "unknown_connections": (
            "Do not automatically accept connection requests from "
            "unknown accounts. Verify unexpected requests."
        ),

        "suspicious_messages": (
            "Do not click unexpected links or provide sensitive "
            "information through suspicious messages. Verify "
            "requests through an independent trusted channel."
        ),

        "photo_metadata": (
            "Review photo privacy and metadata risks before publicly "
            "sharing images that may reveal location or other "
            "technical information."
        ),

        "historical_posts": (
            "Review older posts periodically and remove or restrict "
            "content that exposes unnecessary personal information."
        ),

        "social_engineering": (
            "Reduce publicly available information that could be "
            "combined to create convincing social-engineering attempts."
        )
    }

    for weakness in weaknesses:

        question_id = weakness["question_id"]

        recommendation = recommendation_map.get(question_id)

        if recommendation:
            recommendations.append({
                "category": weakness["category"],
                "recommendation": recommendation
            })

    return recommendations