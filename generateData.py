import random


def generate_unique_numbers(n):
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    return numbers


num_sets = 10
num_elements = 1000000

for i in range(num_sets):
    data_set = generate_unique_numbers(num_elements)
    file_name = f"data_{i+1}.txt"
    with open(file_name, "w") as file:
        for number in data_set:
            file.write(str(number) + "\n")
    print(f"Data set {i+1} exported to {file_name}.")
