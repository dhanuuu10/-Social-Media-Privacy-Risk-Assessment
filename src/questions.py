QUESTIONS = [
    {
        "id": "profile_visibility",
        "question": "How visible is your social-media profile to people you don't know?",
        "category": "Profile Visibility",
        "weight": 5,
        "options": {
            "Private or highly restricted": 0,
            "Friends/connections only": 1,
            "Partially public": 3,
            "Completely public": 5
        }
    },

    {
        "id": "personal_information",
        "question": "How much personal information is publicly visible on your profile?",
        "category": "Personal Information",
        "weight": 5,
        "options": {
            "Very little information": 0,
            "Limited information": 1,
            "Some personal information": 3,
            "A large amount of personal information": 5
        }
    },

    {
        "id": "contact_information",
        "question": "How exposed are your phone number or email/contact details on social media?",
        "category": "Contact Information",
        "weight": 5,
        "options": {
            "Not publicly visible": 0,
            "Visible only to trusted connections": 1,
            "Partially visible": 3,
            "Publicly visible": 5
        }
    },

    {
        "id": "location_exposure",
        "question": "How often do you publicly share your current or regular location?",
        "category": "Location",
        "weight": 5,
        "options": {
            "Never or almost never": 0,
            "Rarely and carefully": 1,
            "Sometimes": 3,
            "Frequently or publicly": 5
        }
    },

    {
        "id": "workplace_education",
        "question": "How much workplace or education information is publicly visible?",
        "category": "Identity Exposure",
        "weight": 5,
        "options": {
            "Not publicly visible": 0,
            "Limited information": 1,
            "Some details visible": 3,
            "Detailed information visible": 5
        }
    },

    {
        "id": "birthday_exposure",
        "question": "How visible is your birthday or date-of-birth information?",
        "category": "Personal Information",
        "weight": 5,
        "options": {
            "Hidden": 0,
            "Visible only to trusted connections": 1,
            "Partially visible": 3,
            "Publicly visible": 5
        }
    },

    {
        "id": "family_relationship",
        "question": "How much family or relationship information do you publicly share?",
        "category": "Personal Information",
        "weight": 5,
        "options": {
            "Very little or none": 0,
            "Limited information": 1,
            "Some information": 3,
            "Detailed information": 5
        }
    },

    {
        "id": "post_visibility",
        "question": "Who can normally view your social-media posts?",
        "category": "Content Visibility",
        "weight": 5,
        "options": {
            "Trusted connections only": 0,
            "Mostly trusted connections": 1,
            "Mixed audience": 3,
            "Anyone/public": 5
        }
    },

    {
        "id": "follower_controls",
        "question": "How carefully do you control who can follow or connect with you?",
        "category": "Social Connections",
        "weight": 5,
        "options": {
            "I carefully review connections": 0,
            "I usually review them": 1,
            "I sometimes accept without checking": 3,
            "I generally accept unknown requests": 5
        }
    },

    {
        "id": "tagging_permissions",
        "question": "Who can tag or mention you in social-media content?",
        "category": "Content Visibility",
        "weight": 5,
        "options": {
            "Tagging is restricted and reviewed": 0,
            "Mostly restricted": 1,
            "Partially unrestricted": 3,
            "Anyone can tag or mention me": 5
        }
    },

    {
        "id": "third_party_apps",
        "question": "How carefully do you manage third-party applications connected to your social-media accounts?",
        "category": "Application Security",
        "weight": 5,
        "options": {
            "I regularly review and remove unnecessary access": 0,
            "I review access occasionally": 1,
            "I rarely review access": 3,
            "I do not review connected applications": 5
        }
    },

    {
        "id": "account_authentication",
        "question": "How strong is the authentication method used to protect your account?",
        "category": "Authentication",
        "weight": 5,
        "options": {
            "Strong authentication with additional protection": 0,
            "Strong unique password": 1,
            "Basic password protection": 3,
            "Weak or easily guessed authentication": 5
        }
    },

    {
        "id": "mfa_usage",
        "question": "Do you use multi-factor authentication (MFA) on your social-media accounts?",
        "category": "Authentication",
        "weight": 5,
        "options": {
            "MFA is enabled": 0,
            "MFA is enabled on important accounts": 1,
            "Planning to enable MFA": 3,
            "MFA is not enabled": 5
        }
    },

    {
        "id": "password_reuse",
        "question": "How often do you reuse the same password across different accounts?",
        "category": "Authentication",
        "weight": 5,
        "options": {
            "I use unique passwords": 0,
            "I rarely reuse passwords": 1,
            "I sometimes reuse passwords": 3,
            "I frequently reuse passwords": 5
        }
    },

    {
        "id": "login_alerts",
        "question": "Do you use login alerts or account security notifications?",
        "category": "Account Monitoring",
        "weight": 5,
        "options": {
            "Enabled and actively monitored": 0,
            "Enabled but rarely checked": 1,
            "Not sure whether they are enabled": 3,
            "Disabled": 5
        }
    },

    {
        "id": "unknown_connections",
        "question": "How do you handle connection or follower requests from people you do not know?",
        "category": "Social Connections",
        "weight": 5,
        "options": {
            "I reject or carefully verify them": 0,
            "I usually verify them": 1,
            "I sometimes accept them": 3,
            "I commonly accept unknown requests": 5
        }
    },

    {
        "id": "suspicious_messages",
        "question": "How do you respond to suspicious links or unexpected messages?",
        "category": "Social Engineering",
        "weight": 5,
        "options": {
            "I avoid them and verify independently": 0,
            "I usually verify them": 1,
            "I sometimes interact before verifying": 3,
            "I often click or respond without verification": 5
        }
    },

    {
        "id": "photo_metadata",
        "question": "How aware are you of location and other metadata that may be associated with photos?",
        "category": "Technical Privacy",
        "weight": 5,
        "options": {
            "I understand and manage metadata risks": 0,
            "I have basic awareness": 1,
            "I am unsure about metadata risks": 3,
            "I have no awareness of metadata risks": 5
        }
    },

    {
        "id": "historical_posts",
        "question": "How often do you review older social-media posts and remove unnecessary exposure?",
        "category": "Content Exposure",
        "weight": 5,
        "options": {
            "I regularly review old posts": 0,
            "I review them occasionally": 1,
            "I rarely review them": 3,
            "I have never reviewed them": 5
        }
    },

    {
        "id": "social_engineering",
        "question": "How much information visible on your profile could potentially help someone create a convincing social-engineering message?",
        "category": "Social Engineering",
        "weight": 5,
        "options": {
            "Very little useful information": 0,
            "Limited information": 1,
            "Some potentially useful information": 3,
            "A significant amount of useful information": 5
        }
    }
]