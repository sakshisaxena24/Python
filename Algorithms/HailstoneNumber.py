def generate_sequence(a, b, initial_value):
    sequence = []
    current_value = initial_value
    sequence.append(current_value)
    for _ in range(30):
        if current_value % 2 == 0:
            current_value = current_value // 2
        else:
            current_value = a * current_value + b
        sequence.append(current_value)
        if sequence[0] == current_value:  # Break if it loops back to the start
            break
    return sequence

def count_unique_patterns(a, b):
    unique_patterns = []
    total_patterns = 0
    for initial_value in range(1, 1001):  # Start sequences from 1 to 1000
        sequence = generate_sequence(a, b, initial_value)
        # Identify loops by checking if the sequence returns to its starting value
        for i in range(2, len(sequence)):
            if sequence[0] == sequence[i]:
                pattern = set(sequence[:i + 1])
                if pattern not in unique_patterns:
                    unique_patterns.append(pattern)
                    total_patterns += 1
                    break
    return total_patterns

def main():
    for a in range(1, 11):
        for b in range(1, 11):
            patterns_count = count_unique_patterns(a, b)
            print(f"Pairs ({a}, {b}) give {patterns_count} unique holding patterns.")

main()

