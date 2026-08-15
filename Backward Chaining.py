# Known symptoms
facts = {
    "fever",
    "cough",
    "body_pain"
}

# Rules: disease -> required symptoms
rules = {
    "flu": {"fever", "cough", "body_pain"},
    "cold": {"cough"},
    "infection": {"fever", "body_pain"}
}

# Backward Chaining Function
def backward_chaining(goal):
    # If goal is already a fact
    if goal in facts:
        return True

    # Check rules that can prove the goal
    if goal in rules:
        for symptom in rules[goal]:
            if not backward_chaining(symptom):
                return False
        return True

    return False


# Test diseases
for disease in rules:
    if backward_chaining(disease):
        print("Possible disease:", disease)
