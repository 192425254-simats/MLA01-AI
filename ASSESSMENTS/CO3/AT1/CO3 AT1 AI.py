# Intelligent Student Academic Advising System
# Student: Priya

# ============================================================
# 1. KNOWLEDGE BASE - FACTS
# ============================================================

student = "Priya"

facts = {
    "attendance": {
        "Priya": 68
    },

    "failed_courses": {
        "Priya": 2
    },

    "good_performance": {
        "Priya": True
    },

    "high_attendance": {
        "Priya": False
    },

    "completed_prerequisite": {
        ("Priya", "AdvancedAI"): True
    }
}


# ============================================================
# 2. FOL PREDICATES
# ============================================================

# Attendance(x, percentage)
# FailedCourses(x, number)
# GoodPerformance(x)
# HighAttendance(x)
# CompletedPrerequisite(x, course)
# AttendanceCounseling(x)
# AcademicCounseling(x)
# AdvancedCourseRecommendation(x, course)
# CanRegister(x, course)


# ============================================================
# 3. FOL RULES
# ============================================================

# Rule 1:
# Attendance(x, A) AND A < 75
# -> AttendanceCounseling(x)

# Rule 2:
# FailedCourses(x, F) AND F >= 2
# -> AcademicCounseling(x)

# Rule 3:
# HighAttendance(x) AND GoodPerformance(x)
# -> AdvancedCourseRecommendation(x, AdvancedCourse)

# Rule 4:
# CompletedPrerequisite(x, AdvancedAI)
# -> CanRegister(x, AdvancedAI)


# ============================================================
# 4. UNIFICATION
# ============================================================

def unify_student(student1, student2):
    if student1 == student2:
        return {"x": student1}
    return None


def unify_course(student_name, course):
    return {
        "x": student_name,
        "course": course
    }


print("=" * 60)
print("INTELLIGENT STUDENT ACADEMIC ADVISING SYSTEM")
print("=" * 60)


print("\n1. KNOWLEDGE ENGINEERING REQUIREMENTS")
print("--------------------------------------")
print("Input:")
print("- Student attendance")
print("- Number of failed courses")
print("- Academic performance")
print("- Completed prerequisite courses")

print("\nRules:")
print("1. Attendance below 75% -> Attendance Counseling")
print("2. Two or more failed courses -> Academic Counseling")
print("3. High attendance + good performance -> Advanced Course")
print("4. Completed prerequisite -> Can Register for Advanced Course")


# ============================================================
# 5. DISPLAY KNOWLEDGE BASE
# ============================================================

print("\n2. KNOWLEDGE BASE")
print("-----------------")

print("Facts:")
print("Attendance(Priya, 68)")
print("FailedCourses(Priya, 2)")
print("CompletedPrerequisite(Priya, AdvancedAI)")


print("\nFOL RULES:")
print("Attendance(x,A) AND A < 75 -> AttendanceCounseling(x)")
print("FailedCourses(x,F) AND F >= 2 -> AcademicCounseling(x)")
print("HighAttendance(x) AND GoodPerformance(x) -> AdvancedCourseRecommendation(x,Course)")
print("CompletedPrerequisite(x,Course) -> CanRegister(x,Course)")


# ============================================================
# 6. UNIFICATION
# ============================================================

print("\n3. UNIFICATION")
print("--------------")

result1 = unify_student("Priya", "Priya")

if result1:
    print("Unification:")
    print("Student(x) = Student(Priya)")
    print("Substitution:", result1)

result2 = unify_course("Priya", "AdvancedAI")

print("\nCourse Unification:")
print("CompletedPrerequisite(x, Course)")
print("CompletedPrerequisite(Priya, AdvancedAI)")
print("Substitution:", result2)


# ============================================================
# 7. FORWARD CHAINING
# ============================================================

print("\n4. FORWARD CHAINING")
print("-------------------")

recommendations = []

# Rule 1
attendance = facts["attendance"]["Priya"]

if attendance < 75:
    recommendations.append("Attendance Counseling")
    print("Attendance(Priya, 68)")
    print("68 < 75")
    print("=> AttendanceCounseling(Priya)")


# Rule 2
failed = facts["failed_courses"]["Priya"]

if failed >= 2:
    recommendations.append("Academic Counseling")
    print("\nFailedCourses(Priya, 2)")
    print("2 >= 2")
    print("=> AcademicCounseling(Priya)")


# Rule 3
if (facts["high_attendance"]["Priya"] and
        facts["good_performance"]["Priya"]):

    recommendations.append("Advanced Course Recommendation")
    print("\nHighAttendance(Priya)")
    print("GoodPerformance(Priya)")
    print("=> AdvancedCourseRecommendation(Priya, AdvancedCourse)")
else:
    print("\nHighAttendance(Priya) AND GoodPerformance(Priya)")
    print("=> Condition not satisfied")


# Rule 4
if facts["completed_prerequisite"][("Priya", "AdvancedAI")]:
    recommendations.append("Can Register for Advanced AI Course")

    print("\nCompletedPrerequisite(Priya, AdvancedAI)")
    print("=> CanRegister(Priya, AdvancedAI)")


# ============================================================
# 8. BACKWARD CHAINING
# ============================================================

print("\n5. BACKWARD CHAINING")
print("--------------------")

print("Goal: AcademicCounseling(Priya)")

print("Required condition:")
print("FailedCourses(Priya, F) AND F >= 2")

print("Fact found:")
print("FailedCourses(Priya, 2)")

if failed >= 2:
    print("2 >= 2")
    print("Therefore:")
    print("AcademicCounseling(Priya) = TRUE")
else:
    print("AcademicCounseling(Priya) = FALSE")


# ============================================================
# 9. RESOLUTION
# ============================================================

print("\n6. RESOLUTION")
print("-------------")

print("Goal: AcademicCounseling(Priya)")

print("\nRule:")
print("FailedCourses(x,F) AND F >= 2")
print("-> AcademicCounseling(x)")

print("\nFact:")
print("FailedCourses(Priya,2)")

print("\nSubstitution:")
print("x = Priya")
print("F = 2")

print("\nSince 2 >= 2:")
print("FailedCourses(Priya,2)")
print("+ Rule")
print("-----------------------------")
print("AcademicCounseling(Priya)")

print("\nResolution Result:")
print("AcademicCounseling(Priya) = TRUE")


# ============================================================
# 10. FINAL RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 60)
print("FINAL RECOMMENDATIONS FOR PRIYA")
print("=" * 60)

for recommendation in recommendations:
    print("->", recommendation)


# ============================================================
# 11. ADVANTAGES AND LIMITATIONS
# ============================================================

print("\n7. ADVANTAGES")
print("-------------")
print("1. Easy to understand and explain.")
print("2. Provides consistent recommendations.")
print("3. Rules can be modified easily.")
print("4. Inference can be traced from facts to conclusions.")
print("5. Useful for academic decision support.")


print("\n8. LIMITATIONS")
print("--------------")
print("1. Cannot easily handle uncertain information.")
print("2. Large systems may require many rules.")
print("3. Recommendations depend on the quality of rules.")
print("4. It may not handle unusual student situations.")
print("5. Rules need to be manually updated.")
