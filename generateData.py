import random


def generate_increasing_data(size):
    return list(range(1, size + 1))


def generate_decreasing_data(size):
    return list(range(size, 0, -1))


def generate_dataset(num_datasets, dataset_size):
    datasets = []
    for i in range(1, num_datasets + 1):
        if i == 1:
            dataset = generate_increasing_data(dataset_size)
        elif i == 10:
            dataset = generate_decreasing_data(dataset_size)
        else:
            # Generate random dataset of unique integers
            dataset = list(range(1, dataset_size + 1))
            random.shuffle(dataset)

        datasets.append(dataset)

    return datasets


def write_dataset_to_file(filename, dataset):
    with open(filename, "w") as file:
        for number in dataset:
            file.write(str(number) + "\n")


num_datasets = 10
dataset_size = 1000000

for i, dataset in enumerate(generate_dataset(num_datasets, dataset_size)):
    output_file = f"./data/data_{i+1}.txt"
    write_dataset_to_file(output_file, dataset)
    print("Dữ liệu đã được ghi vào file", output_file)
