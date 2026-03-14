Student Report Analyzer Using Python

Overview
This project is a simple student report analyzer built using Python along with the NumPy and Pandas libraries. The program organizes student marks in different subjects, calculates their average score, determines whether they pass or fail, assigns grades, and identifies top performing students. The purpose of this project is to practice data analysis concepts that are commonly used in data science.

Objective
The main objective of this project is to demonstrate how basic student data can be analyzed programmatically using Python. It shows how tabular data can be created, processed, and analyzed using Pandas DataFrames.

Technologies Used
Python
NumPy
Pandas

Features
Stores student names and subject marks in a structured dataset
Creates a Pandas DataFrame from the dataset
Calculates the average marks of each student across subjects
Rounds the calculated averages to two decimal places
Determines pass or fail status based on the average score
Assigns grades based on defined score ranges
Displays students who achieved grade A
Sorts students based on average marks and displays the top performers

Grading Logic
Students are graded according to their average marks

Average greater than or equal to 75 results in Grade A
Average greater than or equal to 60 and less than 75 results in Grade B
Average greater than or equal to 40 and less than 60 results in Grade C
Average below 40 results in Fail

Project Workflow
Student names and marks are stored in Python lists
The lists are converted into a dictionary
The dictionary is used to create a Pandas DataFrame
The program calculates the average marks of each student
The result column identifies whether the student passed or failed
The grade column assigns grades using conditional logic
The program identifies grade A students as top performers
The DataFrame is sorted to display the top three students based on average marks

Learning Outcome
This project helps in understanding how data analysis workflows operate using Python. It introduces practical usage of Pandas DataFrames, conditional operations using NumPy, data sorting, and simple reporting systems. These concepts form a foundation for larger data science and analytics projects.

Author
Uday Bhaskar
Aspiring Data Science Learner focusing on Python, NumPy, Pandas, and practical data analysis projects.
