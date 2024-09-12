def findMinArray(arr, k):
    result = []
    while k > 0 and arr:
        # Greedily, we find the smallest element from `arr` and swap it to the front
        minIndex = 0
        for i in range(1, min(k + 1, len(arr))):
            if arr[i] < arr[minIndex]:
                minIndex = i
        # move this element to the front
        k -= minIndex
        result.append(arr[minIndex])
        arr = arr[0: minIndex] + arr[minIndex + 1:]

    return result + arr
