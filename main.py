def manage_student_database():
    students = []
    student_id = 1
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        if any(student[1] == name for student in students):
            print("This name is already in the list.")
        else:
            students.append((student_id, name))
            student_id += 1
    print("\nComplete List of Students (Tuples):")
    print(students)
    print("\nList of Students with IDs:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")
    if total_students > 0:
        longest_name_student = max(students, key=lambda student: len(student[1]))[1]
        shortest_name_student = min(students, key=lambda student: len(student[1]))[1]
        print(f"The student with the longest name is: {longest_name_student}")
        print(f"The student with the shortest name is: {shortest_name_student}")
manage_student_database()
