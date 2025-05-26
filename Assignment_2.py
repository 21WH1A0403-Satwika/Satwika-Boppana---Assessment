university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}
#Q1: Print all student names and their majors
for student in university_data.values():
    print(student["name"], "-", student["major"])


#Q2: Average score per course per student
for student in university_data.values():
    print(student["name"] + ":")
    for course, scores in student["courses"].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course} - {avg:.2f}")


#Q3: Find students who scored >90 in final of Python101
for student in university_data.values():
    if "Python101" in student["courses"]:
        if student["courses"]["Python101"]["final"] > 90:
            print(student["name"])


#Q4: Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 90, "project": 88}
print(university_data["S101"]["courses"])


#Q5: Print average for each course
totals, counts = {}, {}
for s in university_data.values():
    for c, sc in s["courses"].items():
        totals[c] = totals.get(c, 0) + sum(sc.values())
        counts[c] = counts.get(c, 0) + len(sc)
for c in totals:
    print(c, "-", round(totals[c] / counts[c], 2))
