a1, a2 = map(int, raw_input().split())
array1 = sorted(map(int, raw_input().split()))
array2 = map(int, raw_input().split())

def binarySearch(i, j, k, array):
    if i == j or j < i:
        return i if array[i] > k else i + 1
    else:
        middle = (i + j) / 2
        if array[middle] <= k:
            return binarySearch(middle + 1, j, k, array)
        else:
            if array[middle -  1] <= k:
                return middle
            return binarySearch(i, middle - 1, k, array)

numbers = map(lambda k: str(binarySearch(0, a1 - 1, k, array1)), array2)

print " ".join(numbers)