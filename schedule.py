
class Schedule:

    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

    def viewSchedule(self):
        print("Student: " + self.student_name)

        for c in self.courses:
            print("-" + c)


    

def main():
    prefilled_student_map = {
        "Austin": [
            ("MATH 1090"), ("CPSC 3029"), ("ENGL 9903"), ("CPSC 1210")
        ],
        "Drake": [
            ("MATH 3390"), ("CPSC 1590"), ("ENGL 9903"), ("MATH 1101")
        ],
        "Sarah": [
            ("CPSC 3030"), ("HIST 2203"), ("XCOR 9993"), ("CPSC 4403")
        ],
        "Tony": [
            ("CPSC 1590"), ("CPSC 3029"), ("ENGL 9903"), ("MATH 3390")
        ]
    }

    students = {}

    for name, courses in prefilled_student_map.items():
        s = Schedule(name)
        for c in courses:
            s.addCourse(c)

        students[name] = s
    
    for name in students:
        students[name].viewSchedule()
    

if __name__ == "__main__":
    main()
    
    