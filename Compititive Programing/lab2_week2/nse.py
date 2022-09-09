# find the smallest element for all elements in an array to the right in O(n)
def smallest_element(arr):
    n = len(arr)
    stack = []
    res = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        res[i] = arr[i] - arr[stack[-1]] if stack else 1000000000
        stack.append(i)
    return res

# find the smallest element to the right of each element in an array in O(n)
def smallest_to_right(arr):
    n = len(arr)
    stack = []
    res = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    return res

def brute_force(arr):
    global_shortest = 1000000000
    for i,element in enumerate(arr):
        minu = element
        for j in arr[i:]:
            print(j)
            if element - j < minu and element - j > 0:
                minu = element-j
        if minu < global_shortest:
            global_shortest = minu
    return global_shortest

        
                
            

n = int(input())
arr = [int(elem) for elem in input().split()]
smallest_to_right = smallest_element(arr)
print(brute_force(arr))