arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input("enter the numbers"))
    arr.append(element)
print(arr)
x=int(input("enter your item: "))
def binarySearch(arr, x):
    if arr != sorted(arr):
        print("You entered unsorted list {}..., The sorted list is:".format(arr))
        arr.sort()
        print(arr)
    low=0
    high=len(arr)-1
    while low <= high :
        mid = (low+high) // 2
        if arr[mid] == x:
            print("the search element",x, "pos is: ",mid)
            break
        elif x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
    if x != arr[mid]:
        print('Searched item in not in the list, Inserting it into {}'.format(arr))
        arr.append(x)
        arr.sort()
        print("Updated list is : ", arr)
binarySearch(arr, x)
