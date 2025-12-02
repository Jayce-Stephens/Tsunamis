# Tsunamis

## Final Release Checklist
- [ ] README states purpose, contributors, and how to build, run, and test all the code from the CLI.  Build and run should not assume everyone is using a particular IDE (so don't assume users can click a Run button or use VSC's Command Prompt commands.
- [ ] SDD has the project description, outline, architecture (including UML class diagrams), and all project user stories and use cases.
- [ ] Each team member must update our team's **Statement of Work** shared Excel spreadsheet.  Your grade on this assignment is based ONLY on the quality of your use cases, your GitHub contributions that result in accepted pull requests, and 10% of your grade will be assigned by your fellow team members.
- [ ] **Eric** must finish his pushes to our repo by 8 PM on Dec 1st and then check this box.
- [ ] **Tre'sure** must finish her pushes to our repo by 8 PM on Dec 1st and then check this box.
- [√] **Jayce** must finish his pushes to our repo by 8 PM on Dec 1st and then check this box.
- [ ] **Eric** must do one last check that the code builds, runs, and all the tests run by 10 PM on Dec 1st and then check this box.
- [ ] **Eric** must "Project Release" tag our repo. 
- [ ] Everyone must complete the Brightspace survey to earn the final points for Assignment08.
- [ ] Everyone should complete the Class Climate survey to help Dr. Edwards improve her teaching.


## Tsunamis Project Priorities (1 = Highest Priority)

1.CPSC Help Desk
2. CPSC Register
3. CPSC Core Curriculum Recommender
4. CPSC Electives
5. CPSC Degree Works
6. CPSC Study Buddies


# How to Run the CPSC Help Desk Project

## Run the application
python driver.py

(If on Windows, you may need to use:)
py driver.py


## Run all unit tests


python -m unittest discover

(If on Windows, you may need to use:)
py -m unittest discover

Tsunamis – CPSC Help Desk MVP
Software Engineering – Fall 2025

This project is the Minimum Viable Product (MVP) for the CPSC Help Desk, a command-line tool that helps Xavier students quickly access important academic information such as GPA calculation, CRN lookup, drop deadlines, course offering availability, and professor resources.

How to Run ALL Tests (one command)
python -m unittest discover -s test -p "test_*.py"

How to Run the Project
python driver.py

This launches the Help Desk menu:
Welcome to the Tsunamis CPSC Help Desk!
1) Find the drop date for your semester
2) Look up a course CRN, prerequisites, and add/drop dates
3) Create a drop slip for a course
4) Calculate my GPA
5) Check if a course is offered this semester
0) Exit

Tsunamis/
│
├── driver.py
├── course_search.py
├── gpa_calculator.py
├── crn_check.py
├── PerformScraping.py
├── drop_slip.py
├── schedule.py
├── resources.py
│
├── data/
│   └── courses.csv
│
├── test/
│   ├── test_course_search.py
│   ├── test_crn_check.py
│   ├── test_resources.py
│   ├── test_gpa_calculator.py
│   ├── test_dropslip.py          
│   ├── test_schedule.py          
│   └── __pycache__/
│
├── SDD/
│   └── SDD.md
│
└── README.md

5. Use Cases
   5.1 Use Case: Check Course Offering

Actor: Student

Flow
1. Student selects “Check if a course is offered.”
2. Student enters a course code (e.g., "MATH 2550").
3. System validates format.
4. System searches dataset for matching course.
5.System reports whether the course is:
*offered
*full
*not offered
6*If offered or full, system lists all sections (CRN, instructor, days, times).
*Exception Flows
*Invalid format → return "invalid".
*No match → "not_found".
*All sections full → "full".

5.2 Use Case: GPA Calculator

Actor: Student

Flow
1.Student selects “Calculate my GPA.”
2.Enters grade and credit hours repeatedly.
3.System validates input and converts letter grades to points.
4.System computes weighted GPA.
5.System displays final GPA.

Exceptions
*Invalid grade → error message.
*Zero credits → cannot compute

5.3 Use Case: Drop Deadline Checker
Actor: Student
Flow
1.Student selects “Find drop date.”
2.System scrapes academic calendar.
3.User chooses a semester.
4.System prints available drop dates.

5.4 Use Case: CRN Lookup
1.Student enters CRN.
2.System searches course dataset.
3.Displays meeting times, days, prerequisites.

5.5 Use Case: Drop Slip Generator
1.Student enters name, ID, term, CRN.
2.System loads matching course.
3.System generates a drop slip file.
4.Confirms to user.

6. Class & Module Design
   6.1 PerformScraping.py (Scraper Class)
Methods:
*getAcademicCalander()
*getDropDates(soup)

Uses requests + BeautifulSoup.

6.2 gpa_calculator.py
Functions:
*convert_grade_to_points(grade)
*calculate_gpa(grades, credits)
*run_gpa_calculator()

6.3 course_search.py
Class: Course

Attributes:
*subject
*number
*instructor
*days
*time
*seats_open
*semester
*crn

6.4 crn_check.py
Function:
*run_crn_lookup()
*Reads CSV file → returns matching course & prerequisite

6.5 drop_slip.py
Classes/Methods:
*DropSlip
*write_drop_slip_to_file()
*Creates formatted text output.

6.6 schedule.py
Classes:
*Schedule
*load_course_from_csv(crn)

6.7 resources.py

Provides:
*academic quick links
*professor contacts

6.8 driver.py
*Integrates all modules into a single main menu

7. Data Design
Data Sources:
*courses.csv for CRN lookup
*Hardcoded Course Offering dataset
*JSON-like dictionaries for professor contacts & resources






   



