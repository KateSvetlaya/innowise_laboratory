from typing import List, Dict, Union


def add_student(students: List[Dict[str, Union[str, List[float]]]]) -> None:
    """
    Prompt the user to input a student's name and add the student to the list if valid.

    Args:
        students: List of students, each represented by a dictionary with 'name' and 'grades'.

    Returns:
        None
    """
    name = input("Enter the name of the new student: ").strip()
    if not name:
        print("Name can't be empty.")
        return
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Name must contain only letters and spaces.")
        return
    if any(s['name'].lower() == name.lower() for s in students):
        print(f"Student '{name}' already exists.")
        return
    students.append({'name': name, 'grades': []})
    print(f"Student '{name}' added successfully.")


def display_menu() -> None:
    """
    Displays the main menu options.
    """
    print("\n===== Student Grade Analyzer =====")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")
    print("==================================")


def add_grades(students: List[Dict[str, Union[str, List[float]]]]) -> None:
    """
    Prompts the user to add grades for a specified student.

    Args:
        students: List of student dictionaries.

    Returns:
        None
    """
    name = input("Enter the student's name to add grades: ").strip()
    # Search for the student (case-insensitive)
    student = next((s for s in students if s['name'].lower() == name.lower()), None)
    if not student:
        print(f"Student '{name}' not found.")
        return

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()
        if grade_input.lower() == 'done':
            break
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student['grades'].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")


def show_report(students: List[Dict[str, Union[str, List[float]]]]) -> None:
    """
    Displays a report of all students, including their average grades and overall statistics.

    Args:
        students: List of student dictionaries.

    Returns:
        None
    """
    if not students:
        print("No student data available.")
        return

    total_sum = 0.0
    total_count = 0
    max_avg: Union[float, None] = None
    min_avg: Union[float, None] = None
    grades_exist = False

    print("\n--- Student Report ---")
    for s in students:
        try:
            grades = s.get('grades')
            # type checking grades
            if isinstance(grades, list):
                if grades:
                    avg = sum(grades) / len(grades)
            print(f"{s['name']}'s average grade is {avg:.1f}")
            grades_exist = True
            total_sum += float(sum(grades))
            total_count += len(s['grades'])
            if (max_avg is None) or (avg > max_avg):
                max_avg = avg
            if (min_avg is None) or (avg < min_avg):
                min_avg = avg
        except ZeroDivisionError:
            print(f"{s['name']}: N/A")  # Student has no grades

    if grades_exist and total_count > 0:
        overall_avg = total_sum / total_count
        print("\n Overall statistics:")
        print(f"Maximum average grade: {max_avg:.1f}")
        print(f"Minimum average grade: {min_avg:.1f}")
        print(f"Overall average grade: {overall_avg:.1f}")
    else:
        print("No grades available to compute overall statistics.")


def find_top_performer(students: List[Dict[str, Union[str, List[float]]]]) -> None:
    """
    Finds and displays the student with the highest average grade.

    Args:
        students: List of student dictionaries.

    Returns:
        None
    """
    students_with_grades = [s for s in students if s['grades']]
    if not students_with_grades:
        print("No students with grades available to determine top performer.")
        return
    top_student = max(
        students_with_grades,
        key=lambda s: sum(s['grades']) / len(s['grades'])
    )
    avg = sum(top_student['grades']) / len(top_student['grades'])
    print(f"The student with the highest average is {top_student['name']} with a grade of {avg:.1f}")


def main() -> None:
    """
    Main function that runs the student grade analyzer program.
    """
    students: List[Dict[str, Union[str, List[float]]]] = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        try:
            choice_int = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice_int == 1:
            add_student(students)
        elif choice_int == 2:
            add_grades(students)
        elif choice_int == 3:
            show_report(students)
        elif choice_int == 4:
            find_top_performer(students)
        elif choice_int == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
