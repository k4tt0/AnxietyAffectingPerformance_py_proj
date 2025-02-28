import simpy
import numpy as np
import matplotlib.pyplot as plt

# Parameters extracted from the papers
average_anxiety = 5
std_anxiety = 2
average_grade = 75
std_grade = 10
attendance_correlation = 0.4
study_hours_threshold = 10
high_stress_grade = 65
low_stress_grade = 80

# Adjusted parameters based on external resources
coping_reduction = 0.5  # Reduction in anxiety due to coping mechanisms
support_reduction = 0.5  # Reduction in anxiety due to support systems
burnout_study_hours = 20  # Threshold for extreme study hours leading to burnout

class Student:
    
    def __init__(self, env, id, anxiety_level, study_hours, uses_coping_mechanisms, has_support_system):
        self.env = env
        self.id = id
        self.anxiety_level = anxiety_level
        self.study_hours = study_hours
        self.uses_coping_mechanisms = uses_coping_mechanisms
        self.has_support_system = has_support_system
        self.adjust_anxiety_level()
        self.grade = self.calculate_grade()
        self.attendance = self.calculate_attendance()

    def adjust_anxiety_level(self):
        """
        Adjust the anxiety level based on coping mechanisms and support systems.
        """
        if self.uses_coping_mechanisms:
            self.anxiety_level -= coping_reduction  # Coping mechanisms reduce anxiety
        if self.has_support_system:
            self.anxiety_level -= support_reduction  # Support systems reduce anxiety
        self.anxiety_level = max(0, self.anxiety_level)  # Ensure anxiety level is not negative

    def calculate_grade(self):
        """
        Calculate the grade based on the anxiety level and coping mechanisms.
        """
        if self.study_hours > burnout_study_hours:
            return np.random.normal(high_stress_grade, std_grade)  # Burnout due to extreme study hours
        elif self.anxiety_level > 7:
            return np.random.normal(high_stress_grade, std_grade)
        elif self.uses_coping_mechanisms:
            return np.random.normal(low_stress_grade, std_grade)
        else:
            return np.random.normal(average_grade, std_grade)

    def calculate_attendance(self):
        """
        Calculate the attendance based on the anxiety level.
        """
        return np.random.normal(75 + self.anxiety_level * attendance_correlation, 10)

# Create the simulation environment
env = simpy.Environment()

def create_students(env, num_students, high_anxiety=False, effective_coping=False, partial_coping=False, extreme_study_hours=False):
    """
    Create a list of students with specified attributes.
    
    """
    students = []
    for i in range(num_students):
        if high_anxiety:
            anxiety_level = np.random.normal(7, std_anxiety)
        else:
            anxiety_level = np.random.normal(average_anxiety, std_anxiety)
        if extreme_study_hours:
            study_hours = np.random.randint(burnout_study_hours, burnout_study_hours + 5)
        else:
            study_hours = np.random.randint(5, 15)
        uses_coping_mechanisms = effective_coping or partial_coping
        has_support_system = effective_coping
        student = Student(env, i, anxiety_level, study_hours, uses_coping_mechanisms, has_support_system)
        students.append(student)
    return students

# Scenario 1: High anxiety levels with no coping mechanisms
students_scenario1 = create_students(env, 100, high_anxiety=True, effective_coping=False)

# Scenario 2: Low anxiety levels with effective coping mechanisms
students_scenario2 = create_students(env, 100, high_anxiety=False, effective_coping=True)

# Scenario 3: High anxiety levels with partial coping mechanisms
students_scenario3 = create_students(env, 100, high_anxiety=True, partial_coping=True)

# Scenario 4: Impact of extreme study hours (burnout)
students_scenario4 = create_students(env, 100, high_anxiety=False, effective_coping=False, extreme_study_hours=True)

def collect_data(students):
    """
    Collect data from a list of students.
    """
    grades = [student.grade for student in students]
    attendances = [student.attendance for student in students]
    anxiety_levels = [student.anxiety_level for student in students]
    return grades, attendances, anxiety_levels

grades_scenario1, attendances_scenario1, anxiety_levels_scenario1 = collect_data(students_scenario1)
grades_scenario2, attendances_scenario2, anxiety_levels_scenario2 = collect_data(students_scenario2)
grades_scenario3, attendances_scenario3, anxiety_levels_scenario3 = collect_data(students_scenario3)
grades_scenario4, attendances_scenario4, anxiety_levels_scenario4 = collect_data(students_scenario4)

