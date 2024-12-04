first_column, second_column = [], []
distance = 0

with open('day_1.txt', 'r') as file:
    for line in file:
        first_column.append(line[0:5])
        second_column.append(line[8:13])

# first_column = sorted(first_column)
# second_column = sorted(second_column)
#
# for i in range(len(first_column)):
#     difference = abs(int(first_column[0]) - int(second_column[0]))
#     distance += difference
#     first_column.remove(first_column[0])
#     second_column.remove(second_column[0])
#
# print(distance)

for i in first_column:
    repetition = second_column.count(i)
    answer = int(i) * int(repetition)
    distance += answer

print(distance)