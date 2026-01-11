def calculate_risk(answers):
    """
    answers: list of booleans (True = risk indicator)
    """

    score = sum(1 for a in answers if a)

    if score <= 2:
        return score, 'low'
    elif score <= 5:
        return score, 'medium'
    else:
        return score, 'high'