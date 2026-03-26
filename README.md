# Lab 1 - Grade Evaluator & Archiver
This project calculates a student's final grades from a CSV file and automates archival of the data. It includes a Python script ("grade-evaluator.py") that reads "grades.csv", calculates weighted totals, GPA, pass/fail status, and lists assignments eligible for resubmission, and a Bash script ("organizer.sh") that archives the current "grades.csv" with a timestamp, creates a new empty CSV, and logs all archival actions.  

## How to Run
### Python Script
1. Ensure "grades.csv" is in the project folder.  
2. Open a terminal in the folder and run: "py grade-evaluator.py" 
3. Enter "grades.csv" when prompted. The script will print totals, GPA, pass/fail status, and resubmission assignments.  

### Bash Script
1. Open Git Bash in the project folder.  
2. (First time only) run "chmod +x organizer.sh"  
3. Run "./organizer.sh". It will create "archive/" if needed, move and rename "grades.csv" with a timestamp, create a new empty "grades.csv", and log the operation in "organizer.log".  

## Notes
- Weighted totals: Formative 60%, Summative 40%. Passing requires ≥50% in both categories.  
- Failed formative assignments with the highest weight are listed for resubmission.  
- The Bash script ensures data is safely archived and the workspace is ready for new input.  
- Calculations in Python are done using loops; no built-in sorting is used.  
