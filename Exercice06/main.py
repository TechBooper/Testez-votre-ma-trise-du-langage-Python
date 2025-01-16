def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Example usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
