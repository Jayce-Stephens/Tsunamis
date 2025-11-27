
class Schedule:

    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

    

def main():
    s = Schedule("Austin")
    s.addCourse("Math")
    s.addCourse("Comp Sci")

    for c in s.courses:
        print(c)
    

if __name__ == "__main__":
    main()
    
    