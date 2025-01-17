students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

# Prompt the user to enter student's name
student_name = input("Entrez le nom de l’étudiant : ")

# Check if student exists in dictionary
if student_name in students:
    print(f"Notes de {student_name} :")
    total = 0
    count = 0

    # Display each subject and grade
    for subject, grade in students[student_name].items():
        print(f"{subject} : {grade}")
        total += grade
        count += 1

    # Calculate and display average
    average = total / count
    print(f"Moyenne de {student_name} : {average:.2f}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
