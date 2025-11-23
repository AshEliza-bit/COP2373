import numpy as np

#compute statistics for a column of exam scores
def compute_stats(scores):
    return {
        "mean": np.mean(scores),
        "median": np.median(scores),
        "stddev": np.std(scores),
        "min": np.min(scores),
        "max": np.max(scores)
    }

#counts passes and failures
def pass_fail(scores):
    passed = np.sum(scores >= 60)
    failed = np.sum(scores < 60)
    return passed, failed

#main program

data = np.genfromtxt(
    "grades.csv",
    delimiter=",",
    dtype=None,
    encoding="utf-8",
    names=True
)

print("First few rows of dataset:")
print(data[:5])

#extract exam columns
exam1 = data["exam1"]
exam2 = data["exam2"]
exam3 = data["exam3"]

exam1_stats = compute_stats(exam1)
exam2_stats = compute_stats(exam2)
exam3_stats = compute_stats(exam3)

print("Exam 1 stats:", exam1_stats)
print("Exam 2 stats:", exam2_stats)
print("Exam 3 stats:", exam3_stats)

#overal stats
all_scores = np.concatenate([exam1, exam2, exam3])

overall_stats = compute_stats(all_scores)

print("Overall statistics of all exams:", overall_stats)

#pass/fail per exam
p1, f1 = pass_fail(exam1)
p2, f2 = pass_fail(exam2)
p3, f3 = pass_fail(exam3)

print(f"Exam 1 - Passes: {p1}, Failed: {f1}")
print(f"Exam 2 - Passes: {p2}, Failed: {f2}")
print(f"Exam 3 - Passes: {p3}, Failed: {f3}")

#pass percentage overall

total_scores = len(all_scores)
total_passes = np.sum(all_scores >= 60)
overall_pass_percent = (total_passes / total_scores) * 100

print(f"Overall Pass Percentage: {overall_pass_percent:.2f}%")

