# Person DOB Knowledge Base

people = {
    "Rahul": "15-08-2002",
    "Priya": "20-03-2004",
    "Amit": "10-12-2001",
    "Anitha": "25-06-2003",
    "Kiran": "05-01-2005"
}

name = input("Enter person's name: ")

if name in people:
    print("Date of Birth:", people[name])
else:
    print("Person not found.")
