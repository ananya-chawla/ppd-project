def analyze_answers(answers):
    # Dummy scoring system based on 'Yes' answers
    score = 0
    for answer in answers:
        if answer == "No":
            score += 1
    return score
