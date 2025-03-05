# Function to perform linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Take user input for the list
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

# Take user input for the target value
target = int(input("Enter the number to search for: "))

# Perform linear search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
