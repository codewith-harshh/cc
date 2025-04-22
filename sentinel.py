def sentinel_search():
    print("Enter numbers one by one. Type 'done' to stop entering numbers.")

    numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    if not numbers:
        print("No numbers were entered.")
        return

    try:
        target = int(input("Enter the number to search for: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Sentinel search
    numbers.append(target)  # Sentinel
    index = 0

    while numbers[index] != target:
        index += 1

    # Remove the sentinel
    numbers.pop()

    if index == len(numbers):
        print(f"{target} was not found in the list.")
    else:
        print(f"{target} found at position {index}.")

# Run the function
sentinel_search()

