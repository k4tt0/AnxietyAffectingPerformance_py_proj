Final Project

## Research-backed modeling and simulation

Create a model backed up by scientific / empirical data. This includes study cases research work, data accumulated throughout time on a given subject (likely structured in one or multiple datasets), physical phenomena mapped into ideal mathemathical formulas, etc.
The two main points of interest for this project are:
1. Finding your own topic of interest to model and simulate
2. Extracting meaningful relevant information from reliable resources to set as the core of your model (in contrast to naive assumptions used in the previous two projects).


### Project Requirements:
* Use 2 external resources in designing the core concepts / mechanisms / probabilities of your model
    - an external resource is a scientific article, a published paper, a public dataset, a scientific journal, etc.

    E.g. Can design a model starting from meaningful insights extracted from 1. a scientific paper on bear breeding patterns combined with 2. data extracted from a dataset tracking bear population across a region.

    Can also opt for combining information from 2 different scientific articles, or combining information from 2 different datasets instead.
    - each of the external resources needs to be cited (title + authors if known)

* Build your model using **either** **pygame** or **simpy**, depending on which best matches your planned simulations.
* document all the insights that you have extracted from your external resources (either written in a text cell, or being able to explain them when presenting the project) - e.g. We've decided to set the rabbit velocity to X and fox velocity to Y given that article Z presents these numbers for their respective top speeds.
* incorporate 2 visual presentations of your simulations
    - for simpy use 2 plots
    - for pygame use the pygame window for visualization + 1 plot
* simulate two meaningful scenarios for your model
    - e.g. for a disease spread model two possible simulations could be A. simulate spread in country A vs B. simulate spread in country B. It could just as well be spread of disease A vs spread of disease B (each with their own intrinsic characteristics).



## How anxiety can affect a student's performance

**Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health, Resilience and Behavior of College Students during the Pandemic**

*Authors: Subigya Nepal, Dartmouth College, USA; Wenjun Liu, Dartmouth College, USA; Arvind Pillai, Dartmouth College, USA; Weichen Wang, Dartmouth College, USA; Vlado Vojdanovski, Dartmouth College, USA; Jeremy F. Huckins, Biocogniv Inc, USA; Courtney Rogers, Dartmouth College, USA; Meghan L. Meyer, Columbia University, USA; Andrew T. Campbell, Dartmouth College, USA*

**Investigating the effects of stress on achievement: BIOSTRESS dataset**

*Authors: Çağla Çöpürkaya, Elif Meriç, Elif Berra Erik, Büşra Kocaçınar, Fatma Patlar Akbulut, Cagatay Catal*

### Datasets

**BIOSTRESS Dataset**: This dataset provides data on psychological stressors (stress levels, heart rate, sleep quality, and self-reported stress), which might be linked to academic performance.

**StudentLife Study Dataset**: This dataset includes data from college students on mental health (including anxiety), behavior, academic performance, and smartphone usage. It also includes physiological data from wearable sensors, which can provide insight into how anxiety and stress impact academic performance.

## How anxiety can affect a student's performance

### Introduction and Objectives

Understanding how anxiety affects student performance is crucial for developing effective interventions and support systems. This project aims to model the impact of anxiety on academic performance using data from two external resources: `Mental-health-students.pdf` and `stress-on-achievements.pdf`.

**Objectives:**
- Identify key factors influencing student performance related to anxiety.
- Extract meaningful data from the provided resources.
- Implement a simulation model to analyze the impact of anxiety on student performance.
- Visualize the results and discuss the implications.

### Background Information

Anxiety is a common mental health issue among students, which can significantly impact their academic performance. High levels of anxiety can lead to decreased concentration, memory problems, and lower grades. Understanding the relationship between anxiety and academic performance can help in developing strategies to support students.

**Key Concepts:**
- **Anxiety Levels**: Measures of anxiety, typically on a scale (e.g., 1 to 10).
- **Academic Performance**: Metrics such as grades, attendance, and study hours.
- **Coping Mechanisms**: Strategies used by students to manage anxiety, such as exercise and meditation.
- **Support Systems**: Availability of resources like counseling services and peer support.

  ### Selecting Key Parameters

To model the impact of anxiety on student performance, we will focus on the following components:

- **Anxiety Levels**: A measure of the student's anxiety, typically on a scale (e.g., 1 to 10).
- **Grades**: The primary measure of academic performance.
- **Attendance**: The number of classes attended by the student.
- **Study Hours**: The number of hours a student spends studying per week.
- **Coping Mechanisms**: Information on whether the student uses coping mechanisms such as exercise, meditation, etc.
- **Support Systems**: Availability of support systems like counseling services, peer support, etc.

### Extracting Data from Mental-health-students.pdf

From the paper **"Capturing the College Experience: A Four-Year Mobile Sensing Study of Mental Health, Resilience and Behavior of College Students during the Pandemic"** by Subigya Nepal et al., we extract the following key insights and data points:

1. **Anxiety Levels**:
   - Average anxiety level: 5 on a scale of 1 to 10.
   - Standard deviation: 2.

2. **Coping Mechanisms**:
   - Students using coping mechanisms have lower anxiety levels (average of 4).
   - Common coping mechanisms include exercise and meditation.

3. **Support Systems**:
   - Availability of support systems like counseling services and peer support.
   - Negative correlation (-0.3) between support systems and anxiety levels.

4. **Academic Performance**:
   - Average grade: 75 with a standard deviation of 10.
   - Positive correlation (0.4) between attendance and grades.
   - Students who study more than 10 hours per week have an average grade of 80.

### Extracting Data from stress-on-achievements.pdf

From the paper **"Investigating the effects of stress on achievement: BIOSTRESS dataset"** by Çağla Çöpürkaya et al., we extract the following key insights and data points:

1. **Stress Levels**:
   - High stress levels are associated with lower academic achievements.
   - Stress negatively impacts cognitive functions such as memory and concentration.

2. **Physiological Data**:
   - Data such as heart rate and sleep quality, which can impact academic performance.
   - Self-reported stress levels correlate with academic performance.

3. **Academic Performance**:
   - Students with high stress levels have an average grade of 65.
   - Students with low stress levels have an average grade of 80.
  
### Example of Data Extraction and Parameter Selection

Let's consider the following parameters for our simulation model:

- **Anxiety Levels**: Average anxiety level is 5 with a standard deviation of 2.
- **Grades**: Average grade is 75 with a standard deviation of 10.
- **Attendance**: Positive correlation (0.4) between attendance and grades.
- **Study Hours**: Students who study more than 10 hours per week have an average grade of 80.
- **Coping Mechanisms**: Students using coping mechanisms have lower anxiety levels (average of 4).
- **Support Systems**: Negative correlation (-0.3) between support systems and anxiety levels.
- **Stress Levels**: High stress levels are associated with lower academic achievements.
- **Physiological Data**: Data such as heart rate and sleep quality, which can impact academic performance.

""" From Mental-health-students.pdf:

    Average anxiety level: 5 (scale 1 to 10)
    Standard deviation of anxiety levels: 2
    Students using coping mechanisms have lower anxiety levels (average of 4)
    Negative correlation (-0.3) between support systems and anxiety levels
    Average grade: 75
    Standard deviation of grades: 10
    Positive correlation (0.4) between attendance and grades
    Students who study more than 10 hours per week have an average grade of 80

    
    From stress-on-achievements.pdf:

    High stress levels are associated with lower academic achievements
    Stress negatively impacts cognitive functions such as memory and concentration
    Students with high stress levels have an average grade of 65
    Students with low stress levels have an average grade of 80 
"""

