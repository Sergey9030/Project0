grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
print(students)
print(grades)
dict_ = {}
i = 0
dict_.update({students[i]: sum(grades[i])/len(grades[i])})
i = i+1
dict_.update({students[i]: sum(grades[i])/len(grades[i])})
i = i+1
dict_.update({students[i]: sum(grades[i])/len(grades[i])})
i = i+1
dict_.update({students[i]: sum(grades[i])/len(grades[i])})
i = i+1
dict_.update({students[i]: sum(grades[i])/len(grades[i])})
print(dict_)

dict_ = {}
i = 0
for i in range(0, len(grades)):
    dict_.update({students[i]: sum(grades[i])/len(grades[i])})
print(dict_)
