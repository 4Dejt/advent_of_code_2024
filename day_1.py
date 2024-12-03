first_column, second_column = [], []
# distance = 0

with open('day_1.txt', 'r') as file:
    for line in file:
        first_column.append(line[0:5])
        second_column.append(line[8:13])

# first_column = sorted(first_column)
# second_column = sorted(second_column)
#
#
# for i in range(len(first_column)):
#     difference = int(first_column[0]) - int(second_column[0])
#     distance += difference
#     first_column.remove(first_column[0])
#     second_column.remove(second_column[0])
#
# print(distance)

smallest_1 = int(min(first_column))
smallest_2 = int(min(second_column))

def get_distance(first_column, second_column, smallest_1, smallest_2):
    distance = 0

    
    difference = int(abs(smallest_1 - smallest_2))
    distance += difference