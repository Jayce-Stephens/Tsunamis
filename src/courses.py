from dataclasses import dataclass
from typing import List
import csv
from pathlib import Path

@dataclass
class Course:
    subject: str
    number: str
    title: str
    crn: str
    prerequisites: str
    add_deadline: str
    drop_deadline: str

def load_courses(csv_path: str) -> List[Course]:
   
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Cannot find file: {csv_path}")

    courses: List[Course] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            courses.append(
                Course(
                    subject=row["subject"].upper(),
                    number=row["number"],
                    title=row["title"],
                    crn=row["crn"],
                    prerequisites=row["prerequisites"],
                    add_deadline=row["add_deadline"],
                    drop_deadline=row["drop_deadline"],
                )
            )
    return courses

def filter_by_subject(courses: List[Course], subject: str) -> List[Course]:
    subject = subject.strip().upper()
    return [c for c in courses if c.subject == subject]
