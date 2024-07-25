grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_alphabet = tuple(sorted(students)) # перевод в кортеж в алфавитном порядке - для составления словаря нужен хэшируемый тип данных
grades.reverse() # для использования в дальнейшем метода "pop" с целью вызова оценок из списка "переворачиваем" последовательность

gpa = [] # GPA (Grade Point Average) - средний балл, создаем список для расчета и накопления значений GPA для каждого студента

for i in grades[0:5]: # :( не смог найти КРАТКОЕ решение для автоматического определения длины коллекции (если будет не 5, а другое количество студентов)
    gpa_i = grades.pop() # промежуточная переменная для поочередного расчета и вывода GPA
    gpa_i = [sum(gpa_i) / len(gpa_i)]
    gpa.extend(gpa_i) # накапливаем GPA в общий список

dict_gpa = {}
for i in range(len(students_alphabet)):
    dict_gpa[students_alphabet[i]] = gpa[i]
print(dict_gpa)