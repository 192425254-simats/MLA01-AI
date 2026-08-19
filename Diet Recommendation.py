def diet_recommendation(age, bmi, condition):

    if bmi >= 30 and condition == "diabetes":
        return "Low-carbohydrate, low-sugar diet"

    elif bmi >= 25 and condition == "hypertension":
        return "Low-sodium DASH-style diet"

    elif bmi < 18.5:
        return "High-protein, calorie-rich balanced diet"

    elif 18.5 <= bmi < 25:
        return "Balanced diet with fruits, vegetables and whole grains"

    else:
        return "Controlled-calorie balanced diet"


# User input
age = int(input("Enter age: "))
bmi = float(input("Enter BMI: "))
condition = input("Enter health condition: ").lower()

# Expert system
recommendation = diet_recommendation(age, bmi, condition)

print("\nRecommended Diet Plan:")
print(recommendation)
