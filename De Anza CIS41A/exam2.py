import csv


studentRecords = {}



try:
    with open("records.csv", "r") as file:
        reader = csv.reader(file)

        
        next(reader)

        for row in reader:
            try:
                studentId = row[0]
                name = row[1]
                year = int(row[2])
                course = row[3]
                score = float(row[4])
                grade = row[5]

                record = {
                    "name": name,
                    "year": year,
                    "course": course,
                    "score": score,
                    "grade": grade
                }

                if studentId not in studentRecords:
                    studentRecords[studentId] = []

                studentRecords[studentId].append(record)

            except (ValueError, IndexError):
                print("Error processing row:", row)

except FileNotFoundError:
    print("Error: records.csv not found.")

except IOError:
    print("Error reading file.")




def printLastNamesByLetter(records, letter):
    print(f"Last names beginning with '{letter}':")

    found = False

    for studentId in records:
        for record in records[studentId]:

            fullName = record["name"]
            nameParts = fullName.split()

            if len(nameParts) > 1:
                lastName = nameParts[-1]

                if lastName.lower().startswith(letter.lower()):
                    print(lastName)
                    found = True

    if not found:
        print("No matching last names found.")



def countStudentsWithGrade(records, courseName, gradeValue):
    count = 0

    for studentId in records:
        for record in records[studentId]:

            if (record["course"] == courseName and
                    record["grade"] == gradeValue):
                count += 1

    print(f"Students in {courseName} with grade {gradeValue}: {count}")



def calculateCourseAverage(records, courseName):
    scores = []

    for studentId in records:
        for record in records[studentId]:

            if record["course"] == courseName:
                scores.append(record["score"])

    if len(scores) == 0:
        return 0.0

    average = sum(scores) / len(scores)
    return average




printLastNamesByLetter(studentRecords, "S")

countStudentsWithGrade(studentRecords, "CIS 41A", "B")

average = calculateCourseAverage(studentRecords, "CIS 41A")
print("Average score:", average)