from PerformScraping import Scraper
from crn_check import run_crn_lookup
from schedule import Schedule, load_course_from_csv
from drop_slip import DropSlip, write_drop_slip_to_file
from resources import load_default_resources, get_drop_deadline_info, load_professor_contacts



class Driver:

    def main(self):
        print("Welcome to the Tsunamis CPSC Help Desk!\n")
        print("1) Find the drop date for your semester")
        print("2) Look up a course CRN, prerequisites, and add/drop dates")
        print("3) Create a drop slip for a course")
        choice = input("Enter your choice (1 or 2 or 3): ").strip()

        if choice == "1":
            select_soup = Scraper.getAcademicCalander()
            semesterDropDates = Scraper.getDropDates(select_soup)

            print("\nFind the drop date for your semester!")
            usrchoice = input("Which semester are you looking for? (Fall/Spring/Summer): ")
            print("\n")

            for key, values in semesterDropDates.items():
                if usrchoice.lower() in key.lower():
                    for value in values:
                        print("Drop Dates: ", value)

        elif choice == "2":
            run_crn_lookup()

        elif choice == "3":
            self.create_drop_slip()
        else:
             print(" Invalid choice.")



    def create_drop_slip(self):
        student_name = input("Enter your full name: ").strip()
        student_id = input("Enter your student ID: ").strip()
        term = input("Enter the term (e.g., Fall 2025): ").strip()
        crn = input("Enter the CRN you want to drop: ").strip()

        course = load_course_from_csv(crn)
        if course is None:
            print("No course found with that CRN.")
            return

        schedule = Schedule(student_id, student_name)
        schedule.add_course(course)

        slip = DropSlip(student_name, student_id, term, course)
        filename = write_drop_slip_to_file(slip)

        print("Drop slip created:", filename)

    from resources import load_default_resources

def show_resources_menu() -> None:
    """Display all quick-links with numbers a student can choose from."""
    resources = load_default_resources()

    print("\n=== Quick-Links Menu ===")
    for idx, r in enumerate(resources, start=1):
        print(f"{idx}. {r.name} ({r.category})")

    print("\nEnter a number to open a resource or press Enter to cancel.")

def handle_resource_selection(choice: str) -> None:
    resources = load_default_resources()

    if not choice.isdigit():
        print("Invalid selection.")
        return

    idx = int(choice)
    if not (1 <= idx <= len(resources)):
        print("Selection out of range.")
        return

    selected = resources[idx - 1]

    print(f"\nYou selected: {selected.name}")

    if selected.name == "Drop Deadline Calendar":
        print("\n" + get_drop_deadline_info())
    else:
        print(f"URL: {selected.url}")




def show_professor_contacts():
    data = load_professor_contacts()
    print("\n=== Professor Contacts ===")
    for course, info in data.items():
        print(f"{course}: {info['professor']}")
        print(f"  Email: {info['email']}")
        print(f"  Hours: {info['office_hours']}")
        print()

    
    
if __name__ == "__main__":
    driver = Driver()
    driver.main()