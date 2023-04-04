def max_sum(numbers):
    length = len(numbers)

    if length < 2:
        return 0

    sorted_numbers = sorted(numbers, reverse=True)
    max_sum = sorted_numbers[0] + sorted_numbers[1]

    return max_sum


print(max_sum([5, 11, 4, 6]))