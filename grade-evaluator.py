import csv
import sys
import os

def load_csv_data():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    formative_total = 0
    summative_total = 0
    resubmit = []
    max_weight_failed = 0

    for a in data:
        score = float(a['score'])
        weight = float(a['weight'])
        if a['group'].lower() == "formative":
            formative_total += score * weight / 100
            if score < 50:
                if weight > max_weight_failed:
                    resubmit = [a['assignment']]
                    max_weight_failed = weight
                elif weight == max_weight_failed:
                    resubmit.append(a['assignment'])
        elif a['group'].lower() == "summative":
            summative_total += score * weight / 100

    final_grade = formative_total + summative_total
    gpa = final_grade / 100 * 5

    print("\n--- Grade Summary ---")
    print(f"Formative Total: {formative_total:.1f}/60")
    print(f"Summative Total: {summative_total:.1f}/40")
    print(f"Final Grade: {final_grade:.1f}/100")
    print(f"GPA: {gpa:.2f}")
    status = "PASSED" if formative_total >= 30 and summative_total >= 20 else "FAILED"
    print(f"Status: {status}")
    if resubmit:
        print("Assignments eligible for resubmission:", ", ".join(resubmit))
    else:
        print("No assignments need resubmission")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)