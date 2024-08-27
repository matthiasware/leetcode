import random
lsts = [
    [],
    [1],
    [1,2],
    [2,1],
    [1,2,3],
    [3,2,1],
    [1,1,0],
    [1,5,2,3]
]

def test_partition():
    from quicksort import partition
    lsts = [
        ([1,2,4,5,3], 0, 4, [1,2,3,5,4]),
        ([0,1], 0, 1, [0, 1]),
        ([0,3,2], 0, 2, [0,2,3]),
        ([1,0], 0, 1, [0, 1])
    ]
    for (lst_in, i_start, i_end, lst_exp) in lsts:
        lst_in = lst_in[::]
        partition(lst_in, i_start, i_end)
        assert lst_in == lst_exp

def test_insertion_sort():
    from quicksort import insertion_sort

    for act in lsts:
        print(act)
        lst = act[::]
        exp = sorted(lst)
        insertion_sort(act)
        assert exp == act


def test_quicksort():
    from quicksort import quick_sort
    for act in lsts:
        print(act)
        lst = act[::]
        exp = sorted(lst)
        quick_sort(act)
        assert exp == act

    item_min = -10
    item_max = 10
    for _ in range(100):
        size = random.randint(1, 100)
        lst = [random.randint(item_min, item_max) for _ in range(size)]
        exp = sorted(lst)
        quick_sort(lst)
        assert exp == lst


def test_merge_sort():
    from merge_sort import merge_sort

    for lst in lsts:
        act = lst[::]
        exp = sorted(lst)
        merge_sort(act, 0, len(act)-1)
        #print(exp, act)
        assert exp == act

    item_min = -10
    item_max = 10
    for _ in range(100):
        size = random.randint(1, 200)
        lst = [random.randint(item_min, item_max) for _ in range(size)]
        exp = sorted(lst)
        print(lst)
        merge_sort(lst, 0, len(lst)-1)
        print(exp, lst)
        assert exp == lst
        
if __name__ == "__main__":
    # test_quicksort()
    test_merge_sort()