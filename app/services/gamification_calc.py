def calculate_rank(xp: int) -> str:
    if xp >= 1000:
        return "Master"
    if xp >= 300:
        return "Advanced"
    return "Beginner"
