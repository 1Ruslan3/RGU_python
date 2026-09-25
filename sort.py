def bubblesort(data: list[int]) -> None:
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if (data[j+1] < data[j]):
                data[j+1], data[j] = data[j], data[j+1]


def insertsort(data: list[int]) -> None:
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current

def heapify(data: list[int], n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and data[l] > data[largest]:
        largest = l

    if r < n and data[r] > data[largest]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heapsort(data: list[int]) -> None:
    n = len(data)
    for i in range(n, -1, -1):
        heapify(data, n, i)

    for i in range(n-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

import random
data = [5, 3, 34, 12, 76, 89, 45]

for i in range(100000):
    data.append(random.randint(2000, 500000))

heapsort(data)
print(data)