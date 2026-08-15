# Facts
facts = {
    "computer_not_starting",
    "power_light_off"
}

# Production rules
rules = [
    ({"computer_not_starting", "power_light_off"}, "power_supply_problem"),
    ({"power_supply_problem"}, "check_power_cable"),
    ({"check_power_cable"}, "computer_needs_service")
]

# Forward Chaining
changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            changed = True
            print("Derived:", conclusion)

print("\nFinal Facts:")
for fact in facts:
    print("-", fact)
