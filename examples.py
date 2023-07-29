from pypipe import pipe


def do_list_example():
    nums = [1, 2, 3, 4, 5, 6, 7]
    cool_nums = pipe(nums) \
                    .map(lambda num: num ** 2) \
                    .filter(lambda num: num % 2 == 0) \
                    .filter_false(lambda num: num // 10 == 0) \
                    .reverse() \
                    .to_list()
    assert cool_nums == [36, 16]


def do_list_reduce_example():
    nums = [8, 12, 24, 4]

    reduced_cool_num = pipe(nums).reduce(lambda acc, num: num / acc, 2)  # or .fold / .foldl
    assert reduced_cool_num == 0.5

    reduced_cool_num = pipe(nums).reduce_reverse(lambda acc, num: num / acc, 2)  # or .foldr
    assert reduced_cool_num == 8.0


def do_list_reduce_inner_example():
    left_nums = [2, 8, 12, 24, 4]
    reduced_cool_num = pipe(left_nums).reduce(lambda acc, num: num / acc)  # or .foldl1
    assert reduced_cool_num == 0.5

    right_nums = [8, 12, 24, 4, 2]
    reduced_cool_num = pipe(right_nums).reduce_reverse(lambda acc, num: num / acc)  # or .foldr1
    assert reduced_cool_num == 8.0


def do_list_accumulate_example():
    nums = [4, 2, 4]
    cool_nums = pipe(nums) \
                    .accumulate(lambda acc, num: acc // num, 64) \
                    .to_list()
    assert cool_nums == [64, 16, 8, 2]


def do_list_zip_example():
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    cool_nums = pipe(nums1) \
                    .zip(nums2) \
                    .map(lambda num: num[0]+num[1]) \
                    .to_list()
    assert cool_nums == [5, 7, 9]


def do_list_zip_longest_example():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7]
    cool_nums = pipe(nums1) \
                    .zip_longest(nums2, fill_value=0) \
                    .map(lambda num: num[0]+num[1]) \
                    .to_list()
    assert cool_nums == [7, 9, 3, 4, 5]


def do_dict_example():
    nums_dict = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66, 7: 77}
    cools_nums_dict = pipe(nums_dict) \
                        .map(lambda key, value: (key, value*2)) \
                        .filter(lambda key, value: key % 3 != 0) \
                        .to_dict()
    assert cools_nums_dict == {1: 22, 2: 44, 4: 88, 5: 110, 7: 154}


def do_dict_reduce_example():
    nums_dict = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55}
    reduced_cool_item = pipe(nums_dict) \
                        .reduce(lambda acc_key, acc_value, key, value: (acc_key+key, acc_value+value), (0, 0))  # or .fold / .foldl
    assert reduced_cool_item == (15, 165)

    reduced_cool_item = pipe(nums_dict) \
                        .reduce(lambda acc_key, acc_value, key, value: (acc_key+key, acc_value+value))  # or .foldl1
    assert reduced_cool_item == (15, 165)


def do_dict_accumulate_example():
    nums_dict = {1: 4, 2: 2, 3: 4}
    cool_nums_dict = pipe(nums_dict) \
                        .accumulate(lambda acc_key, acc_value, key, value: (key, acc_value // value), (0, 64)) \
                        .to_dict()
    assert cool_nums_dict == {0: 64, 1: 16, 2: 8, 3: 2}


def do_dict_zip_example():
    nums_dict1 = {1: 1, 2: 2, 3: 3}
    nums_dict2 = {4: 4, 5: 5, 6: 6}
    cools_nums_dict = pipe(nums_dict1) \
                        .zip(nums_dict2.items()) \
                        .map(lambda key, value: (key[0]+value[0], key[1]+value[1])) \
                        .to_dict()
    assert cools_nums_dict == {5: 5, 7: 7, 9: 9}


def main():
    do_list_example()
    do_list_reduce_example()
    do_list_reduce_inner_example()
    do_list_accumulate_example()
    do_list_zip_example()
    do_list_zip_longest_example()
    do_dict_example()
    do_dict_reduce_example()
    do_dict_accumulate_example()
    do_dict_zip_example()


if __name__ == "__main__":
    main()
