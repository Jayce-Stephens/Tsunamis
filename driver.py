from PerformScraping import Scraper
from crn_check import run_crn_lookup
from schedule import Schedule, load_course_from_csv
from drop_slip import DropSlip, write_drop_slip_to_file

# NEW imports
from gpa_calculator import run_gpa_calculator
from course_search import search_course_offerings, CURRENT_SEMESTER


class Driver:

    def main(self):
        while True:
            print("\nWelcome to the Tsunamis CPSC Help Desk!\n")
            print("1) Find the drop date for your semester")
            print("2) Look up a course CRN, prerequisites, and add/drop dates")
            print("3) Create a drop slip for a course")
            print("4) Calculate my GPA")
            print("5) Check if a course is offered this semester")
            print("0) Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.show_drop_dates()
            elif choice == "2":
                run_crn_lookup()
            elif choice == "3":
                self.create_drop_slip()
            elif choice == "4":
                run_gpa_calculator()
            elif choice == "5":
                self.run_course_offering_check()
            elif choice == "0":
                print("\nGoodbye from the Tsunamis CPSC Help Desk!\n")
                break
            else:
                print("\nInvalid choice. Please try again.\n")

    # ==== existing feature: drop dates ====
    def show_drop_dates(self):
        select_soup = Scraper.getAcademicCalander()
        semesterDropDates = Scraper.getDropDates(select_soup)

        print("\nFind the drop date for your semester!")
        usrchoice = input("Which semester are you looking for? (Fall/Spring/Summer): ")
        print()

        found = False
        for key, values in semesterDropDates.items():
            if usrchoice.lower() in key.lower():
                found = True
                for value in values:
                    print("Drop Dates:", value)

        if not found:
            print("Sorry, no drop dates found for that semester.")

    # ==== existing feature: drop slip ====
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

    # ==== NEW feature: course offering checker ====
    def run_course_offering_check(self):
        print("\n--- Course Offering Check ---\n")
        print(f"Current semester: {CURRENT_SEMESTER}")
        print("Example input: MATH 2550, CPSC 2740, ENGL 1020\n")

        course_code = input("Enter a course code (e.g., MATH 2550): ").strip()
        result = search_course_offerings(course_code)

        status = result.get("status")
        message = result.get("message", "")
        sections = result.get("sections", [])

        print(f"\n{message}\n")

        if status in ("offered", "full") and sections:
            print("Sections:")
            for i, sec in enumerate(sections, start=1):
                prefix = sec.get("prefix", "")
                number = sec.get("number", "")
                crn = sec.get("crn", "N/A")
                days = sec.get("days", "TBA")
                time = sec.get("time", "TBA")
                instructor = sec.get("instructor", "TBA")
                seats_open = sec.get("seats_open", "N/A")

                print(
                    f"  {i}. {prefix} {number} (CRN {crn}) "
                    f"- {days} {time}, {instructor}, seats open: {seats_open}"
                )
            print()


if __name__ == "__main__":
    driver = Driver()
    driver.main()
