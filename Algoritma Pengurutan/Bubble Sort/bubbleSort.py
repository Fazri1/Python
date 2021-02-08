# Algoritma Sorting

# best case : array terurut 0(N)
# worse case : array terurut terbalik 0(N**2)

def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break


a = [314, 4, 12, 312, 83, 212, 93, 70]
bubbleSort(a)
print(a)
