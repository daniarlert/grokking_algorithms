import random


def selection_sort(arr: list[int]) -> list[int]:
    tmp = []
    for i in range(len(arr)):
        smallest = min(arr)
        tmp.append(arr.pop(arr.index(smallest)))

    return tmp


if __name__ == "__main__":
    arr = [n for n in range(255)]
    random.shuffle(arr)

    print(selection_sort(arr))
