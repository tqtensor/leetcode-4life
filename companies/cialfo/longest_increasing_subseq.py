from bisect import bisect_left


def ArrayChallenge(arr: list) -> int:
    n = len(arr)
    for i in range(n):
        idx = bisect_left(arr, arr[i], hi=i)
        if idx != i:
            arr[idx], arr[i] = arr[i], float("inf")
    arr = arr.index(float("inf")) if float("inf") in arr else n
    return arr


# keep this function call here
print(ArrayChallenge(input()))
