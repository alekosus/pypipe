from pypipe import pipe


def do_list_example():
    nums = [1, 2, 3, 4, 5, 6, 7]
    cool_nums = pipe(nums) \
                    .map(lambda num: num ** 2) \
                    .filter(lambda num: num % 2 == 0) \
                    .reverse() \
                    .to_list()
    print(cool_nums)  # [36, 16, 4]


def do_dict_example():
    nums_dict = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66, 7: 77}
    cools_nums_dict = pipe(nums_dict) \
                        .map(lambda key, value: (key, value*2)) \
                        .filter(lambda key, value: key % 3 != 0) \
                        .to_dict()
    print(cools_nums_dict)  # {1: 22, 2: 44, 4: 88, 5: 110, 7: 154}


def main():
    do_list_example()
    do_dict_example()


if __name__ == "__main__":
    main()
