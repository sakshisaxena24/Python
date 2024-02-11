def StockPicker(arr):
    min_index = arr.index(min(arr))
    max_value= max(arr[min_index+1:],default=None)

    if max_value is not None:
        return max_value-min(arr)
    else:
        return -1

input_string = input("enter numbers")
arr = [int(element) for element in input_string.split(",")]
print("max profit",StockPicker(arr))


