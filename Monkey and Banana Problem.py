# Monkey and Banana Problem in AI

# Initial State
monkey_pos = "Door"
stool_pos = "Corner"
stick_pos = "Corner"
banana_pos = "Center"

on_stool = False
has_stick = False
has_banana = False

print("------ Initial State ------")
print("Monkey :", monkey_pos)
print("Stool  :", stool_pos)
print("Stick  :", stick_pos)
print("Banana :", banana_pos)

# Step 1: Move to stool
if monkey_pos != stool_pos:
    print("\nMonkey moves to the stool.")
    monkey_pos = stool_pos

# Step 2: Take the stick
if monkey_pos == stick_pos:
    print("Monkey picks up the stick.")
    has_stick = True

# Step 3: Push stool under banana
if stool_pos != banana_pos:
    print("Monkey pushes the stool under the banana.")
    stool_pos = banana_pos
    monkey_pos = banana_pos

# Step 4: Climb the stool
if monkey_pos == banana_pos:
    print("Monkey climbs onto the stool.")
    on_stool = True

# Step 5: Get banana
if on_stool and has_stick:
    print("Monkey uses the stick to get the banana.")
    has_banana = True

# Final State
print("\n------ Final State ------")
print("On Stool :", on_stool)
print("Has Stick:", has_stick)
print("Has Banana:", has_banana)

if has_banana:
    print("\nGoal Achieved! Monkey got the banana.")
else:
    print("\nGoal Not Achieved!")
