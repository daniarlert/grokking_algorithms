def binary_search(list: list[int], item: int) -> int | None:
    low = 0  # lower bound
    high = len(list) - 1  # higher bound

    while low <= high:
        mid = (low + high) // 2  # check middle element
        guess = list[mid]

        if guess == item:
            # if we've guessed the item correctly
            return mid
        elif guess > item:
            # the guess was too high
            high = mid - 1
        else:
            # the guess was too low
            low = mid + 1

    return None


if __name__ == "__main__":
    num_list = [n for n in range(100)]

    assert binary_search(num_list, 55) == 55
    assert binary_search(num_list, 99) == 99
    assert binary_search(num_list, 102) is None
