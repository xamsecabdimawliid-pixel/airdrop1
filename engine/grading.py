def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    return "REJECT"


def calculate_quality_score(
    team_verified,
    official_website,
    clear_tokenomics,
    project_activity,
    transparent_rules
):
    checks = [
        (team_verified, 20),
        (official_website, 20),
        (clear_tokenomics, 20),
        (project_activity, 20),
        (transparent_rules, 20)
    ]

    score = sum(
        points for passed, points in checks if passed
    )

    return score, calculate_grade(score)
