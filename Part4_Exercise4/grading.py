
def grade_student(score):
    """
    Return a letter grade based on the numeric score (0–100).

    Rules:
    - 90–100 -> "A"
    - 80–89  -> "B"
    - 70–79  -> "C"
    - 60–69  -> "D"
    - 0–59   -> "F"

    If score is outside the range 0–100, raise ValueError.
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    