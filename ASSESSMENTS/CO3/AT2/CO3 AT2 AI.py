# Vehicle Fault Diagnosis using Logic Reasoning

# -----------------------------
# 1. FACTS
# -----------------------------

facts = {
    "does_not_start": ["Car101"],
    "dim_headlights": ["Car101"],
    "battery_problem": [],
    "battery_inspection": [],
    "marked_for_service": []
}

# -----------------------------
# 2. PROPOSITIONAL LOGIC
# -----------------------------
# DoesNotStart(Car101) AND DimHeadlights(Car101)
# -> BatteryProblem(Car101)
#
# BatteryProblem(Car101)
# -> BatteryInspection(Car101)
#
# BatteryInspection(Car101)
# -> MarkedForService(Car101)


# -----------------------------
# 3. FOL PREDICATES AND RULES
# -----------------------------

def DoesNotStart(vehicle):
    return vehicle in facts["does_not_start"]


def DimHeadlights(vehicle):
    return vehicle in facts["dim_headlights"]


def BatteryProblem(vehicle):
    return vehicle in facts["battery_problem"]


def BatteryInspection(vehicle):
    return vehicle in facts["battery_inspection"]


def MarkedForService(vehicle):
    return vehicle in facts["marked_for_service"]


# Rules:
# DoesNotStart(x) AND DimHeadlights(x) -> BatteryProblem(x)
# BatteryProblem(x) -> BatteryInspection(x)
# BatteryInspection(x) -> MarkedForService(x)


# -----------------------------
# 4. UNIFICATION
# -----------------------------

def unify(vehicle1, vehicle2):
    if vehicle1 == vehicle2:
        return {"x": vehicle1}
    return None


vehicle = "Car101"

print("===== VEHICLE FAULT DIAGNOSIS =====\n")

print("FACTS:")
print("1. DoesNotStart(Car101)")
print("2. DimHeadlights(Car101)")

print("\nUNIFICATION:")
result = unify(vehicle, "Car101")

if result:
    print("DoesNotStart(x) and DoesNotStart(Car101)")
    print("Unification successful:", result)
else:
    print("Unification failed")


# -----------------------------
# 5. RESOLUTION / INFERENCE
# -----------------------------

print("\nRESOLUTION / INFERENCE:")

# Rule 1:
# DoesNotStart(x) AND DimHeadlights(x)
# -> BatteryProblem(x)

if DoesNotStart(vehicle) and DimHeadlights(vehicle):
    facts["battery_problem"].append(vehicle)
    print("DoesNotStart(Car101) AND DimHeadlights(Car101)")
    print("=> BatteryProblem(Car101)")

# Rule 2:
# BatteryProblem(x) -> BatteryInspection(x)

if BatteryProblem(vehicle):
    facts["battery_inspection"].append(vehicle)
    print("BatteryProblem(Car101)")
    print("=> BatteryInspection(Car101)")

# Rule 3:
# BatteryInspection(x) -> MarkedForService(x)

if BatteryInspection(vehicle):
    facts["marked_for_service"].append(vehicle)
    print("BatteryInspection(Car101)")
    print("=> MarkedForService(Car101)")


# -----------------------------
# 6. FINAL RESULT
# -----------------------------

print("\n===== FINAL RESULT =====")

if BatteryProblem(vehicle):
    print("Battery Problem: YES")
else:
    print("Battery Problem: NO")

if MarkedForService(vehicle):
    print("Marked for Service: YES")
else:
    print("Marked for Service: NO")