# Calculate summary statistics
def print_summary_statistics(grades, attendances, anxiety_levels, scenario_name):
    """
    Print summary statistics for grades, attendance, and anxiety levels.
    """
    print(f"Summary Statistics for {scenario_name}:")
    print(f"Grades - Mean: {np.mean(grades):.2f}, Median: {np.median(grades):.2f}, Std Dev: {np.std(grades):.2f}")
    print(f"Attendance - Mean: {np.mean(attendances):.2f}, Median: {np.median(attendances):.2f}, Std Dev: {np.std(attendances):.2f}")
    print(f"Anxiety Levels - Mean: {np.mean(anxiety_levels):.2f}, Median: {np.median(anxiety_levels):.2f}, Std Dev: {np.std(anxiety_levels):.2f}")
    print()

print_summary_statistics(grades_scenario1, attendances_scenario1, anxiety_levels_scenario1, "Scenario 1: High Anxiety, No Coping")
print_summary_statistics(grades_scenario2, attendances_scenario2, anxiety_levels_scenario2, "Scenario 2: Low Anxiety, Effective Coping")
print_summary_statistics(grades_scenario3, attendances_scenario3, anxiety_levels_scenario3, "Scenario 3: High Anxiety, Partial Coping")
print_summary_statistics(grades_scenario4, attendances_scenario4, anxiety_levels_scenario4, "Scenario 4: Extreme Study Hours (Burnout)")

# Redoing the visualizations for better clarity and understanding

def plot_histogram(data, labels, title, xlabel, ylabel, bins=10, alpha=0.7, figsize=(10, 6), colors=None, edgecolor='black'):
    plt.figure(figsize=figsize)
    for i, d in enumerate(data):
        color = colors[i] if colors else None
        plt.hist(d, bins=bins, alpha=alpha, label=labels[i], color=color, edgecolor=edgecolor)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_violinplot(data, labels, title, ylabel, figsize=(10, 6), colors=None):
    plt.figure(figsize=figsize)
    parts = plt.violinplot(data, showmeans=True, showmedians=True)
    if colors:
        for pc, color in zip(parts['bodies'], colors):
            pc.set_facecolor(color)
            pc.set_edgecolor('black')
            pc.set_alpha(0.7)
    plt.xticks(ticks=range(1, len(labels) + 1), labels=labels)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage with custom colors
data_labels = [
    'High Anxiety, No Coping', 
    'Low Anxiety, Effective Coping', 
    'High Anxiety, Partial Coping', 
    'Extreme Study Hours'
]

grades_data = [grades_scenario1, grades_scenario2, grades_scenario3, grades_scenario4]
attendances_data = [attendances_scenario1, attendances_scenario2, attendances_scenario3, attendances_scenario4]
anxiety_levels_data = [anxiety_levels_scenario1, anxiety_levels_scenario2, anxiety_levels_scenario3, anxiety_levels_scenario4]

colors = ['red', 'green', 'blue', 'purple']

# Plotting grades
plot_histogram(
    grades_data,
    data_labels,
    title='Grade Distributions Across Scenarios',
    xlabel='Grades',
    ylabel='Number of Students',
    colors=colors
)

plot_violinplot(
    grades_data,
    data_labels,
    title='Grade Distribution Comparison Across Scenarios',
    ylabel='Grades',
    colors=colors
)

# Plotting attendance
plot_histogram(
    attendances_data,
    data_labels,
    title='Attendance Distributions Across Scenarios',
    xlabel='Attendance',
    ylabel='Number of Students',
    colors=colors
)

plot_violinplot(
    attendances_data,
    data_labels,
    title='Attendance Distribution Comparison Across Scenarios',
    ylabel='Attendance',
    colors=colors
)

# Plotting anxiety levels
plot_histogram(
    anxiety_levels_data,
    data_labels,
    title='Anxiety Level Distributions Across Scenarios',
    xlabel='Anxiety Levels',
    ylabel='Number of Students',
    colors=colors
)

plot_violinplot(
    anxiety_levels_data,
    data_labels,
    title='Anxiety Level Distribution Comparison Across Scenarios',
    ylabel='Anxiety Levels',
    colors=colors
)