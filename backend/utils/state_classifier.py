def classify_state(text, step_count, heart_rate):
    if "stress" in text.lower() or heart_rate > 100:
        return "Stressed"
    elif step_count < 50:
        return "Fatigued"
    elif "creative" in text.lower():
        return "Creative"
    else:
        return "Focused"