#implement binary search
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#implement merge sort
def merge(list, start, mid, end):
    left = list[start:mid + 1]
    right = list[mid + 1:end + 1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(start, end + 1):
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
    return list

def merge_sort(list, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid + 1, end)
        merge(list, start, mid, end)
    return list

if __name__ == '__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    arr = merge_sort(arr, 0, len(arr) - 1)
    print(arr)
    print(binary_search(arr, 1))