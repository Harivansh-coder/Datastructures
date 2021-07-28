"""
A simple python script for array rotation.
Time complexity = O(n)
n = number of elements in the array
"""
def ArrayRotation(arr,step):
    temp = []

    for i in range(step, len(arr)):
        temp.append(arr[i])

    for i in range(step):
        temp.append(arr[i])
        
    return temp


if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7]

    step = int(input("Enter the number of step of rotation: "))

    rotatedArray = ArrayRotation(arr, step)
    print("Before rotation: ",arr)
    print("After rotation:",rotatedArray)

"""
# Output:
    Enter the number of step of rotation: 1
    Before rotation:  [1, 2, 3, 4, 5, 6, 7]
    After rotation: [2, 3, 4, 5, 6, 7, 1]


    Enter the number of step of rotation: 5
    Before rotation:  [1, 2, 3, 4, 5, 6, 7]
    After rotation: [6, 7, 1, 2, 3, 4, 5]
"""