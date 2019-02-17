import random


def quick_partition(data):
    if len(data) < 2:
        return -1

    key = random.choice(data)
    print(key)
    i = -1
    for j in range(0, len(data)):
        if j-i > 1:
            if data[j] < key:
                i += 1
                data[j], data[i] = data[i], data[j]
        else:
            if data[j] < key:
                i = i+1
        print(data)
    if i == -1:
        return quick_partition(data)
    return i


def quickSort(data):
    partition = quick_partition(data)
    if partition != -1:
        data[:partition+1] = quickSort(data[:partition+1])
        data[partition+1:] = quickSort(data[partition+1:])
    return data


input = [5, 4, 7, 10, 8, 9, 2, 1, 3, 6]
result = quickSort(input)
print(result)
