import numpy as np

# 🎓 Step 1: Create a 2D array for grades (3 students × 4 subjects)
grades = np.array([
    [85, 90, 78, 92],   # Student 1
    [70, 88, 84, 75],   # Student 2
    [90, 93, 89, 96]    # Student 3
])

# 🎯 Step 2: Calculate statistics
overall_mean = np.mean(grades)
overall_median = np.median(grades)
overall_std = np.std(grades)
overall_var = np.var(grades)

# 🎯 Step 3: Calculate per-student and per-subject averages
student_avg = np.mean(grades, axis=1)  # mean across each row
subject_avg = np.mean(grades, axis=0)  # mean across each column

# 🎯 Step 4: Display results
print("📊 GRADE TRACKER STATISTICS")
print("-----------------------------")
print("Grades Table:\n", grades)
print("\nAverage per Student:", student_avg)
print("Average per Subject:", subject_avg)
print("\nOverall Mean:", overall_mean)
print("Overall Median:", overall_median)
print("Standard Deviation:", overall_std)
print("Variance:", overall_var)
