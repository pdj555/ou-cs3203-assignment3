def sum_of_list(numbers):
    return sum(numbers)

def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [1, 2, 3, 4, 5]
sum_result = sum_of_list(numbers)
product_result = product_of_list(numbers)
print(f"Sum: {sum_result}, Product: {product_result}")
