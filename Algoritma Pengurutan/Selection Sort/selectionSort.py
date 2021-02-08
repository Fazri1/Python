# Algoritma Sorting
# Kompleksitas 0(N**2)

def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


a = [1, 5, 2, 7, 4, 9, 8]
selectionSort(a)
print(a)
