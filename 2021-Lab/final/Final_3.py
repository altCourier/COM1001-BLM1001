
names = {}

with open("notlar.txt", "r") as file:
    for line in file:
        name, grades = line.split(":")
        name.strip()
        grades = grades.split(",")

        for grade in grades:
            grade = eval(grade.strip())
            if grade < 1:
                names[name] = "Failed"
            elif not names.get(name) and grade >= 1:
                names[name] = "Passed"

print("Students who have passed:")
for key in sorted(names):
    if names[key] == "Passed":
        print(key.strip(), end="")
        print(", ", end="")
print()
print("\nStudents who have failed: ")
for key in sorted(names):
    if names[key] == "Failed":
        print(key.strip(), end="")
        print(", ", end="")
                
# I am too lazy to fix the issue of printment of , at the end...