"""
A simple python script to reverse an array.
"""

def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6,7]
    print("Original Array",arr)
    reverseArray(arr)
    print("Reversed Array",arr)

"""
# Output

    Original Array [1, 2, 3, 4, 5, 6, 7]
    Reversed Array [7, 6, 5, 4, 3, 2, 1]
"""