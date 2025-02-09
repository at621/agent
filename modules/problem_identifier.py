def identify_problem(user_request: str) -> str:
    """
    Naive approach to detect PD or LGD from text.
    """
    req = user_request.lower()
    if "pd" in req or "default" in req:
        return "PD"
    elif "lgd" in req or "loss given default" in req:
        return "LGD"
    else:
        return "UNKNOWN"