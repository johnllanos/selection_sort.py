arr = [100,48,70,29,2,17]
#Setting our array values in mixed order
def selection_sort(arr):
    for i in range(len(arr)):
        # Entering our for loop above and fiding our minimum value below
        min = i
        # Once we have established our minimum value lets look to the rest of the array of numbers to compare
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                # Once a smaller number is encountered we can establish our new minimum, and we will continue to seek out a new minimum until we exit this for loop.
                min = j
        # Once we return to the initial for loop we can swap out positions and move forward as our variable increments
        arr[i] , arr[min] = arr[min], arr[i]
        # We'll print out along the way and see how things are moving.
        print(arr)
            
            

selection_sort(arr)