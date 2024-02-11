def StockPicker(arr):
    n = len(arr)

    if n < 2:
        return -1  # Not enough days to make a profit

    max_profit = 0
    current_profit = 0

    for i in range(1, n):
        current_profit = max(0, current_profit + arr[i] - arr[i-1])
        max_profit = max(max_profit, current_profit)

    return max_profit if max_profit > 0 else -1

# Take input from the user
input_string = input("Enter numbers separated by commas: ")
arr = [int(element) for element in input_string.split(",")]

# Call the function and print the result
max_profit = StockPicker(arr)
print("Max Profit:", max_profit)
