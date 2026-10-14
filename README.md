Sleep, Body Weight and Stress

MAT2007 (Introduction to Programming) project tests whether sleep duration is related to body weight category and whether self-rated stress level predicts how long people sleep. 

Research question: Is sleep duration associated with BMI category, and does stress level predict how long people sleep?

Files in this folder
- newdataanalysis.py - the anaylsis and plotting script
- sleep_health_and_lifestyle.csv - the input data
- boxplot_sleep_by_bmi.png - output, made by newdataanalysis.py
- scatter_stress_vs_sleep.png - output, made by newdataanalysis.py
- Programming_Project.pdf - report

Installation and dependencies:
- Install Python 3
- Install the required packages: pandas, numpy, scipy, matplotlib

How to run:
1. Install VS Code and Python, then add the Python extension in VS Code (from the Extensions panel).
2. Open this folder in VS Code and open a terminal (Ctrl+`).
3. Install the packages: 
python3 -m pip install pandas numpy scipy matplotlib
4. Run the script:
python3 newdataanalysis.py
This will read the CSV file, merge the duplicate BMI label, compute median sleep duration per BMI category, run the Spearman correlation between stress level and sleep duration, print the results and save the two PNG files.

Conditions: no internet connection is needed to run the script, since the dataset is already included as a CSV file in this folder. The script must be run from inside this folder since it reads sleep_health_and_lifestyle.csv using a relative path.

Dataset
The dataset is sleep_health_and_lifestyle.csv, included in this folder. It is a public dataset from Kaggle, called the "Sleep Health and Lifestyle Dataset":
https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset

It has 374 adults and 13 columns, including sleep duration, sleep quality, blood pressure, BMI category, etc. This project only uses three columns: Sleep Duration, Stress Level and BMi Category. No rows are missing any of these three.
One cleaning step: BMI Category has two labels, "Normal" and "Normal Weight", for the same group so these were merged into one "Normal" category before analysis. After merging, "Normal" has 216 people, "Overweight" has 148 and "Obese" has 10.
