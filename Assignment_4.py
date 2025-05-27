class Dept:
    def __init__(self, dept_id, name, loc, hod):
        self.dept_id = dept_id
        self.name = name
        self.loc = loc
        self.hod = hod
    
    def show(self):
        print(f"\nDept ID: {self.dept_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.loc}")
        print(f"HOD: {self.hod}")

depts = []
n = int(input("No. of depts: "))

for i in range(n):
    dept_id = input("Dept ID: ")
    name = input("Dept Name: ")
    loc = input("Location: ")
    hod = input("HOD: ")
    depts.append(Dept(dept_id, name, loc, hod))

print("\n------All Depts------:")
for d in depts:
    d.show()

print(f"\nTotal Depts: {len(depts)}")

id = input("\nSearch Dept ID: ")
found = False
for d in depts:
    if d.dept_id == id:
        d.show()
        found = True
        break
if not found:
    print("Dept ID not found")

name = input("\nSearch Dept Name: ")
for d in depts:
    if name.lower() in d.name.lower():
        d.show()
        found = True
        break
if not found:
    print("Dept not found")

