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
                score = int(row[4])
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
    print("Error: records.csv was not found.")

except PermissionError:
    print("Error: Permission denied when accessing the file.")

except IOError:
    print("Error: Problem reading the file.")


for studentId, records in studentRecords.items():
    print(studentId, records)