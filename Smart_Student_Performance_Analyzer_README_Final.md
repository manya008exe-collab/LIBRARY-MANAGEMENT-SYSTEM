# Smart Student Performance Analyzer

## Project Overview

This repository contains a beginner-friendly Python command-line project for analyzing student academic performance.

The program takes student details, subject marks, attendance and assignment information as input. It then calculates total marks and percentage, assigns a grade, identifies the performance category, and gives a recommendation based on the subject with the lowest marks.

## Aim

To create a simple Python program that analyzes student performance and provides basic academic feedback using marks, attendance and assignment information.

## Features

- Takes student name and roll number.
- Takes marks for Mathematics, Python and English.
- Calculates total marks and percentage.
- Assigns a grade based on percentage.
- Classifies overall performance.
- Identifies the subject with the lowest marks.
- Gives a recommendation for improvement.
- Checks attendance percentage.
- Displays a warning when attendance is below 75%.
- Checks completed assignments.
- Suggests completing more assignments when fewer than 5 are completed.
- Displays a final student performance report.

## Grade System

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80 to 89 | A |
| 70 to 79 | B |
| 60 to 69 | C |
| 50 to 59 | D |
| Below 50 | F |

## Performance Categories

- **Excellent:** Percentage is 75 or above and attendance is 75% or above.
- **Good:** Percentage is 60 or above and attendance is 60% or above.
- **Needs Improvement:** All other cases.

## Requirements

- Python 3.x
- No external libraries are required.

## Environment Setup

1. Install Python 3 from https://www.python.org/downloads/
2. During installation on Windows, select **Add Python to PATH**.
3. Open a terminal or VS Code.
4. Download or clone this repository.
5. Open the project folder.

## How to Run

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Input Details

The program asks for:

- Student name
- Roll number
- Mathematics marks
- Python marks
- English marks
- Attendance percentage
- Number of completed assignments

## Working

1. Takes student information as input.
2. Takes marks for three subjects.
3. Calculates total marks and percentage.
4. Determines the grade.
5. Checks percentage and attendance.
6. Determines the performance category.
7. Finds the subject with the lowest marks.
8. Displays a recommendation.
9. Checks attendance and assignments.
10. Displays the final performance report.

## Python Concepts Used

The project uses basic Python concepts such as:

- input and output
- variables
- if-elif-else
- comparison operators
- arithmetic operators
- lists
- strings
- simple calculations
- conditional logic

## Project Structure

```text
Smart_Student_Performance_Analyzer/
│
├── main.py
├── README.md
└── PROJECT_REPORT.md
```

## Dependencies

No external dependencies are required. The project uses only standard Python features.

## Testing

The program can be tested using different marks, attendance percentages and assignment counts to verify:

- Grade calculation
- Percentage calculation
- Performance category
- Lowest-mark subject recommendation
- Attendance warning
- Assignment suggestion

## Limitations

- The project runs through the command line.
- Student information is not permanently stored.
- The program currently analyzes three subjects.
- It does not use a database or graphical user interface.

## Future Scope

The project can be improved by adding:

- More subjects
- Student data storage
- Database support
- Graphical user interface
- Multiple student records
- Detailed performance reports
- Automatic report generation

## Project Report

A project report can be included with the repository containing the project explanation, algorithm, pseudocode, flowchart, testing and sample output.

## Author

Name: Anamika Choudhary  
Academic Number: 26BCE11499
Course: Python Essentials
