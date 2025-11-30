from courses import load_courses, filter_by_subject, Course

def prompt_subject() -> str:
    return input("Enter a subject code (e.g., MATH, CPSC): ").strip()

def show_course_list(courses_for_subject):
    print("\nAvailable courses:")
    for idx, course in enumerate(courses_for_subject, start=1):
        print(f"{idx}. {course.subject} {course.number} - {course.title}")

def select_course(courses_for_subject):
    if not courses_for_subject:
        return None

    while True:
        choice = input("\nChoose a course number (or press Enter to cancel): ").strip()

        if choice == "":
            return None

        if not choice.isdigit():
            print("Invalid input, enter a number.")
            continue

        index = int(choice)
        if 1 <= index <= len(courses_for_subject):
            return courses_for_subject[index - 1]
        else:
            print("That number is not in the list. Try again.")

def show_course_details(course: Course):
    print("\n====== Course Details ======")
    print(f"{course.subject} {course.number} - {course.title}")
    print(f"CRN: {course.crn}")
    print(f"Prerequisites: {course.prerequisites}")
    print(f"Add Deadline: {course.add_deadline}")
    print(f"Drop Deadline: {course.drop_deadline}")
    print("============================\n")

def main():
    courses = load_courses("data/courses.csv")
    subject = prompt_subject()

    filtered = filter_by_subject(courses, subject)

    if not filtered:
        print("No courses found for that subject.")
        return

    show_course_list(filtered)

    selected = select_course(filtered)
    if selected:
        show_course_details(selected)
    else:
        print("No course selected.")

if __name__ == "__main__":
    main()