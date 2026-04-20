student_grades = {
    "Aram Petrosyan": [78, 85, 92, 88],
    "Nareh Mkrtchyan": [65, 70, 58, 62],
    "Vahan Grigoryan": [90, 95, 88, 93],
    "Lusine Harutyunyan": [45, 52, 49, 55],
    "Sona Khachatryan": [82, 77, 80, 85],
    "Tigran Manukyan": [70, 68, 72, 75],
    "Ani Karapetyan": [88, 91, 85, 90],
    "David Hovhannisyan": [55, 60, 58, 62],
    "Mariam Ghazaryan": [77, 79, 81, 78],
    "Arsen Babayan": [92, 95, 90, 94],
    "Elena Sargsyan": [60, 62, 65, 68],
    "Levon Vardanyan": [85, 80, 87, 82],
    "Hasmik Stepanyan": [50, 55, 52, 48],
    "Karen Harutyunyan": [73, 75, 70, 72],
    "Suren Avetisyan": [66, 68, 64, 65],
    "Lilit Khachatryan": [89, 92, 90, 88],
    "Vahagn Margaryan": [58, 60, 55, 57],
    "Narine Melikyan": [80, 85, 83, 82],
    "Gor Movsesyan": [47, 50, 45, 48],
    "Astghik Danielyan": [91, 95, 93, 94]
}
best_student = ""
max_average = 0
for i, j in student_grades.items():
    average = sum(j) / 4
    if average > max_average:
        max_average = average
        best_student = i
print(f"Best average student is: {best_student}")


count_80 = 0
for i, j in student_grades.items():
    average = sum(j) / 4
    if average > 80:
        count_80 += 1
print(f"Average above 80 is: {count_80}")

count_60 = 0
for i, j in student_grades.items():
    average = sum(j) / 4
    if average < 60:
        count_60 += 1
print(f"Average bellow 60 is: {count_60}")