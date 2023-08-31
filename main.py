import random


def get_private_keys(count):
    with open("privat_key.txt", "r+") as file:
        keys = file.read().splitlines()
        selected_keys = []
        for _ in range(count):
            if len(keys) == 0:
                print("No more keys available.")
                break
            random_index = random.randint(0, len(keys) - 1)
            selected_key = keys.pop(random_index)
            selected_keys.append(selected_key)
            print(selected_key)

        file.seek(0)
        file.truncate()
        file.write("\n".join(keys))


# Задайте количество приватных ключей, которые вы хотите получить
num_keys = 25

get_private_keys(num_keys)
