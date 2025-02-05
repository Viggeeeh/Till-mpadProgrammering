def sort(list):
    for _ in range(len(list)):
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

numbers = [5, 3, 10, 2]

print(sort(numbers))