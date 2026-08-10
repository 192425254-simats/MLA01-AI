# Subjects
subjects = ['AI', 'DBMS', 'CN', 'ML', 'CD']

# Examination slots
slots = ['T1', 'T2', 'T3', 'T4']

# Conflict graph
conflicts = {
    'AI': ['DBMS', 'CN'],
    'DBMS': ['AI', 'ML'],
    'CN': ['AI', 'ML', 'CD'],
    'ML': ['DBMS', 'CN', 'CD'],
    'CD': ['CN', 'ML']
}

# Initial domains
domains = {}

for subject in subjects:
    domains[subject] = slots.copy()


def is_consistent(subject, value, assignment):

    for neighbor in conflicts[subject]:

        if neighbor in assignment:
            if assignment[neighbor] == value:
                return False

    return True


def forward_check(subject, value, domains, assignment):

    new_domains = {
        s: domains[s].copy()
        for s in domains
    }

    for neighbor in conflicts[subject]:

        if neighbor not in assignment:

            if value in new_domains[neighbor]:
                new_domains[neighbor].remove(value)

            # Empty domain means failure
            if len(new_domains[neighbor]) == 0:
                return None

    return new_domains


def select_mrv_variable(assignment, domains):

    unassigned = [
        s for s in subjects
        if s not in assignment
    ]

    return min(
        unassigned,
        key=lambda s: len(domains[s])
    )


def backtracking(assignment, domains):

    # All subjects assigned
    if len(assignment) == len(subjects):
        return assignment

    # MRV
    subject = select_mrv_variable(
        assignment,
        domains
    )

    print("\nSelected using MRV:", subject)

    for value in domains[subject]:

        print("Trying:", subject, "=", value)

        if is_consistent(
            subject,
            value,
            assignment
        ):

            assignment[subject] = value

            # Forward Checking
            new_domains = forward_check(
                subject,
                value,
                domains,
                assignment
            )

            if new_domains is not None:

                result = backtracking(
                    assignment,
                    new_domains
                )

                if result is not None:
                    return result

            # Backtracking
            del assignment[subject]

    return None


solution = backtracking({}, domains)

print("\nFinal Examination Timetable")
print("--------------------------------")

for subject, slot in solution.items():
    print(subject, "->", slot)
