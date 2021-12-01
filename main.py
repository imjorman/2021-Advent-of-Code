def count_increases():
    file = open("day_1_data.txt", "r")
    list_of_measurements = file.readlines()

    increase_counter = 1
    for measurement in range(1, len(list_of_measurements)):
        if list_of_measurements[measurement] > list_of_measurements[measurement - 1]:
            increase_counter += 1
    print(f"There are {increase_counter} measurements that are larger than the previous measurement.")
    file.close()

def sliding_window():
    file = open("day_1_data.txt", "r")
    list_of_measurements = file.readlines()
    previous_sum = 0
    increase_counter = 1

    for measurement in range(2, len(list_of_measurements) - 2):
        current_sum = int(list_of_measurements[measurement]) + int(list_of_measurements[measurement + 1]) + int(list_of_measurements[measurement + 2])
        if current_sum > previous_sum:
            increase_counter += 1
        previous_sum = current_sum
    print(increase_counter)

count_increases()
sliding_window()
